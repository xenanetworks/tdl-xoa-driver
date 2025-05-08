import setuptools


def main():
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="tdl-xoa-driver",
        description=(
            "XOA Driver is a Python library providing user-friendly communication"
            " interfaces to Xena Traffic Generation test equipment."
            " It provides a rich collection of programming interfaces that can be used to either write"
            " test scripts or develop applications."
        ),
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Leonard Yu",
        author_email="leonard.yu@teledyne.com",
        maintainer="Teledyne LeCroy Xena",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenanetworks/tdl-xoa-driver",
        packages=setuptools.find_packages(),
        license='Apache 2.0',
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
        ],
        python_requires=">=3.11",
    )


if __name__ == '__main__':
    main()
