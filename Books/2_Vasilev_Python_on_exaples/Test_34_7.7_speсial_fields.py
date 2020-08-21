class Alpha:
    "Класс альфа и внутренний класс браво"

    def hello():
        pass

    class Bravo:
        pass


class Charlie(Alpha):
    pass


class Delta(Charlie):
    pass


obj = Alpha()

print("Field odj.__class__: \n", obj.__class__, '\n')
print("Field Alpha.__class__: \n", Alpha.__class__, '\n')
print("Field Alpha.Bravo.__class__: \n", Alpha.Bravo.__class__, '\n')
print("Field Charlie.__class__: \n", Charlie.__class__, '\n')

print("Delta __bases__ & __mro__:", Delta.__bases__, Delta.__mro__, '\n',
      "Alpha __bases__ & __mro__:", Alpha.__bases__, Alpha.__mro__, '\n',
      sep='\n')

print(
    "Module class Alpha:", Alpha.__module__, '\n' * 2,
    "Dict class Alpha:", Alpha.__dict__, '\n' * 2,
    "Dict class Alpha.Bravo:", Alpha.Bravo.__dict__, '\n' * 2,

)
