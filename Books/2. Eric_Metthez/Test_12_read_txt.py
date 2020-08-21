with open('Test_12.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())
print()

with open('Test_12.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print()

with open('Test_12.txt') as file_object:
    lines = file_object.readlines()
    print(lines)
print()

for line in lines:
    print(line.rstrip())


string = ''
for line in lines:
    string += line.strip() + ' '
print(string)
print(len(string))
