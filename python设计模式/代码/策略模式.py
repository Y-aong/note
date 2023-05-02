# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 策略模式.py
# Time       ：2023/4/30 16:49
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context(object):
    """上下文"""

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    """策略接口"""

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    # 具体策略A
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    # 具体策略B
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
