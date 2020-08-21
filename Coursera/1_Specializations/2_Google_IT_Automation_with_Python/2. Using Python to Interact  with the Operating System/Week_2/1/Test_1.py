import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'w') as f:
        f.write(comments)
    return os.path.getsize(filename)


print(create_python_script("program.py"))
