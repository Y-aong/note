# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 责任链模式二.py
# Time       ：2023/4/30 17:07
# Author     ：blue_moon
# version    ：python 3.7
# Description：已经知道顺序，链的下方依次代表着处理问题的最大权限
"""
from abc import ABC, abstractmethod


class AskLeave(ABC):
    @abstractmethod
    def furlough(self, day):
        pass


class PL(AskLeave):

    def furlough(self, day):
        if day <= 1:
            print('准假')
        else:
            PM().furlough(day)


class PM(AskLeave):
    def furlough(self, day):
        if day <= 3:
            print('准假')
        else:
            Manger().furlough(day)


class Manger(AskLeave):
    def furlough(self, day):
        if day <= 10:
            print('准假')
        else:
            print('离职吧')
