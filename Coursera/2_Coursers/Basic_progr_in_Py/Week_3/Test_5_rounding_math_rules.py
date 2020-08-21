number = float(input())
fraction = (number * 10) % 10
if fraction == 5:
    number += 0.1

print(round(number))
