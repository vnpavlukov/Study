class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename) as file:
                data = file.read()
            return data
        except OSError:
            return ''
