class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value

        with open('log.txt', 'a') as f:
            f.write('{};'.format(str(value)))


class Account:
    amount = ImportantValue(100)


bobs_account = Account()
bobs_account.amount = 150

bobs_account.amount = 200
