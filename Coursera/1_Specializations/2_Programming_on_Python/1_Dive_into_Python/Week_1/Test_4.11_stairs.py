import sys

stairs = int(sys.argv[1])
i = 0
while stairs:
    print(' ' * (stairs - 1) + '#' * (i + 1))
    i += 1
    stairs -= 1
