x, y = 0, 0

input_count = int(input())

for i in range(input_count):
    coords = input().split()
    if coords[0] == 'север':
        y += int(coords[1])
    elif coords[0] == 'юг':
        y -= int(coords[1])
    elif coords[0] == 'восток':
        x += int(coords[1])
    elif coords[0] == 'запад':
        x -= int(coords[1])
    coords.clear()

print(x, y)
