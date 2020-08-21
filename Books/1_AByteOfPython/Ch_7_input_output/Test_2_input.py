something = input('Введите текст: ')
low = something.lower()
no_space = low.replace(' ', '')


def reverse(text):  # make revers text
    return text[::-1]  # now any text is revers


def palindrome(text):  # compare our text with reverse
    return text == reverse(text)


if (palindrome(no_space)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")

print(no_space)
