"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
 завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
 полученной ранее сумме и после этого завершить программу."""

string_of_numbers = '1 2 3 4'


def sum_of_numbers():
    answer = 0
    while True:
        list_of_symbols = input('Enter values separated by spaces:').split()
        for number in list_of_symbols:
            try:
                answer += int(number)
            except ValueError:
                return answer
        print(answer)


print(sum_of_numbers())
