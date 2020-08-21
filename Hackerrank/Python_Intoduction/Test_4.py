def subject(string):
    alphanumeric = False
    for l in string:
        if l.isalnum():
            alphanumeric = True
    print(alphanumeric)

    alphabetical = False
    for l in string:
        if l.isalpha():
            alphabetical = True
    print(alphabetical)

    digits = False
    for l in string:
        if l.isdigit():
            digits = True
    print(digits)

    lowercase = False
    for l in string:
        if l.islower():
            lowercase = True
    print(lowercase)

    uppercase = False
    for l in string:
        if l.isupper():
            uppercase = True
    print(uppercase)


if __name__ == '__main__':
    s = input()
    subject(s)
