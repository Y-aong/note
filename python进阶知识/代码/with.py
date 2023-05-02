# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : with.py
# Time       ：2023/4/30 20:57
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


class MyResource:
    def __enter__(self):
        print("begin connect resource")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print(f"exc_type=={exc_type}")
        print(f"exc_value=={exc_value}")
        print(f"tb=={tb}")
        print("close connection")

    def query(self):
        print("begin execute resource")


with MyResource() as resource:
    resource.query()

# 结果
# begin connect resource
# exc_type==<class 'ZeroDivisionError'>
# exc_value==division by zero
# tb==<traceback object at 0x018DEA80>
# close connection
