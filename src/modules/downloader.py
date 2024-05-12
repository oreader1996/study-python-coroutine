from src.utils.common import download_request
from src.modules.base import BaseModule
from src.settings import *


def _task():
    print("dsadsda")
    pass


class Downloader(BaseModule):
    def __init__(self):
        super().__init__()
        # self.img_url = "https://www.loliapi.com/acg/pe/"

    def process_singlethread(self):
        imgs = []
        for i in range(download_count):
            logging.debug("开始请求第{}个链接".format(str(i + 1)))
            imgs.append(download_request(images[i]))
        return imgs

    def process_multithread(self):
        imgs = []
        futures = []
        for i in range(download_count):
            logging.debug("开始请求第{}个链接".format(str(i + 1)))
            future = self.tps.submit(download_request, images[i])
            futures.append(future)

        for future in futures:
            img = future.result()
            imgs.append(img)
        return imgs

    def process_multiprocess(self):
        imgs = []
        futures = []
        for i in range(download_count):
            logging.debug("开始请求第{}个链接".format(str(i + 1)))
            future = self.pps.submit(download_request, images[i])
            futures.append(future)

        for future in futures:
            img = future.result()
            imgs.append(img)
        return imgs

    def process_coroutine(self):
        pass
