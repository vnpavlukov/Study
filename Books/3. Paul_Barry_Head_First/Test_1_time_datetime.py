from datetime import datetime
import time
import random

odds = [x for x in range(1, 60, 2)]

for i in range(5):
    right_this_sec = datetime.today().second
    print(right_this_sec, end='')
    if right_this_sec in odds:
        print(' - this second seems a little odd.')
    else:
        print('- not an odd second')
    time.sleep(random.randint(1, 5))
