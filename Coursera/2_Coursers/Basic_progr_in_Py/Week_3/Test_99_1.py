s = input()
reverse_s = s[::-1]
first_number = s.find('f')
second_number = len(s) - 1 - reverse_s.find('f')

if first_number == second_number:
    print(first_number)
else:
    print(first_number, second_number)
