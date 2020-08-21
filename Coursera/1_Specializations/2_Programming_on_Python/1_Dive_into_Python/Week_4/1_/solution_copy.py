import os
import tempfile


class File:
    def __init__(self, name):
        self.name = name
        if not os.path.exists(self.name):
            open(name, mode='w', encoding='utf8').close()

    def read(self):
        file = open(self.name, mode='r', encoding='utf8')
        text_file = file.read()
        file.close()
        return text_file

    def write(self, text):
        file = open(self.name, mode='w', encoding='utf8')
        file.write(text)
        file.close()

    def __add__(self, other):
        new_file = File(tempfile.NamedTemporaryFile().name)
        new_file.write(self.read() + other.read())
        return new_file

    def __str__(self):
        return os.path.abspath(self.name)

    def __iter__(self):
        self.file = open(self.name)
        return self

    def __next__(self):
        new_file = self.file
        new_line = new_file.readline()
        if new_line:
            return new_line
        else:
            self.file.close()
            raise StopIteration
