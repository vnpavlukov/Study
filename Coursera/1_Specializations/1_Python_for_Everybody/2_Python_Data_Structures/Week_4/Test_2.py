fname = ''
# count = 0
# if len(fname) < 1: fname = "mbox-short.txt"
#
# with open(fname) as file:
#     for line in file:
#         if 'From ' in line:
#             print(line.strip().split()[1])
#             count += 1
#
# print("There were", count, "lines in the file with From as the first word")


if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if 'From ' in line:
        print(line.strip().split()[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
