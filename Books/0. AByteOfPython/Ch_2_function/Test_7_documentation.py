def printmax(x, y):
    '''Get max from two numbers'''

    if x > y:
        print(x, 'bigger')
    else:
        print(y, 'bigger')


print(printmax.__doc__)
printmax(3, 1)
