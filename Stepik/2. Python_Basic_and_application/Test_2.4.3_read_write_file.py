with open("Test_2.4.1_read_from_file_2.txt") as f, open(
        "Test_2.4.3_read_write_file.txt", "w") as w:
    for line in f:
        w.write(line)  # write lines in w file
