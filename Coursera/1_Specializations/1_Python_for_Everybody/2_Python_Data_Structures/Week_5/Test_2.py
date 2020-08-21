name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
count_senders = dict()
for line in handle:
    if 'From ' in line:
        sender = line.strip().split()[1]
        count_senders[sender] = count_senders.get(sender, 0) + 1


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


max_key = keywithmaxval(count_senders)
print(max_key, count_senders[max_key])