# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 斐波那契数列.py
# Time       ：2023/4/30 19:48
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


def fibonacci(n):
    i, j = 0, 1
    fibonacci_list = list()
    while i < n:
        fibonacci_list.append(i)
        i, j = j, i + j
    return fibonacci_list


print(fibonacci(10))

