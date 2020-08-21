runs_per_day = int(input())
goal_per_day = int(input())


def count_days(run_per_day, goal):
    current_day = 1
    while goal > run_per_day:
        run_per_day *= 1.1
        current_day += 1
    return current_day


print(count_days(runs_per_day, goal_per_day))
