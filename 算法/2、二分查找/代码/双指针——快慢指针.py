# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 双指针——快慢指针.py
# Time       ：2023/5/5 22:29
# Author     ：blue_moon
# version    ：python 3.7
# Description：双指针
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。
示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
"""
from typing import List


# 前后指针
def search_target(arr: List[int], target: int):
    j = 0
    for i in range(len(arr)):
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1
    return j


# 快慢指针
def search_target1(arr: List[int], target: int):
    fast = 0
    slow = 0
    size = len(arr)
    while fast < size:
        if arr[fast] != target:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    return slow


print(search_target1([0, 1, 2, 2, 3, 0, 4, 2], 2))
