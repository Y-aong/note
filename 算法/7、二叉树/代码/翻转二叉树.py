# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 翻转二叉树.py
# Time       ：2023/5/5 21:31
# Author     ：blue_moon
# version    ：python 3.7
# Description：翻转二叉树
"""


# 前序遍历
def overturn(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    overturn(root.left)
    overturn(root.right)
    return root


# 后序遍历
def overturn1(root):
    if not root:
        return None
    overturn(root.left)
    overturn(root.right)
    root.left, root.right = root.right, root.left
    return root


# 迭代法
def overturn2(root):
    if not root:
        return None
    stack = list(root)
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


# 层序遍历
def overturn3(root):
    if not root:
        return None
    from collections import deque
    que = deque([root])
    while que:
        for _ in range(len(que)):
            node = que.popleft()

            node.left, node.right = node.right, node.left
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
    return root
