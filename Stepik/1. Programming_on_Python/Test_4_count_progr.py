n = int(input())
if 10 < n % 100 < 20 or 4 < n % 10 <= 9 or n % 10 == 0:
    print(n, 'программистов')
elif 1 < n % 10 < 5:
    print(n, 'программиста')
elif n % 10 == 1 and n != 11:
    print(n, 'программист')
