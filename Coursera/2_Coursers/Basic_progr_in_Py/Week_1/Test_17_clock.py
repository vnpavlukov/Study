inp_sec = int(input())
hour = inp_sec // 3600 % 24
min = inp_sec // 60 % 60
sec = inp_sec % 60
print(hour, ':', "%02d" % min, ':', "%02d" % sec, sep='')
