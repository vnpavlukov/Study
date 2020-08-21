def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """

    if bool1:
        if bool2:
            return False
        else:
            return True
    else:
        return True


b_1 = True
b_2 = False

print(nand(b_1, b_2), ':')
print('1', not (b_1 or b_2))
# print('2', not (b_1 and b_2))
# print('3', b_1 and b_2)
# print('4', b_1 or b_2)
