import functools
import time


def timer(func):
    """to show make function time"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        delta_time = end_time - start_time
        print(f'func runtime is: {delta_time:.4f} sec')
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(999)
