from simplecrypt import decrypt

passwords_file = open("Test_2.2.9_passwords.txt")
all_passwords = passwords_file.read().splitlines()

with open("Test_2.2.9_encrypted.bin", "rb") as inp:
    encrypted = inp.read()

count_attempts = 0
for password in all_passwords:
    try:
        plaintext = decrypt(password, encrypted).decode('utf8')
        print(plaintext)
    except:
        count_attempts += 1
        print('Attempt №', count_attempts, 'with password', password,
              'is finish, let\'s try one more time')
        continue

passwords_file.close()
