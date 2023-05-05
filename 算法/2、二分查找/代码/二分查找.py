# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 二分查找.py
# Time       ：2023/5/5 22:09
# Author     ：blue_moon
# version    ：python 3.7
# Description：
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""
from typing import List


def search(arr: List[int], target):
    left = 0
    right = len(arr)

    while left < right:
        middle = left + (right - left) // 2
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle
        else:
            return middle
    return -1


print(search([1, 3, 5, 6, 7], 3))
