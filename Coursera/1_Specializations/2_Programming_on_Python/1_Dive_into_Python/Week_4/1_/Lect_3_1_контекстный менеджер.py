class open_file:
    def __init__(self, file_name, mode):
        self.f = open(file_name, mode)

    def __enter__(self):  # что происходит вначале контекстного менеджера
        return self.f

    def __exit__(self, *args):  # что происходит вконце контекстного менеджера
        self.f.close()


with open_file('test.log', 'w') as f:
    f.write('Test Messanger')
