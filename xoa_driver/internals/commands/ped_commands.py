from __future__ import annotations
from dataclasses import dataclass
import typing
import functools

from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpByte,
    XmpInt,
    XmpLong,
)
from .enums import OnOff


@register_command
@dataclass
class PED_SCHEDULE:
    """
    Configure the impairment scheduler function.  The configuration of the scheduler
    depends on the kind of distribution to schedule:      (1) Burst distributions:
    "Fixed Burst" and "Accumulate and Burst".      (2) Non-Burst distributions: All
    others.  For burst distributions, the scheduler can be configured for "One-shot"
    operation or "Repeat Operation".  When running in "Repeat Operation" the "Repeat
    Period" must be configured. For non-burst distributions,  the scheduler can be
    configured operate in either "Continuous" or "Repeat Period" modes.  When
    running in "Repeat Period" configuration of "Duration" and "Repeat Period" is
    required.
    """

    code: typing.ClassVar[int] = 1611
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        duration: int = field(XmpInt())
        """integer, specifies the "on" period. Units = multiples of 10 ms (range 1 to 65535), default is 1"""
        period: int = field(XmpInt())
        """integer, specifies the "total" period. Units = multiples of 10 ms (range 0 to 65535), default is 0"""

    class SetDataAttr(RequestBodyStruct):
        duration: int = field(XmpInt())
        """integer, specifies the "on" period. Units = multiples of 10 ms (range 1 to 65535), default is 1"""
        period: int = field(XmpInt())
        """integer, specifies the "total" period. Units = multiples of 10 ms (range 0 to 65535), default is 0"""

    def get(self) -> Token[GetDataAttr]:
        """Get the impairment scheduler configuration.

        :return: the impairment scheduler configuration
        :rtype: PED_SCHEDULE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, duration: int, period: int) -> Token[None]:
        """Set the impairment scheduler configuration.

        :param duration: specifies the "on" period. Units = multiples of 10 ms (range 1 to 65535), default is 1
        :type duration: int
        :param period: specifies the "total" period. Units = multiples of 10 ms (range 0 to 65535), default is 0
        :type period: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex, self._impairment_type_xindex],
                duration=duration,
                period=period
            )
        )


