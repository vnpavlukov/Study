print('let`s check the contents of the list')
myList = [1, 3 + 2j, True, 4.0]
# myList = [1, 3 + 2j, 'Python', 4.0]
print('List:', myList)
for i in myList:
    if type(i) == str:
        print('there is the text element here')
        break
else:
    print('there is no text element here')
print('verification completed')
