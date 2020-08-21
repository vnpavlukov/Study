a = input()
a = a.lower()

g = a.count('g')
c = a.count('c')
a_length = len(a)

print(float((g+c)/a_length*100))
