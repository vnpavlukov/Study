brick_1 = int(input())
brick_2 = int(input())
brick_3 = int(input())
hole_1 = int(input())
hole_2 = int(input())


def check_hole(brick1, brick2, brick3, hole1, hole2):
    sides_brick = [brick1, brick2, brick3]
    sides_brick.sort()

    if hole1 > hole2:
        hole1, hole2 = hole2, hole1

    if sides_brick[0] <= hole1 and sides_brick[1] <= hole2:
        return 'YES'
    else:
        return 'NO'


print(check_hole(brick_1, brick_2, brick_3, hole_1, hole_2))
