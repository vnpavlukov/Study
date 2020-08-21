input_string = input()
find = input()
find_from = 0
num_of_matches = 0

while True:
    if input_string.find(find, find_from) == -1:
        break
    else:
        find_from = input_string.find(find, find_from) + 1
        num_of_matches += 1

print(num_of_matches)