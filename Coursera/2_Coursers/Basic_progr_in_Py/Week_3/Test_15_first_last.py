s = input()
reverse_s = s[::-1]
first_number = s.find('h')
second_number = len(s) - 1 - reverse_s.find('h')

start_string = s[0:first_number]
finish_string = s[second_number + 1:]

print(start_string + finish_string)
