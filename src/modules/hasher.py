from src.modules.base import BaseModule
from src.utils.common import hasher_get_md5

from src.settings import *


class Hasher(BaseModule):
    def __init__(self):
        super().__init__()
        self.imgs = None

    def process(self, imgs):
        self._set_imgs(imgs)
        return super().process()

    def process_singlethread(self):
        md5s = []
        for i, img in enumerate(self.imgs):
            logging.debug("开始哈希第{}个链接".format(str(i + 1)))
            md5 = hasher_get_md5(img)
            md5s.append(md5)
        return md5s

    def process_multithread(self):
        md5s = []
        futures = []
        for i, img in enumerate(self.imgs):
            logging.debug("开始哈希第{}个链接".format(str(i + 1)))
            future = self.tps.submit(hasher_get_md5, img)
            futures.append(future)

        for future in futures:
            md5 = future.result()
            md5s.append(md5)

        return md5s

    def process_multiprocess(self):
        md5s = []
        futures = []
        for i, img in enumerate(self.imgs):
            logging.debug("开始哈希第{}个链接".format(str(i + 1)))
            future = self.pps.submit(hasher_get_md5, img)
            futures.append(future)

        for future in futures:
            md5 = future.result()
            md5s.append(md5)

        return md5s

    def process_coroutine(self):
        pass

    def _set_imgs(self, imgs):
        self.imgs = imgs
