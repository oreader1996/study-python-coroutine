import multiprocessing
import os
import time


def consumer(queue):
    while True:
        cnt = queue.get()
        if cnt is None:
            continue

        print("i am a consumer ,my cnt is {},my pid = {}".format(cnt, os.getpid()))
        time.sleep(1)


def producer(queue):
    cnt = 0

    while True:
        queue.put(cnt)
        print("i am a producer ,my cnt is {},my pid = {}".format(cnt, os.getpid()))
        cnt += 1
        time.sleep(1)


if __name__ == "__main__":
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()
