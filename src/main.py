from scheduler import Scheduler
from settings import *

if __name__ == '__main__':
    logging.basicConfig(level=logging_level, format=logging_format)

    logging.info("调度器开始工作")
    Scheduler().process()
