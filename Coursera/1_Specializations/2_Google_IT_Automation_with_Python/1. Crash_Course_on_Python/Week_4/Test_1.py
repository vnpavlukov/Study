def format_address(address_string):
    street = []
    words = address_string.split()
    for word in words:
        if word.isdigit():
            house = word
        else:
            street.append(word)
    return "house number {} on street named {}".format(house, ' '.join(street))


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
