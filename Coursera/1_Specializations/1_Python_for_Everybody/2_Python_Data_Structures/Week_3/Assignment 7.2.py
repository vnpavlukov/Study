fname = 'mbox-short.txt'
fh = open(fname)
count = 0
all_dspam = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        all_dspam += float(line.rstrip()[20:])

avg = all_dspam / count
print("Average spam confidence:", avg)
