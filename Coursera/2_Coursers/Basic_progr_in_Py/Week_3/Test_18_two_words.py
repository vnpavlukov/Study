s = input()
find_spaсe = s.find(' ')
first_part = s[find_spaсe + 1:]
finish_part = s[:find_spaсe]
print(first_part, finish_part)
