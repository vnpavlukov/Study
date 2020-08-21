name = input("Enter file:")

if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if 'From ' in line:
        sender = line.strip().split()
        time = sender[5][:2]
        counts[time] = counts.get(time, 0) + 1

for key in sorted(counts):
    print(key, counts[key])