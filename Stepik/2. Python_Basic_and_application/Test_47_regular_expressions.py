import re

pattern = r"(test)"
string = "testtest"
print('1:\t', re.match(pattern, string))
print("\tв лекции  match='testtest")

pattern = r"(test|text)"
string = "testtext"
print('2:\t', re.match(pattern, string))

pattern = r"abc|(test|text)"
print('3:\t', re.match(pattern, string))

pattern = r"abc|(test|text)"
string = "abc"
print('4:\t', re.match(pattern, string))

pattern = r"((abc)|(test|text)*)"
print('5:\t', re.match(pattern, string), '\n',
      re.match(pattern, string).groups())

pattern = r"((abc)|(test|text)*)"
string = "abc"
print('5:\t', re.match(pattern, string), '\n',
      re.match(pattern, string).groups())