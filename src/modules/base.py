from abc import ABC, abstractmethod
from src.settings import *
import logging

from src.utils.common import timeit


class BaseModule(ABC):
    def __init__(self):
        self.calc_type = None
        self.calc_types = {
            CalcType.SingleThread: self.process_singlethread,
            CalcType.MultiThread: self.process_multithread,
            CalcType.MultiProcess: self.process_multiprocess,
            CalcType.Coroutine: self.process_coroutine
        }

    @classmethod
    def from_scheduler(cls, scheduler, calc_type=None):
        obj = cls()

        obj.calc_type = default_calc_type if calc_type is None else calc_type
        obj.tps = scheduler.tps
        obj.pps = scheduler.pps

        return obj

    @timeit
    def process(self, *args):
        if self.calc_type is not None:
            handler = self.calc_types[self.calc_type]
            logging.debug(f"{type(self).__name__}的{default_calc_type.name}类型模块启动")
            return handler()
        else:
            logging.error("未知类型模块")

    @abstractmethod
    def process_singlethread(self):
        pass

    @abstractmethod
    def process_multithread(self):
        pass

    @abstractmethod
    def process_multiprocess(self):
        pass

    @abstractmethod
    def process_coroutine(self):
        pass
