number = 23
running = True

while running:
    guess = int(input('Guess the number: '))

    if guess == number:
        print('Congratulation, you are guessed!')
        running = False
    elif guess < number:
        print('No, my number is higher, try again')
    else:
        print('My number a little less, try again')
else:
    print('While is over')
