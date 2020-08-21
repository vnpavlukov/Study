class User:
    count_users = 1

    def __init__(self, name, email):  # задаем переменные
        self.name = name
        self.email = email

    # def __new__(cls):  # выполяет действия при создании класса
    #     cls.count_users += 1
    #     return cls.count_users

    # def __hash__(self):  # что-то там с хэшем связано
    #     return hash(self.name)

    def __eq__(self, other):  # что именно мы будем сравнивать при сравнении кл.
        return self.email == other.email

    def __str__(self):  # поведение при вызове функции
        return '{} <{}>'.format(self.name, self.email)

    def __getattr__(self, item):  # вызыв. если мы обращаемся к несуществ.аттриб.
        return 'Повнимательнее пожалуйста! Нет такого метода!'

    # def __getattribute__(self, item):  # постоянно вызывается
    #     return 'а вот я терь буду постоянно вызываться'

    def __delattr__(self, item):  # переопределение метода удаления аттрибута
        value = getattr(self, item)
        print(f'Goodbye {item}, you were {value}!')
        object.__delattr__(self, item)


jane = User('Jane Doe', 'jdoe@ya.ru')
joe = User('Joe Doe', 'jdoe@ya.ru')

print(jane == joe)  # True
print(jane)  # Jane Doe <jdoe@ya.ru>
print(jane.addres)
jane.addres = 'Baker street'
del jane.addres
