import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\\"
    if re.search(pattern, line):
        print(line)
