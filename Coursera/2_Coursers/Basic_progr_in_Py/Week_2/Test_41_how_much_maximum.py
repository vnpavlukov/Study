input_number = int(input())
my_list = [input_number]

while input_number != 0:
    input_number = int(input())
    my_list.append(input_number)

my_list.sort()

print(my_list.count(my_list[-1]))
