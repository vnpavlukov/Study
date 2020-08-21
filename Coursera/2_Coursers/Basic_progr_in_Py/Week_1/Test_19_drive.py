rides_a_day = int(input())
route = int(input())
need_days = (route + rides_a_day - 1 ) // rides_a_day
print(need_days)

