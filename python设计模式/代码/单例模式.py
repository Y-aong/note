# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 单例模式.py
# Time       ：2023/4/30 16:02
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
import threading


class SimpleSingle:
    """简单模式"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


class Singleton:
    """
    线程安全模式
    """
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "__instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "__instance"):
                    Singleton._instance_lock = object.__new__(cls)
        return Singleton._instance_lock
