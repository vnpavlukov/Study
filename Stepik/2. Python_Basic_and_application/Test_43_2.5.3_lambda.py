x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

# def length(name):
#     return len(" ".join(name))
#
#
# name_length = [length(name) for name in x]
# print(name_length)
#
# x.sort(key=length)
x.sort(key=lambda name: len(" ".join(name)))
print(x)
