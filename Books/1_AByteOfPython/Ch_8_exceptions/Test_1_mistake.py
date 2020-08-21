try:
    text = input('Give me something:')
except EOFError:
    print('Don`t do it any more please!!!')
else:
    print('You are give {0}'.format(text))