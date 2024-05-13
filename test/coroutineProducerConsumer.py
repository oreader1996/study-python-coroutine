import time


def consumer():
    cnt = yield
    while True:
        if cnt <= 0:
            cnt = yield cnt

        print("i am consumer {}------".format(cnt))
        cnt -= 1
        time.sleep(1)


def producer(cnt):
    gen = consumer()
    next(gen)
    cnt = gen.send(cnt)
    while True:
        cnt += 1
        cnt = gen.send(cnt)
        print("i am producer {}".format(cnt))


if __name__ == "__main__":
    producer(4)
