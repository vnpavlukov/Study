new_file = open('Test_2.4.1_read_from_file_2.txt', 'r')

first_read = new_file.read().splitlines()

print(first_read)

new_file.close()

# ['First line', 'Second line', 'Third line']
