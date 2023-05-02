# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 冒泡算法.py
# Time       ：2023/4/30 22:46
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
from typing import List


def bubble_sort(arr: List[int]):
    # 总计需要遍历n-1次
    for i in range(len(arr) - 1):
        # 已经排序过的数字不再需要排序
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


data = [123, 234, 46, 65, 8567, 5678]
print(bubble_sort(data))
