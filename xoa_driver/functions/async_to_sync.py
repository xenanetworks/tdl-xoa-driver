
"""
Xena Async-to-Sync Bridge

The APIs provided by tdl-xoa-driver are async functions. 
This means any function that uses the tdl-xoa-driver must be 
declared as async. 

This might be a problem for you if your existing framework 
doesn't support async functions. To solve this "incompatibility" 
issue, we have made a class **XenaAsyncToSyncBridge** 
for you to wrap tdl-xoa-driver's async function inside and use it 
as a regular Python function.
"""

from typing import (
    Any, 
    TypeVar, 
    Coroutine
)
import asyncio
import threading
import queue

T = TypeVar("T")

class XenaAsyncToSyncBridge:
    """Run XOA coroutines from synchronous code.

    The bridge runs an asyncio event loop on a dedicated background thread.
    Calling the bridge blocks until the coroutine completes and returns its
    result. Use it from a synchronous thread, not from the bridge's event-loop
    thread.

    Call :meth:`close` when finished to stop the background thread.

    Example:

    .. code-block:: python
        
        import asyncio
        from xoa_driver import testers, modules, ports
        from xoa_driver.hlfuncs import mgmt, async_to_sync

        # initialize async-to-sync bridge
        xab = async_to_sync.XenaAsyncToSyncBridge()

        # check if it starts to work
        while not xab.is_thread_started():
            time.sleep(0.01)

        # create a tester instance
        # this will automatically create a tcp connection to the tester
        tester = xab(testers.L23Tester(host=CHASSIS_IP, username=USERNAME))

        # obtain a module instance
        module = tester.modules.obtain(MODULE_IDX)

        # Obtain a port from the module
        port = module.ports.obtain(PORT_IDX)

        # reserve & reset port
        xab(mgmt.reserve_ports(ports=[port], reset=True))

        xab(asyncio.sleep(5))

        # create a stream
        stream = xab(port.streams.create())
        xab(utils.apply(
            stream.enable.set_on(),
            stream.comment.set(f"Stream A to B"),
            stream.rate.pps.set(stream_rate_pps=10000),
            stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000),
            stream.tpld_id.set(test_payload_identifier = 0))
            )
        
        # start and stop traffic
        xab(port.traffic.state.set_start())
        time.sleep(TRAFFIC_DURATION)
        xab(port.traffic.state.set_stop())
        time.sleep(COOLDOWN_DURATION)

    """

    
    __slots__ = ("loop", "thread", "_events")

    def __init__(self) -> None:
        """Start the background thread that will run the event loop.

        The loop may not be running immediately when this method returns.
        """
        self.loop: asyncio.AbstractEventLoop | None = None
        self.thread = threading.Thread(target=self._run_event_loop)
        self.thread.start()
        self._events = queue.Queue()

    def _run_event_loop(self):
        """Create and run the event loop on the background thread."""
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def run_coroutine_threadsafe(self, coro: Coroutine[Any, Any, T]) -> T:
        """Submit a coroutine to the background loop and block for its result.

        Args:
            coro: The coroutine to run.

        Returns:
            The value returned by the coroutine.

        Raises:
            RuntimeError: If the event loop has not been initialized.
            Exception: Any exception raised by the coroutine.
        """
        if not self.loop:
            raise RuntimeError("Event loop is not running")
        future_ = asyncio.run_coroutine_threadsafe(coro, self.loop)
        if exc := future_.exception():
            raise exc
        return future_.result()

    def is_thread_started(self) -> bool:
        """Return whether the background event loop is running."""
        return self.loop is not None and self.loop.is_running()

    def close(self) -> None:
        """Request the event loop to stop and wait for its thread to exit."""
        if not self.loop:
            return None
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join()

    def __call__(self, coro):
        """Run a coroutine on the background loop and block for its result.

        Args:
            coro: The coroutine to run.

        Returns:
            The value returned by the coroutine.
        """
        if self.loop is None:
            raise RuntimeError("Thread not started")

        event = asyncio.Event()

        def _callback(fut):
            self._events.put((fut.result(), fut.exception()))
            assert self.loop is not None  # Type guard for type checker
            self.loop.call_soon_threadsafe(event.set)

        async def _runner():
            try:
                fut = asyncio.ensure_future(coro)
                fut.add_done_callback(_callback)
                await event.wait()
            except Exception as exc:
                self._events.put((None, exc))

        asyncio.run_coroutine_threadsafe(_runner(), self.loop)
        result, exc = self._events.get()

        if exc:
            raise exc
        return result
