import os
import time
from concurrent.futures import ProcessPoolExecutor


def _task():
    for i in range(2):
        print("this is a task,i = {},pid = {}\n".format(i, os.getpid()))
        time.sleep(1)
    return time.time()


if __name__ == "__main__":
    pool = ProcessPoolExecutor(10)

    futures = []
    for i in range(20):
        future = pool.submit(_task)
        futures.append(future)

    for future in futures:
        print(future.result())
    pass