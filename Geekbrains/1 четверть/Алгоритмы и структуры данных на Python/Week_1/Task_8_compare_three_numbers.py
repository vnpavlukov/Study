"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

# tests = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# for test in tests:
#     a, b, c = test
#     print(test)
#
#     if a > b:
#         if a > c:
#             if b > c:
#                 print(b)
#             else:
#                 print(c)
#         else:
#             print(a)
#     else:
#         if b > c:
#             if a > c:
#                 print(a)
#             else:
#                 print(c)
#         else:
#             print(b)

a, b, c = map(int, input('Что бы найти среднее из трех чисел, введите три числа через пробел: ').split())

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)
