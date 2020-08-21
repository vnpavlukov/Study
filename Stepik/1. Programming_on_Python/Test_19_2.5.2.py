data = [int(i) for i in input().split()]

data_len = len(data)
index = 0

if data_len == 1:
    print(int(data[0]))
else:
    while data_len >= index:
        try:
            num = data[index - 1] + data[index + 1]
            print(num, end=" ")
            index += 1
        except:
            num = data[index - 1] + data[0]
            print(num)
            index += 1
            break
