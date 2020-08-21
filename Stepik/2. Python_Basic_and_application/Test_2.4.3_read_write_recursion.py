def write_to_file():
    first_line = f.readline()
    second_line = f.readline()
    if bool(second_line) == False:
        return w.write(first_line)
    return write_to_file()


with open("Test_2.4.3_read_write_recursion_read.txt") as f, open(
        "Test_2.4.3_read_write_recursion_write.txt", "w") as w:
    write_to_file()