s = input()
new_s = []

for i in s:
    new_s.append(i + '*')

new_s.remove(new_s[-1])
new_s.append(s[-1])

for a in new_s:
    print(a, end='')
