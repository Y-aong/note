# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 线程锁.py
# Time       ：2023/4/30 20:10
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
import threading

num = 1


def add():
    lock.acquire()
    global num
    for i in range(10_000_000):
        num += 1
    lock.release()


def sub():
    lock.acquire()
    global num
    for i in range(10_000_000):
        num -= 1
    lock.release()


if __name__ == "__main__":
    lock = threading.Lock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)
