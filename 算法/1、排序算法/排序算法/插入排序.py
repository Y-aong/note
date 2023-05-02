# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 插入排序.py
# Time       ：2023/4/30 22:57
# Author     ：blue_moon
# version    ：python 3.7
# Description：基本定义就是对于未排序的数据，在已排序的序列中从后到前进行扫描，找到相应位置并插入
有序区 arr[:sorted]; 无序区 arr[sorted:] (初始状态认为第0个元素为已排序的，sorted = 1)
取出无序区的第一个元素的值，temp = arr[sorted]
将该值从后向前依次与有序区元素arr[i]比较，若temp < arr[i]，则将arr[i]后移；否则，将temp的值插入在(i+1)位置处。
重复1-3直至整个数组排序完成。
"""


def select_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    # 总计需要遍历n -1次
    for i in range(1, length):
        j = i
        target = arr[i]  # #每次循环的一个待插入的数
        while j > 0 and target < arr[j - 1]:
            # 比较、后移，给target腾位置
            arr[j] = arr[j - 1]
            j -= 1
        # 把target插到空位
        arr[j] = target
    return arr


data = [12, 24, 64, 567, 567]
print(select_sort(data))
