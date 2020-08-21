import os


def parent_directory():
    return os.path.abspath(os.path.join(os.getcwd(), os.pardir))


print(parent_directory())
