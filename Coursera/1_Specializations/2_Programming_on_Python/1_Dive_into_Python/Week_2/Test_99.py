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

