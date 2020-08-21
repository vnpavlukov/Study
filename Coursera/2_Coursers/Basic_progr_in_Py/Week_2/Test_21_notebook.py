storageH = 100
storageW = 200
storageL = 300
boxH = 1
boxW = 2
boxL = 3

storage_size = [storageH, storageW, storageL]


def count_capacity(storage_sizes, box_h, box_w, box_l):
    count_h = storage_sizes[0] // box_h
    count_w = storage_sizes[1] // box_w
    count_l = storage_sizes[2] // box_l

    return count_h * count_w * count_l


capacity_1 = count_capacity(storage_size, boxH, boxW, boxL)
capacity_2 = count_capacity(storage_size, boxL, boxH, boxW)
capacity_3 = count_capacity(storage_size, boxW, boxL, boxH)
capacity_4 = count_capacity(storage_size, boxH, boxL, boxW)
capacity_5 = count_capacity(storage_size, boxL, boxW, boxH)
capacity_6 = count_capacity(storage_size, boxW, boxH, boxL)

print(max(capacity_1, capacity_2, capacity_3, capacity_4, capacity_5, capacity_6))

# print(storageH, storageW, storageL, boxH, boxW, boxL)
# print(check_height_capacity(storageH, storageW, storageL, boxH, boxW, boxL))
# print()
#
# for i in possible_options[0]: print(i, end=' ')
# print([for i in possible_options[0]: print(i, end=' '))
# # print(possible_options[0])
# #
# check_height_capacity(
# for i in possible_options[0]: print(i))


# check_height_capacity(possible_options[0])

# for capacity in possible_options:
#     print(capacity)
