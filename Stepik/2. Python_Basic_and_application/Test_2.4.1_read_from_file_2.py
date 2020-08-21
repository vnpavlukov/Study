new_file = open('Test_2.4.1_read_from_file_2.txt', 'r')

next_line = new_file.readline()
print(next_line)
# First line

next_line = new_file.readline()
print(next_line)
# Second line

next_line = new_file.readline()
print(next_line)


next_line = new_file.readline()
print(bool(next_line))


new_file.close()
