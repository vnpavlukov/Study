current_users = ['Egor', 'Oksana', 'Alisa', 'Kate', 'Artyem', 'Petr']
new_users = ['Vova', 'KATE', 'admin', 'Sasha', 'Marina', 'Petr']

check_users = []
for check_name in current_users:
    check_users.append(check_name.lower())

for new_user in new_users:
    if new_user.lower() in check_users:
        print(new_user + ', please take another nickname')
    else:
        print(new_user + ', you can take this nickname')

print(101 / 496)
