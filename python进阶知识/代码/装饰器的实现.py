# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 装饰器的实现.py
# Time       ：2023/4/30 19:18
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
import time


def time_use(func):
    def wrapper():
        start = time.time()
        res = func()
        end = time.time()
        print(f'执行用时::{end - start}')
        return res

    return wrapper


@time_use
def test():
    for i in range(100000000):
        pass

# test()



