# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 策略模式简化.py
# Time       ：2023/4/30 16:54
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


def handle_week():
    print('处理一周数据')


def handle_day():
    print('处理一天数据')


def handle_month():
    print('处理一月数据')


handlers = {
    'week': handle_week,
    'day': handle_day,
    'month': handle_month
}
