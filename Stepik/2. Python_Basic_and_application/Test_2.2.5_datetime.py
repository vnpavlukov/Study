import datetime as dt

y, m, d = map(int, input().split())
delta_days = int(input())
new_date = dt.date(y, m, d) + dt.timedelta(days=delta_days)
print(new_date.year, new_date.month, new_date.day)
