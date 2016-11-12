
import os


def getlast(path):
    return path.split(os.pathsep)[-1]


def makefolder(path):
    os.makedirs(path)
    print("directory created at /{}".format(getlast(path)))


def makefile(path):
    file = open(path, "w")
    file.close()

    print("Created new list file at {}".format(getlast(path)))


def write(content, path="lists.json"):

    with open(path, "w") as file:
        file.write(content)
