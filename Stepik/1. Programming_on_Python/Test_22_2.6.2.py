input_num = int(input())

massiv = []

for i in range(1, input_num + 1):
    massiv += [str(i)] * i
print(" ".join(massiv[:input_num]))
