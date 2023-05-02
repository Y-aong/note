# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : python多线程.py
# Time       ：2023/4/30 20:04
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
import threading


# 基于方法

def demo():
    for i in range(10):
        print(i)


t1 = threading.Thread(target=demo)
t1.start()


# 基于类

class Demo(threading.Thread):
    def __init__(self):
        super(Demo, self).__init__()

    def run(self) -> None:
        demo()
