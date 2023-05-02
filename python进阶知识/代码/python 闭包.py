# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : python 闭包.py
# Time       ：2023/4/30 19:13
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


def outer(a):
    b = 10

    def inner():
        print(a + b)
        return a + b

    return inner


demo = outer(5)
print(demo())
