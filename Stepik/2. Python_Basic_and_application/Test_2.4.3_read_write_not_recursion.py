with open("Test_2.4.3_read_write_not_recursion_read.txt") as f, open(
        "Test_2.4.3_read_write_not_recursion_write.txt", "w") as w:
    all_text = f.read().splitlines()
    contents = "\n".join(reversed(all_text))
    w.write(contents)

    #  w.writelines(f.readlines()[::-1])

# lines = open("input.txt").readlines()
# with open("output.txt", "w") as out:
#     out.writelines(reversed(lines))

#  print(*reversed(open("sample.txt").readlines()), sep="")

# with open("123.txt") as f, open("123_copy.txt", "w") as f2:
#   for line in reversed(list(f)):
#     f2.write(line)

# with open("input.txt", 'r') as f, open("out.txt", 'w') as w:
#     w.writelines(reversed(f.readlines()))

# with open('1.txt') as f, open('2.txt','w') as w:
#     w.write('\n'.join(f.read().splitlines()[::-1]))