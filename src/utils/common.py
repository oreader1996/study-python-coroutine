from PIL import ImageFile
import numpy as np
from functools import wraps
import time
from requests import request
from src.settings import *
import hashlib
from scipy import signal
from PIL import Image


def bytes_to_np(img):
    parser = ImageFile.Parser()
    parser.feed(img)
    img = parser.close()
    return np.array(img)


def download_request(url):
    r = request("GET", url)
    if r.status_code == 200:
        return bytes_to_np(r.content)
    return None


def hasher_get_md5(img):
    cov = [[[0.1], [0.05], [0.1]]]
    img = signal.convolve(img, cov)
    img = Image.fromarray(img.astype('uint8')).convert('RGB')
    return hashlib.md5(str(img).encode("utf-8")).hexdigest()


def storager_save(item):
    content, path = item
    Image.fromarray(content.astype('uint8')).convert("RGB").save(path)
    return True


def timeit(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()

        run_time = end_time - start_time
        logging.info(f"{type(self).__name__}类中{func.__name__} 函数的运行时差为 {run_time:.4f}秒")
        return result

    return wrapper


def save_path(md5):
    filename = "{}.jpg".format(md5)

    # 检测路径是否存在，不存在则创建
    if not os.path.exists(storage_path):
        try:
            os.makedirs(storage_path)
        except OSError as e:
            logging.error("创建路径{}失败".format(storage_path))
            return

    return os.path.join(storage_path, filename)


if __name__ == "__main__":
    pass
