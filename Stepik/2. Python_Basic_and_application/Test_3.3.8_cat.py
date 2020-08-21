import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"cat.*cat"
    if re.findall(pattern, line):
        print(line)
