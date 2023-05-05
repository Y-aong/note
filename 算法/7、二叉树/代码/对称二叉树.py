# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 对称二叉树.py
# Time       ：2023/5/5 21:50
# Author     ：blue_moon
# version    ：python 3.7
# Description：判断二叉树是否对称
"""


def check(left, right):
    if not left and not right:
        return True
    if not left and right:
        return False
    if left and not right:
        return False
    if left.val != right.val:
        return False

    outside = check(left.left, right.right)
    inside = check(left.right, right.left)
    return all([outside, inside])


def compare(root):
    if not root:
        return True
    return check(root.left, root.right)



