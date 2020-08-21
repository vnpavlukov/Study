something = input('Введите текст: ')


def reverse(text):  # new function revers
    return text[::-1]  # revers text


def palindrome(text):  # compare revers and original
    return text == reverse(text)


if palindrome(something):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
