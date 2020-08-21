box1_h = int(input())
box1_w = int(input())
box1_l = int(input())
box2_h = int(input())
box2_w = int(input())
box2_l = int(input())


# box1_h = 2
# box1_w = 2
# box1_l = 3
# box2_h = 3
# box2_w = 2
# box2_l = 1


def compare_boxes(box1h, box1w, box1l, box2h, box2w, box2l):
    sides_box1 = [box1h, box1w, box1l]
    sides_box2 = [box2h, box2w, box2l]

    sides_box1.sort()
    sides_box2.sort()

    if sides_box1 == sides_box2:
        return 'Boxes are equal'

    elif sides_box1[0] <= sides_box2[0] and \
            sides_box1[1] <= sides_box2[1] and \
            sides_box1[2] <= sides_box2[2]:
        return 'The first box is smaller than the second one'

    elif sides_box1[0] >= sides_box2[0] and \
            sides_box1[1] >= sides_box2[1] and \
            sides_box1[2] >= sides_box2[2]:
        return 'The first box is larger than the second one'

    else:
        return 'Boxes are incomparable'


print(compare_boxes(box1_h, box1_w, box1_l, box2_h, box2_w, box2_l))
