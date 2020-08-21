input_a = int(input())
input_b = int(input())


def function(a, b):
    while (a + 1) / 2 > b:
        if a % 2 != 0:
            print(-1)
            a -= 1
        else:
            print(':2')
            a /= 2
    while a - b > 0:
        print(-1)
        a -= 1


function(input_a, input_b)
