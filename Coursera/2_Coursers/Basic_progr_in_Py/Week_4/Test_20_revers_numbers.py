def rev_numbers():
    n = int(input())
    if n:
        rev_numbers()
    print(n)


rev_numbers()
