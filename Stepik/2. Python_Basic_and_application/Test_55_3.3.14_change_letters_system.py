# https://stepik.org/lesson/24470/step/11?unit=6776
import re
from sys import stdin

for line in stdin:
    print(re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line.rstrip()))
