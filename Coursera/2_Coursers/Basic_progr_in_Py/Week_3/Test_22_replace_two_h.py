l = input()


def replace_center(s):
    first_h = s.find('h')
    reverse_s = s[::-1]
    last_h = len(s) - (reverse_s.find('h') + 1)
    start_string = s[0:first_h + 1]
    center_string = s[first_h + 1: last_h]
    big_h_center_string = center_string.replace('h', 'H')
    finish_string = s[last_h:]
    return start_string + big_h_center_string + finish_string


if l.count('h') < 3:
    print(l)
else:
    print(replace_center(l))
