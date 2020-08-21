cow = int(input())


def how_many_cows(cow):
    if (cow <= 19) and (cow >= 11):
        word = "korov"
    else:
        if (cow % 10) == 1:
            word = "korova"
        elif cow % 10 in (2, 3, 4):
            word = "korovy"
        else:
            word = "korov"
    print(cow, word)


how_many_cows(cow)
