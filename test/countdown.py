import multiprocessing
import threading
cnt = 100000000


def run():
    global cnt
    while cnt > 0:
        cnt -= 1


if __name__ == "__main__":

    run()

    # 多线程
    # t1 = threading.Thread(target=run)
    # t2 = threading.Thread(target=run)
    #
    # t1.start()
    # t2.start()

    # 多进程
    # p1 = multiprocessing.Process(target=run)
    # p2 = multiprocessing.Process(target=run)
    #
    # p1.start()
    # p2.start()

    pass
