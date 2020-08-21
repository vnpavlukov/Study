s = input()
count_f = 0
second_pos = 0
pos = s.find('f')

if pos == -1:
    print(-2)
else:
    while pos != -1:
        pos = s.find('f', pos + 1)
        if second_pos == 0:
            second_pos = pos
    print(second_pos)
