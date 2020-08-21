import math

Pan_capacity = int(input())
Time = int(input())
Chunks = int(input())


def how_much_cutlet(pan_capacity, time, chunks):
    if pan_capacity > chunks:
        return time * 2
    else:
        return math.ceil(chunks * 2 / pan_capacity) * time


print(how_much_cutlet(Pan_capacity, Time, Chunks))
