# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 选择排序.py
# Time       ：2023/4/30 22:49
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


def select_sort(arr):
    length = len(arr)
    # 总计需要遍历的次数为n - 1
    for i in range(length - 1):
        # 先假设第i个数字为最小值
        min_index = i
        # 第二次变量这里需要先排除掉已经变量完成的数据，然后在未排序的数组中找到最小值
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        # 这里每次遍历完成找到了最小值就交换顺序
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


data = [23, 234, 3546, 567, 3542, 8]
print(select_sort(data))
