
from setuptools import setup

setup(
    name="bookend",
    description="Keeps track of the books you want to read!",

    version="0.0.6",
    license="MIT",

    url="https://github.com/apizzimenti/bookend.git",
    author="Anthony Pizzimenti",
    author_email="pizzimentianthony@gmail.com",

    packages=["bookend"],

    install_requires="termcolor",

    entry_points={
        "console_scripts": ["bookend=bookend.index:main"]
    }
)