import multiprocessing
import time

cnt = 0


def consumer():
    global cnt
    while True:
        if cnt <= 0:
            # print("cnt = {}".format(cnt))
            continue

        print("i am consumer,cnt = {}".format(cnt))
        cnt -= 1
        time.sleep(1)


def producer():
    global cnt
    while True:
        print("i am producer,cnt = {}".format(cnt))
        cnt += 1
        time.sleep(1)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=consumer)
    p2 = multiprocessing.Process(target=producer)

    p1.start()
    p2.start()
