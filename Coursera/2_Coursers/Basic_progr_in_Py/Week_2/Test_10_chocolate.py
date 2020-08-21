chocolate_h = int(input())
chocolate_w = int(input())
chunk = int(input())


def check_chunk(chocolate_h, chocolate_w, chunk):
    if chunk < chocolate_h * chocolate_w:
        if chunk % chocolate_h == 0 or chunk % chocolate_w == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


check_chunk(chocolate_h, chocolate_w, chunk)
