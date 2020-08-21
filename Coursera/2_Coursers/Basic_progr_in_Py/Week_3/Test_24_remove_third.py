s = input()
my_list = list(s)
x = 0
for i in range(0, len(my_list), 3):
    x += 1

for i in range(0, x * 2, 2):
    my_list.pop(i)

for z in my_list:
    print(z, end='')
