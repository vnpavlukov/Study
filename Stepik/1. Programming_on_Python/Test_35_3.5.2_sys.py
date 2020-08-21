import sys

data = sys.argv

for i in data:
    print(i)


l = len(sys.argv)
for i in range(1, l):
    print(sys.argv[i])