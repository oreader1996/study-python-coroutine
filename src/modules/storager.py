from src.modules.base import BaseModule
from src.utils.common import save_path
from PIL import Image
import logging
from src.utils.common import storager_save


class Storager(BaseModule):
    def __init__(self):
        super().__init__()
        self.items = None

    def process(self, imgs, md5s):
        self._set_items(imgs, md5s)
        return super().process()

    def process_singlethread(self):
        for i, item in enumerate(self.items):
            logging.debug("开始存储第{}个链接".format(str(i + 1)))
            storager_save(item)

    def process_multithread(self):
        futures = []
        results = []
        for i, item in enumerate(self.items):
            logging.debug("开始存储第{}个链接".format(str(i + 1)))
            future = self.tps.submit(storager_save, item)
            futures.append(future)

        for future in futures:
            result = future.result()
            results.append(result)
        return results

    def process_multiprocess(self):
        futures = []
        for i, item in enumerate(self.items):
            logging.debug("开始存储第{}个链接".format(str(i + 1)))
            future = self.pps.submit(storager_save, item)
            futures.append(future)

        for future in futures:
            future.result()

    def process_coroutine(self):
        pass

    def _set_items(self, imgs, md5s):
        self.items = []
        for img, md5 in zip(imgs, md5s):
            item = (img, save_path(md5))
            self.items.append(item)
