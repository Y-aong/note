# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 其他.py
# Time       ：2023/5/10 18:16
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


# 斐波那契数列
def fibo(n):
    result = list()
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        result.append(a)
    return result


print(fibo(5))


# 单例模式
class Single:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance
