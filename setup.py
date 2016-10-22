
from setuptools import setup

setup(
    name="booklist",
    description="Keeps track of the books you want to read!",

    version="0.0.5",
    license="MIT",

    url="https://github.com/apizzimenti/booklist.git",
    author="Anthony Pizzimenti",
    author_email="pizzimentianthony@gmail.com",

    packages=["booklist"],

    install_requires="termcolor",

    entry_points={
        "console_scripts": ["booklist=booklist.index:main"]
    }
)