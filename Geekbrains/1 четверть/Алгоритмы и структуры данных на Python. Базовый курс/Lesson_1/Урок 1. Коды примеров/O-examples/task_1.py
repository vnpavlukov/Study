import time


def check_1(n):
    start_val = time.time()
    res = 0
    for i in range(1, n + 1):
        res = res + i
    end_val = time.time()
    return res, end_val - start_val


for i in range(5):
    print(f'{check_1(10000)[0]} Операция заняла {check_1(10000)[1]} сек')

print()
for i in range(5):
    print(f'Операция заняла {check_1(100000)[1]} сек')
print()
for i in range(5):
    print(f'Операция заняла {check_1(10000000)[1]} сек')
