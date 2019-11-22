import time

num_runs = 10


class time_this:
    def __init__(self, func, num_runs):
        self.num_runs = num_runs
        self.func = func

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        avg_time = 0
        b = time.time()
        avg_time += b - self.start_time
        print(avg_time / self.num_runs)


def f():
    for j in range(1000000):
        pass


with time_this(f, num_runs) as t:
    for i in range(num_runs):
        f()

