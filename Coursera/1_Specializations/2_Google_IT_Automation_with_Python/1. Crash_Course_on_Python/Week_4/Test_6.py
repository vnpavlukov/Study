def combine_guests(main_list, ap_list):
    for key, values in ap_list.items():
        if key not in main_list:
            main_list[key] = values
    return main_list


# Combine both dictionaries into one, with each key listed
# only once, and the value from guests1 taking precedence

Rorys_guests = {
    "Adam": 2, "Brenda": 3, "David": 1, "Jose": 3,
    "Charlotte": 2, "Terry": 1, "Robert": 4
}

Taylors_guests = {
    "David": 4, "Nancy": 1, "Robert": 2,
    "Adam": 1, "Samantha": 3, "Chris": 5
}

print(combine_guests(Rorys_guests, Taylors_guests))
