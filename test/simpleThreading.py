import threading
import time


class SimpleThreading:
    def __init__(self, size):
        self.queue = []
        self.pool = []
        for i in range(size):
            self.pool.append(threading.Thread(target=self.process))

    def process(self):
        while True:
            if len(self.queue) == 0:
                time.sleep(1)
                continue

            task = self.queue.pop()
            task()

    def submit(self):
        self.queue.append(self._task)

    def _task(self):
        time.sleep(1)
        print("当前时间{}和当前线程名{}".format(time.time(), threading.get_native_id()))

    def start(self):
        for th in self.pool:
            th.start()


if __name__ == "__main__":
    ths = SimpleThreading(10)
    for i in range(100):
        ths.submit()

    ths.start()
