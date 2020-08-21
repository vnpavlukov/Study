from Test_17_get_formatted_name import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first_name = input("\nPlease give me a first name: ")
    if first_name == 'q':
        print('Good bye')
        break
    last_name = input("\nPlease give me a last name: ")
    if last_name == 'q':
        print('Good bye')
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print('\tNeatly formatted name: ' + formatted_name + '.')
