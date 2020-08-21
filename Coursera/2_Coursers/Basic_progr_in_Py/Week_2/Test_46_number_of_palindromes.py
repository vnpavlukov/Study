input_number = int(input())


def count_palindromes(limit):
    number = 0
    count = 0
    while number < limit:
        number += 1
        string = str(number)
        revered_string = string[::-1]
        if string == revered_string:
            count += 1
    return count


print(count_palindromes(input_number))
