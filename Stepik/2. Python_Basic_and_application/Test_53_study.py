import re

pattern = r'AV '
text = 'AV something else'

result = re.match(pattern, text)
print(result.group(0))
print(result.start())
print(result.end())

pattern = r'в'
text = 'Привет, привет'
print(re.split(pattern, text))

pattern = re.compile('AV')
result = pattern.findall('AV gjkfjdsaflsdjfa')
print(result)
result = pattern.findall("AV asdf AV")
print(result)