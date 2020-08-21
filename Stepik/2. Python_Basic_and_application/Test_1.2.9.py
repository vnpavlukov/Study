# objects = [1, 2, 1, 2, 3]
n = set()
for obj in objects:
    n.add(id(obj))
print(len(n))
