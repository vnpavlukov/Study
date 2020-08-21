with open('in.txt') as inf:
    dna = inf.readline()


def decoding(data):
    decode, i = '', 0
    while i < len(data) - 1:
        letter = data[i]
        i += 1
        factor = data[i]
        if i < len(data) - 1:
            i += 1
        else:
            decode += letter * int(factor)
            return decode
        if data[i].isdigit():
            factor += data[i]
            decode += letter * int(factor)
            i += 1
        else:
            decode += letter * int(factor)
    return decode


print(decoding(dna))
