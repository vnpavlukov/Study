import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"aa+"
    new = 'argh'
    print(re.sub(pattern, new, line, re.IGNORECASE))
