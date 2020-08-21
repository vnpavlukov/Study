import os


def new_directory(directory, filename):
    if not os.path.isdir(directory):
        os.makedirs(directory)
    os.chdir(directory)
    with open(filename, 'w') as file:
        pass

    return os.listdir()


print(new_directory("PythonPrograms", "script.py"))
