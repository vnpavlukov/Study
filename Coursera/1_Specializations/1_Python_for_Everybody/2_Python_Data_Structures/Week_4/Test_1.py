fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)
print(sorted(lst))
