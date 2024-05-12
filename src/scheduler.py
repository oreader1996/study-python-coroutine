from modules.downloader import Downloader
from modules.hasher import Hasher
from modules.storager import Storager
from src.settings import *
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from src.utils.common import timeit


class Scheduler:
    def __init__(self):
        self.tps = ThreadPoolExecutor(multi_count)
        self.pps = ProcessPoolExecutor(multi_count)

    @timeit
    def process(self):
        logging.debug("下载器开始工作")
        imgs = Downloader.from_scheduler(self, CalcType.MultiThread).process()

        logging.debug("哈希器开始工作")
        md5s = Hasher.from_scheduler(self, CalcType.MultiProcess).process(imgs)

        logging.debug("存储器使用开始工作")
        Storager.from_scheduler(self, CalcType.MultiThread).process(imgs, md5s)
        pass
