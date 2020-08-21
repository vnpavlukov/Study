dna = str(input())

count = 1
a = 1
dna_data = dna[a:a + 1]

for i in dna:
    if i in dna_data:
        count += 1
    else:
        print(i, end='')
        print(count, end='')
        count = 1
    a += 1
    dna_data = dna[a:a + 1]
