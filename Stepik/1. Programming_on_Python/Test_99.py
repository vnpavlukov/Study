from memory_profiler import memory_usage


def new_func():
    return ((11 + (15)) ** 100) ** 100

print(new_func())

print(memory_usage())