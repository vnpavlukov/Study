A = [2, False, 9.1, 2 - 1j, 'hello', 5, 'Python']
B = [5, 3, 'HELLO', 7, 12.5, 'Python', True, False]

print(A)
print(B)

i = 0

for a in A:
    i += 1
    j = 0

    for b in B:
        j += 1

        if a == b:
            txt = str(i) + ' element first list'
            txr = txt + str(j) + 'element second list'
            print(txt)
