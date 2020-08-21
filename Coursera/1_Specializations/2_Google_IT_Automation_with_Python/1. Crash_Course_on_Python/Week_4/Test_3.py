def combine_lists(list1, list2):
    return list1 + list2[::-1]


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
new_list = combine_lists(Jamies_list, Drews_list)

print(Jamies_list)
print(Drews_list)
print(new_list)
print()


def combine_lists(list1, list2):
    new_list = list()
    for i in list2:
        new_list.append(i)
    for i in list1[::-1]:
        new_list.append(i)
    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
new_list = combine_lists(Jamies_list, Drews_list)

print(Jamies_list)
print(Drews_list)
print(new_list)
