from concurrent.futures import ThreadPoolExecutor
import time
import threading


def _task():
    time.sleep(1)
    print("当前时间{}和当前线程名{}".format(time.time(), threading.get_native_id()))


if __name__ == "__main__":
    futures = []
    tps = ThreadPoolExecutor(10)
    for i in range(20):
        future = tps.submit(_task)
        futures.append(future)

    for future in futures:
        future.result()
