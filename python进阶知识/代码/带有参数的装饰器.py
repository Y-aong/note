# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 带有参数的装饰器.py
# Time       ：2023/4/30 19:23
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
import time
from functools import wraps


def retry(count=3, sleep=1):
    def wrapper(func):
        @wraps
        def inner(*args, **kwargs):
            res = None
            for i in range(count):
                try:
                    res = func(*args, **kwargs)
                except Exception as e:
                    print(f'函数执行出错::{e}')
                    time.sleep(sleep)
                    continue
            return res

        return inner

    return wrapper