@register_command
@dataclass
class PED_ONESHOTSTATUS:
    """
    Retrieves the one-shot completion status.

    .. note::

        The return value is only valid, if the configured distribution is either accumulate & burst (DELAY) or fixed burst (non-DELAY).
        
    """

    code: typing.ClassVar[int] = 1612
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        one_shot_status: int = field(XmpByte())
        """byte, specifies the status."""

    def get(self) -> Token[GetDataAttr]:
        """Get the one-shot completion status.

        :return: the one-shot completion status
        :rtype: PED_ONESHOTSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))


@register_command
@dataclass
class PED_OFF:
    """Configure Impairments Distribution to OFF. Assigning a different distribution than OFF to an impairment
    will activate the impairment. To de-activate the impairment assign distribution OFF.
    """

    code: typing.ClassVar[int] = 1620
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Configure Impairments Distribution to OFF. Assigning a different distribution than OFF to an impairment
        will activate the impairment. To de-activate the impairment assign distribution OFF.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))


@register_command
@dataclass
class PED_FIXED:
    """
    Configuration of Fixed Rate distribution. This is predictable distribution with
    nearly equal distance between impairments, to match the configured probability.

    .. note::

        In case of misordering, a special limit applies, probability * (depth + 1) should be less than 1000000.

    """

    code: typing.ClassVar[int] = 1621
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        probability: int = field(XmpInt())
        """integer, specifies the fixed probability in ppm. Default value is 0."""

    class SetDataAttr(RequestBodyStruct):
        probability: int = field(XmpInt())
        """integer, specifies the fixed probability in ppm. Default value is 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the probability of a Fixed Rate distribution.

        :return: the fixed probability in ppm. Default value is 0.
        :rtype: PED_FIXED.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, probability: int) -> Token[None]:
        """Set the probability of a Fixed Rate distribution.

        :param probability: the fixed probability in ppm. Default value is 0.
        :type probability: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex, self._impairment_type_xindex],
                probability=probability
            )
        )


@register_command
@dataclass
class PED_RANDOM:
    """
    Configuration of Random Rate distribution. Packets are impaired randomly based
    on a per packet probability. This way the impaired fraction of packets will be
    equal to the configured probability over time. Random probability in ppm (i.e. 1
    means 0.0001%)
    """

    code: typing.ClassVar[int] = 1622
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        probability: int = field(XmpInt())
        """integer, specifies the random probability in ppm. Default value is 0."""

    class SetDataAttr(RequestBodyStruct):
        probability: int = field(XmpInt())
        """integer, specifies the random probability in ppm. Default value is 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the probability of a Random Rate distribution.

        :return: specifies the random probability in ppm. Default value is 0.
        :rtype: PED_RANDOM.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, probability: int) -> Token[None]:
        """Set the probability of a Random Rate distribution.

        :param probability: specifies the random probability in ppm. Default value is 0.
        :type probability: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex, self._impairment_type_xindex],
                probability=probability
            )
        )


@register_command
@dataclass
class PED_BER:
    """
    Configuration of Bit Error Rate distribution.
    """

    code: typing.ClassVar[int] = 1623
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        coef: int = field(XmpInt())
        """integer, specifies the coefficient for BER. Default value: 1 (Range is 1 to 9)."""
        exp: int = field(XmpInt())
        """integer, specifies the exponent for BER. Default value: -10 (Range is -18 to -1)."""

    class SetDataAttr(RequestBodyStruct):
        coef: int = field(XmpInt())
        """integer, specifies the coefficient for BER. Default value: 1 (Range is 1 to 9)."""
        exp: int = field(XmpInt())
        """integer, specifies the exponent for BER. Default value: -10 (Range is -18 to -1)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Bit Error Rate distribution.

        :return: the configuration of Bit Error Rate distribution
        :rtype: PED_BER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, coef: int, exp: int) -> Token[None]:
        """Set the configuration of Bit Error Rate distribution.

        :param coef: specifies the coefficient for BER. Default value: 1 (Range is 1 to 9).
        :type coef: int
        :param exp: specifies the exponent for BER. Default value: -10 (Range is -18 to -1).
        :type exp: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], coef=coef, exp=exp))


@register_command
@dataclass
class PED_FIXEDBURST:
    """
    Configuration of Fixed Burst distribution.

    .. note::

        In case of ``_impairment_type_xindex`` = ``MISO``, burst size is fixed to 1.

    """

    code: typing.ClassVar[int] = 1624
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        burst_size: int = field(XmpInt())
        """integer, specifies the burst size (Range 1 - 16383). Default value = 1."""

    class SetDataAttr(RequestBodyStruct):
        burst_size: int = field(XmpInt())
        """integer, specifies the burst size (Range 1 - 16383). Default value = 1."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Fixed Burst distribution.

        :return: configuration of Fixed Burst distribution.
        :rtype: PED_FIXEDBURST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, burst_size: int) -> Token[None]:
        """Set the configuration of Fixed Burst distribution.

        :param burst_size: specifies the burst size (Range 1 - 16383). Default value = 1.
        :type burst_size: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], burst_size=burst_size)
        )


@register_command
@dataclass
class PED_RANDOMBURST:
    """
    Configuration of Random Burst distribution.
    """

    code: typing.ClassVar[int] = 1625
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        minimum: int = field(XmpInt())
        """integer, specifies minimum burst size. Default value: 0 (Range 0 to 65535)"""
        maximum: int = field(XmpInt())
        """integer, specifies maximum burst size. Default value: 0 (Range 0 to 65535)"""
        probability: int = field(XmpInt())
        """integer, specifies the per packet probability of initiating a burst in ppm. Default value: 0."""

    class SetDataAttr(RequestBodyStruct):
        minimum: int = field(XmpInt())
        """integer, specifies minimum burst size. Default value: 0 (Range 0 to 65535)"""
        maximum: int = field(XmpInt())
        """integer, specifies maximum burst size. Default value: 0 (Range 0 to 65535)"""
        probability: int = field(XmpInt())
        """integer, specifies the per packet probability of initiating a burst in ppm. Default value: 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Random Burst distribution.

        :return: configuration of Random Burst distribution.
        :rtype: PED_RANDOMBURST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, minimum: int, maximum: int, probability: int) -> Token[None]:
        """Set the configuration of Random Burst distribution.

        :param minimum: specifies minimum burst size. Default value: 0 (Range 0 to 65535)
        :type minimum: int
        :param maximum: specifies maximum burst size. Default value: 0 (Range 0 to 65535)
        :type maximum: int
        :param probability: specifies the per packet probability of initiating a burst in ppm. Default value: 0.
        :type probability: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex, self._impairment_type_xindex],
                minimum=minimum,
                maximum=maximum,
                probability=probability
            )
        )


@register_command
@dataclass
class PED_GE:
    """
    Configuration of Gilbert-Elliot distribution.
    """

    code: typing.ClassVar[int] = 1626
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        good_state_prob: int = field(XmpInt())
        """integer, specifies the good state probability in ppm. Default value: 0."""
        good_state_trans_prob: int = field(XmpInt())
        """integer, specifies the good state transition probability in ppm. Default value: 0."""
        bad_state_prob: int = field(XmpInt())
        """integer, specifies the bad state probability in ppm. Default value: 0."""
        bad_state_trans_prob: int = field(XmpInt())
        """integer, specifies the bad state transition probability in ppm. Default value: 0."""

    class SetDataAttr(RequestBodyStruct):
        good_state_prob: int = field(XmpInt())
        """integer, specifies the good state probability in ppm. Default value: 0."""
        good_state_trans_prob: int = field(XmpInt())
        """integer, specifies the good state transition probability in ppm. Default value: 0."""
        bad_state_prob: int = field(XmpInt())
        """integer, specifies the bad state probability in ppm. Default value: 0."""
        bad_state_trans_prob: int = field(XmpInt())
        """integer, specifies the bad state transition probability in ppm. Default value: 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Gilbert-Elliot distribution.

        :return: the configuration of Gilbert-Elliot distribution.
        :rtype: PED_GE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, good_state_prob: int, good_state_trans_prob: int, bad_state_prob: int, bad_state_trans_prob: int) -> Token[None]:
        """Set the configuration of Gilbert-Elliot distribution.

        :param good_state_prob: specifies the good state probability in ppm. Default value: 0.
        :type good_state_prob: int
        :param good_state_trans_prob: specifies the good state transition probability in ppm. Default value: 0.
        :type good_state_trans_prob: int
        :param bad_state_prob: specifies the bad state probability in ppm. Default value: 0.
        :type bad_state_prob: int
        :param bad_state_trans_prob: specifies the bad state transition probability in ppm. Default value: 0.
        :type bad_state_trans_prob: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex, self._impairment_type_xindex],
                good_state_prob=good_state_prob,
                good_state_trans_prob=good_state_trans_prob,
                bad_state_prob=bad_state_prob,
                bad_state_trans_prob=bad_state_trans_prob
            )
        )


@register_command
@dataclass
class PED_UNI:
    """
    Configuration of Uniform distribution.

    .. note::

        If minimum is less than minimum , value is set to minimum. If minimum is greater than maximum, value is set to maximum.

    """

    code: typing.ClassVar[int] = 1627
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        minimum: int = field(XmpLong())
        """long, in case of iid != DELAY, specifies the minimum no. of packets. Default value: 0 (Range 0 to 4194288).
        In case of iid = DELAY, specifies the minimum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.
        """
        maximum: int = field(XmpLong())
        """long, in case of iid != DELAY, specifies the maximum no. of packets. Default value: 0 (Range 0 to 4194288).
        In case of iid = DELAY, specifies the maximum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.
        """

    class SetDataAttr(RequestBodyStruct):
        minimum: int = field(XmpLong())
        """long, in case of iid != DELAY, specifies the minimum no. of packets. Default value: 0 (Range 0 to 4194288).
        In case of iid = DELAY, specifies the minimum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.
        """
        maximum: int = field(XmpLong())
        """long, in case of iid != DELAY, specifies the maximum no. of packets. Default value: 0 (Range 0 to 4194288).
        In case of iid = DELAY, specifies the maximum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Uniform distribution.

        :return: the configuration of Uniform distribution.
        :rtype: PED_UNI.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, minimum: int, maximum: int) -> Token[None]:
        """Set the configuration of Uniform distribution.

        :param minimum: in case of iid != DELAY, specifies the minimum no. of packets. Default value: 0 (Range 0 to 4194288).
            In case of iid = DELAY, specifies the minimum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.
        :type minimum: int
        :param maximum: in case of iid != DELAY, specifies the maximum no. of packets. Default value: 0 (Range 0 to 4194288).
            In case of iid = DELAY, specifies the maximum latency limit. Unit is nanosecond (must be multiples of 100 ns). Default value: minimum latency.
        :type maximum: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], minimum=minimum, maximum=maximum)
        )


@register_command
@dataclass
class PED_GAUSS:
    """
    Configuration of Gaussian distribution.

    .. note::

        In case of ``_impairment_type_xindex != DELAY``:
            (1) mean plus 3 times standard deviation should be less than or equal to max allowed (4194288).
            (2) mean should always be at least 3 times the standard deviation, this to ensure that the impairment distance is always positive.

        In case of ``_impairment_type_xindex = DELAY``:
            (1) mean plus 3 times standard deviation should be less than or equal to the maximum latency.
            (2) mean minus 3 times the standard deviation should be greater than or equal to minimum latency.

    """

    code: typing.ClassVar[int] = 1628
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        mean: int = field(XmpLong())
        """long, specifies the Gaussian mean. In case of iid != DELAY, specifies the Gaussian mean value as number of packets.Default value: 0 packets (Range 0 to 4194288).
        In case of iid = DELAY, specifies the Gaussian mean value. Units is nanosecond (must be multiples of 100 ns).
        """
        std_deviation: int = field(XmpLong())
        """long, specifies the Gaussian standard deviation. In case of iid != DELAY, specifies the standard deviation as number of packets.
        Default value: 0 packets (Range 0 to 4194288). In case of iid = DELAY, specifies the the Gaussian standard deviation.
        Units is nanosecond (must be multiples of 100 ns). Default value: 0 ns.
        """

    class SetDataAttr(RequestBodyStruct):
        mean: int = field(XmpLong())
        """long, specifies the Gaussian mean. In case of iid != DELAY, specifies the Gaussian mean value as number of packets.Default value: 0 packets (Range 0 to 4194288).
        In case of iid = DELAY, specifies the Gaussian mean value. Units is nanosecond (must be multiples of 100 ns)."""
        std_deviation: int = field(XmpLong())
        """long, specifies the Gaussian standard deviation. In case of iid != DELAY, specifies the standard deviation as number of packets.
        Default value: 0 packets (Range 0 to 4194288). In case of iid = DELAY, specifies the the Gaussian standard deviation.
        Units is nanosecond (must be multiples of 100 ns). Default value: 0 ns.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Gaussian distribution.

        :return: the configuration of Gaussian distribution
        :rtype: PED_GAUSS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, mean: int, std_deviation: int) -> Token[None]:
        """Set the configuration of Gaussian distribution.

        :param mean: specifies the Gaussian mean.
        :type mean: int
        :param std_deviation: specifies the Gaussian standard deviation.
        :type std_deviation: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], mean=mean, std_deviation=std_deviation)
        )


@register_command
@dataclass
class PED_POISSON:
    """
    Configuration of "Poisson" distribution.

    .. note::

        Standard deviation is derived from mean, i.e., standard deviation = SQRT(mean).

        In case of ``_impairment_type_xindex != DELAY``, mean plus 3 times standard deviation should be less than or equal to max allowed (4194288).

        In case of ``_impairment_type_xindex = DELAY``, mean plus 3 times standard deviation should be less than or equal to the maximum latency.

    """

    code: typing.ClassVar[int] = 1629
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        mean: int = field(XmpLong())
        """long, specifies the Poisson mean value. In case of iid = DELAY specifies the Poisson mean. Unit is nanosecond (must be multiples of 100ns).
        Default value: 0 ns. In case of iid != DELAY specifies the Poisson mean in number of packets packets. Default value: 9 packets (Range 0 to 4194288).
        """

    class SetDataAttr(RequestBodyStruct):
        mean: int = field(XmpLong())
        """long, specifies the Poisson mean value. In case of iid = DELAY specifies the Poisson mean. Unit is nanosecond (must be multiples of 100ns).
        Default value: 0 ns. In case of iid != DELAY specifies the Poisson mean in number of packets packets. Default value: 9 packets (Range 0 to 4194288).
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Poisson distribution.

        :return: the configuration of Poisson distribution
        :rtype: PED_POISSON.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, mean: int) -> Token[None]:
        """Set the configuration of Poisson distribution.

        :param mean: specifies the Poisson mean value.
        :type mean: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], mean=mean))


@register_command
@dataclass
class PED_GAMMA:
    """
    Configuration of Gamma distribution.

    .. note::

        Mean and Standard deviation are calculated from Shape and Scale parameters and validation is performed using those.
        standard deviation = [SQRT(shape * scale * scale)]mean = [shape * scale].

        In case of ``_impairment_type_xindex != DELAY``,
        (1) mean plus 4 times standard deviation should be less than or equal to max allowed(4194288).
        (2)shape and scale should be greater than or equal to 0.

        In case of ``_impairment_type_xindex = DELAY``, mean plus 4 times standard deviation should be less than or equal to the maximum latency.

    """

    code: typing.ClassVar[int] = 1630
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        shape: int = field(XmpLong())
        """long, specifies the shape. Units: none. Default value: 0."""
        scale: int = field(XmpLong())
        """long, specifies the Gamma function scale parameter. In case of iid = DELAY, units: nanosecond
        (must be multiples of 100 ns). Default value: 0 ns. In case of iid != DELAY, units: number of packets.Default value: 0 packets.
        """

    class SetDataAttr(RequestBodyStruct):
        shape: int = field(XmpLong())
        """long, specifies the shape. Units: none. Default value: 0."""
        scale: int = field(XmpLong())
        """long, specifies the Gamma function scale parameter. In case of iid = DELAY, units: nanosecond (must be multiples of 100 ns). Default value: 0 ns.
        In case of iid != DELAY, units: number of packets.Default value: 0 packets.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Gamma distribution.

        :return: the configuration of Gamma distribution
        :rtype: PED_GAMMA.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, shape: int, scale: int) -> Token[None]:
        """Set the configuration of Gamma distribution.

        :param shape: specifies the shape. Units: none. Default value: 0.
        :type shape: int
        :param scale: specifies the Gamma function scale parameter.
        :type scale: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex, self._impairment_type_xindex],
                shape=shape,
                scale=scale
            )
        )


@register_command
@dataclass
class PED_CUST:
    """
    Associate a custom distribution to a flow and impairment type.

    .. note::

        Before associating a custom distribution, the below validation checks are applied.

        In case of ``_impairment_type_xindex != DELAY``,
        (1) Custom values should be less than or equal to max allowed (4194288).
        (2) Custom distribution bust contain 512 values.

        In case of ``_impairment_type_xindex = DELAY``,
        (1) Custom values should be less than or equal to the maximum latency.
        (2) Custom values should be greater than or equal to minimum latency.
        (3) Custom distribution should contain 1024 values.

    """

    code: typing.ClassVar[int] = 1631
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        cust_id: int = field(XmpInt())
        """integer, custom distribution identifier."""

    class SetDataAttr(RequestBodyStruct):
        cust_id: int = field(XmpInt())
        """integer, custom distribution identifier."""

    def get(self) -> Token[GetDataAttr]:
        """Get the custom distribution identifier that is associated to a flow and impairment type.

        :return: custom distribution identifier
        :rtype: PED_CUST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, cust_id: int) -> Token[None]:
        """Associate a custom distribution to a flow and impairment type.

        :param cust_id: custom distribution identifier
        :type cust_id: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], cust_id=cust_id))


@register_command
@dataclass
class PED_CONST:
    """
    Configuration of Constant Delay distribution (DELAY only). Unit is ns (must be
    multiples of 100ns). Default value: Minimum supported per speed and FEC mode.

    .. note::

        If the latency is less than minimum latency, value is set to minimum latency. If the latency is greater than maximum latency, value is set to maximum latency.

    """

    code: typing.ClassVar[int] = 1640
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        delay: int = field(XmpLong())
        """long, specifies the constant delay/latency time. Unit is nanosecond (must be multiples of 100 ns). Default value: Minimum supported per speed and FEC mode."""

    class SetDataAttr(RequestBodyStruct):
        delay: int = field(XmpLong())
        """long, specifies the constant delay/latency time. Unit is nanosecond (must be multiples of 100 ns). Default value: Minimum supported per speed and FEC mode."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Constant Delay distribution (DELAY only).

        :return: the configuration of Constant Delay distribution (DELAY only)
        :rtype: PED_CONST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, delay: int) -> Token[None]:
        """Set the configuration of Constant Delay distribution (DELAY only).

        :param delay: specifies the constant delay/latency time. Unit is nanosecond (must be multiples of 100 ns). Default value: Minimum supported per speed and FEC mode.
        :type delay: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], delay=delay))


@register_command
@dataclass
class PED_ACCBURST:
    """
    Configuration of Accumulate & Burst distribution (DELAY only).

    .. note::

        If the delay is less than minimum latency, value is set to minimum latency. If the delay is greater than maximum latency, value is set to maximum latency.

    """

    code: typing.ClassVar[int] = 1641
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        delay: int = field(XmpLong())
        """long, specifies the burst delay time. Units = nanosecond (must multiples of 100 ns). Default value: minimum latency."""

    class SetDataAttr(RequestBodyStruct):
        delay: int = field(XmpLong())
        """long, specifies the burst delay time. Units = nanosecond (must multiples of 100 ns). Default value: minimum latency."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Accumulate & Burst distribution (DELAY only).

        :return: the configuration of Accumulate & Burst distribution (DELAY only)
        :rtype: PED_ACCBURST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, delay: int) -> Token[None]:
        """Set the configuration of Accumulate & Burst distribution (DELAY only).

        :param delay: specifies the burst delay time. Units = nanosecond (must multiples of 100 ns). Default value: minimum latency.
        :type delay: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], delay=delay))


@register_command
@dataclass
class PED_STEP:
    """
    Configuration of Step distribution (DELAY only).

    .. note::

        If the low/high is less than minimum latency, value is set to minimum latency. If the low/high is greater than maximum latency, value is set to maximum latency.

    """

    code: typing.ClassVar[int] = 1642
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        low: int = field(XmpLong())
        """long, specifies the packet delay in the 'low' state of the step. Units = nanosecond (must be multiples of 100 ns)."""
        high: int = field(XmpLong())
        """long, specifies the packet delay in the 'high' state of the step. Units = nanosecond (must be multiples of 100 ns)."""

    class SetDataAttr(RequestBodyStruct):
        low: int = field(XmpLong())
        """long, specifies the packet delay in the 'low' state of the step. Units = nanosecond (must be multiples of 100 ns)."""
        high: int = field(XmpLong())
        """long, specifies the packet delay in the 'high' state of the step. Units = nanosecond (must be multiples of 100 ns)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of Step distribution (DELAY only).

        :return: the configuration of Step distribution (DELAY only)
        :rtype: PED_STEP.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, low: int, high: int) -> Token[None]:
        """Set the configuration of Step distribution (DELAY only).

        :param low: specifies the packet delay in the 'low' state of the step. Units = nanosecond (must be multiples of 100 ns).
        :type low: int
        :param high: specifies the packet delay in the 'high' state of the step. Units = nanosecond (must be multiples of 100 ns).
        :type high: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], low=low, high=high))


@register_command
@dataclass
class PED_ENABLE:
    """
    Control whether this impairment distribution is enabled.

    .. note::

        This command is not applicable for PE_BANDPOLICER and PE_BANDSHAPER because they have a separate ``ON / OFF`` parameter.

    """

    code: typing.ClassVar[int] = 1644
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _impairment_type_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        action: OnOff = field(XmpByte())
        """coded byte, specifying whether impairment is enabled."""

    class SetDataAttr(RequestBodyStruct):
        action: OnOff = field(XmpByte())
        """coded byte, specifying whether impairment is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of this impairment distribution.

        :return: the status of this impairment distribution
        :rtype: PED_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex]))

    def set(self, action: OnOff) -> Token[None]:
        """Set the status of this impairment distribution.

        :param action: the status of this impairment distribution
        :type action: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._impairment_type_xindex], action=action))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable impairment distribution"""

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable impairment distribution"""
