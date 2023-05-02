# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 使用装饰器实现缓存.py
# Time       ：2023/4/30 19:31
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
from inspect import signature


def fifo_cache(maxsize=128):
    cache = dict()
    cache_list = list()

    def wrapper(func):
        sig = signature(func)

        def inner(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            key = bound_values.__str__()
            value = cache.get(key)
            if value:
                print('命中缓存')
                return value
            if len(cache_list) >= maxsize:
                old_key = cache_list.pop()
                if old_key in cache: cache.pop(old_key)

            result = func(*args, **kwargs)
            cache_list.append(key)
            cache.setdefault(key, result)
            return result

        return inner

    return wrapper


@fifo_cache()
def test1(x, y):
    return x + y


@fifo_cache()
def test2(x, y, z=20):
    return x + y + z


@fifo_cache()
def test3(*args, **kwargs):
    return 5


print(test1(19, 20))

print(test2(19, 20, 20))
print(test2(19, 20))  # 不会命中缓存

print(test3(4, 2, x=6, y=9))
print(test1(19, 20))
