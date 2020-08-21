s = input()
reverse_s = s[::-1]
first_number = s.find('h')
second_number = len(s) - 1 - reverse_s.find('h')
first_part = s[0:first_number + 1]
cut_part = s[first_number + 1: second_number]
finish_part = s[second_number:]
print(first_part + cut_part + cut_part + finish_part)
