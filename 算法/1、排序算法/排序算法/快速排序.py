# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 快速排序.py
# Time       ：2023/4/30 23:09
# Author     ：blue_moon
# version    ：python 3.7
# Description：
基本思路从数列中挑选一个元素作为基准
重新排序数组之后所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""


def QuickSort(lst):
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr, left, right)
        # 递归调用
        # print(arr)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n - 1)
    return lst


arr = [234, 354, 654, 5467, 867, 8679, 8967]
print(QuickSort(arr))

