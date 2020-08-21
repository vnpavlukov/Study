input_num = [int(i) for i in input().split()]
num = int(input())
list = []
a = len(input_num) - 1
if num in input_num:
    for i in range(0, a + 1):
        if input_num[i]==num:
            list.append(i)
    g = len(list) - 1
    for j in range(0,g+1):
        print(list[j], end=' ')
else:
    print('Отсутствует')