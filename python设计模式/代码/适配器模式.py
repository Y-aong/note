# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 适配器模式.py
# Time       ：2023/4/30 17:20
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""


class Target:

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
