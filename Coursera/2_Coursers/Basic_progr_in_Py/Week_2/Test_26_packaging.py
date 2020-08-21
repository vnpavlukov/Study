# box1_l = int(input())
# box1_w = int(input())
# box1_h = int(input())
#
# box2_l = int(input())
# box2_w = int(input())
# box2_h = int(input())
#
# cont_l = int(input())
# cont_w = int(input())
# cont_h = int(input())

box1_l = int(input())
box1_w = int(input())
box1_h = int(input())

box2_l = int(input())
box2_w = int(input())
box2_h = int(input())

cont_l = int(input())
cont_w = int(input())
cont_h = int(input())


def oriented(l, w, h): return [min(l, w, ), max(l, w), h]


box1 = oriented(box1_l, box1_w, box1_h)
box2 = oriented(box2_l, box2_w, box2_h)
cont = oriented(cont_l, cont_w, cont_h)


def check_ground_capacity(box1, box2, cont):
    return ((cont[0] >= box1[0] + box2[0] and box1[1] <= cont[1] >= box2[1]) or
            (cont[1] >= box1[1] + box2[1] and box1[0] <= cont[0] >= box2[0]) or
            (cont[1] >= box1[0] + box2[0] and box1[1] <= cont[0] >= box2[
                0])) and box1[2] <= cont[2] >= box2[2]


def check_height_capacity(box1, box2, cont):
    return (box1[0] <= cont[0] >= box2[0] and
            box1[1] <= cont[1] >= box2[1]) and cont[2] >= box1[2] + box2[2]


check_1 = check_ground_capacity(box1, box2, cont)
check_2 = check_height_capacity(box1, box2, cont)

if check_1 or check_2:
    print("YES")
else:
    print("NO")
