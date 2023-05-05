# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 二叉树遍历.py
# Time       ：2023/5/5 21:00
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 二叉树的递归遍历

def pre_order1(root: Tree):
    """
    前序遍历 中左右
    """
    result = list()
    if not root:
        return None

    def order(node):
        result.append(node.val)
        if node.left:
            order(node.left)
        if node.right:
            order(node.right)

    order(root)
    return result


def in_order1(root: Tree):
    """
    中序左中右
    """
    result = list()
    if not root:
        return None

    def order(node):
        if node.left:
            order(node.left)
        result.append(node.val)
        if node.right:
            order(node.right)

    order(root)
    return result


def pre_order2(root: Tree):
    """迭代方法使用栈来复制"""
    stack = list()
    stack.append(root)
    result = list()

    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            stack.append(node)
            stack.append(None)
        else:
            node = stack.pop()
            result.append(node.val)
    return result


def lever_order(root: Tree):
    results = list()
    if not root:
        return results
    from collections import deque
    que = deque([root])

    while que:
        size = len(que)
        result = list()
        for _ in range(len(size)):
            cur = que.popleft()
            result.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        results.append(result)
    return results


def level_order(root):
    result = list()
    if not root:
        return result

    def order(node, depth):
        if len(result) == depth:
            result.append([])
        result[depth].append(node.val)
        if node.left:
            order(node.left, depth + 1)
        if node.right:
            order(node.right, depth + 1)

    order(root, 0)
    return result
