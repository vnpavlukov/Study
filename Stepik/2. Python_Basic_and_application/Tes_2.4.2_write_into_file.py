f = open("Tes_2.4.2_write_into_file.txt", "w")

f.write("Hello\n")
f.write("World\n")
f.write(str(25) + '\n')


lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents)


f.close()
