# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 二叉树的最大深度.py
# Time       ：2023/5/5 21:56
# Author     ：blue_moon
# version    ：python 3.7
# Description：获取二叉树的最大深度
"""
from collections import deque


def get_max_depth(root):
    def get_depth(node) -> int:
        if not node:
            return 0

        left_depth = get_depth(node.left)
        right_depth = get_depth(node.right)
        return max(left_depth, right_depth) + 1

    return get_depth(root)


def get_max_depth1(root):
    # 层序遍历
    stack = deque()
    stack.append(root)
    depth = 0
    while stack:
        size = len(stack)
        depth += 1
        for _ in range(size):
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return depth
