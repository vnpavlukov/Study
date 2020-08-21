class exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):  # что происходит вначале контекстного менеджера
        return

    def __exit__(self, exc_type, exc_value,
                 traceback):  # что происходит вконце контекстного менеджера
        if exc_type == self.exc_type:
            print('Nothing happend')
            return True


with exception('test.log', 'w') as f:
    f.write('Test Messanger')
