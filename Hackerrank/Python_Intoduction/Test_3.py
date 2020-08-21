def count_substring(string, sub_string):
    entry = 0
    while sub_string in string:
        entry += 1
        string = string[string.find(sub_string) + 1:]
    return entry


string = 'ABCDCDC'
sub_string = 'CDC'

print(count_substring(string, sub_string))
