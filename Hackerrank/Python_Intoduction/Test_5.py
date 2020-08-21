# ljust center rjust
thickness = 5
c = 'H'

for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(
        thickness * 6))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(
        thickness * 6))

for i in range(thickness):
    print(((c * (thickness - i - 1)).center(thickness) + c + (
                c * (thickness - i - 1)).center(thickness)).ljust(thickness * 6))
