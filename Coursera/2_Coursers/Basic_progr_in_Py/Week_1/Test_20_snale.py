height = int(input())
speed = int(input())
fall = int(input())
days = (height - fall - 1) // (speed - fall) + 1
print(days)
