x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())

len_1 = (((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5)
len_2 = (((x_3 - x_1) ** 2 + (y_3 - y_1) ** 2) ** 0.5)
len_3 = (((x_3 - x_2) ** 2 + (y_3 - y_2) ** 2) ** 0.5)

print(len_1 + len_2 + len_3)
