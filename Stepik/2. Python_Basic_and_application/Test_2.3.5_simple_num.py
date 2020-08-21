def primes():
    n = 1
    numbers = []
    while n < 148:
        divider = 2  # делитель, от 2 до n-1, если он есть, то число составное
        n += 1
        while divider < n - 1:
            if n % divider == 0:
                n += 1
                divider = 2
            else:
                divider += 1
        numbers.append(n)
    return numbers


my = primes()
need = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]

print(need)
print(my)