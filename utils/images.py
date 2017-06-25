# coding=utf-8
__author__ = 'zhaoyuntao'
from pyocr import pyocr
from PIL import Image
import _carnumber_detect


def ocr(path):
    import os
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    tools = pyocr.get_available_tools()[:]
    if len(tools) == 0:
        return None
    return tools[0].image_to_string(Image.open(path),lang='chi_sim')


def carnum_detect(path):
    return _carnumber_detect.detect_by_color(path)

if __name__ == "__main__":
    print ocr("/Users/zhaoyuntao/Desktop/1.png");