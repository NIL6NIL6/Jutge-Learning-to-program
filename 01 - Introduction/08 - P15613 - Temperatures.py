#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def hot():
    print('fa calor')


def boil():
    print("fa calor\nl'aigua bulliria")


def cold():
    print('fa fred')


def freeze():
    print("fa fred\nl'aigua es gelaria")


def ok():
    print("s'esta be")


def main():
    temp = int(input())
    if (temp <= 0):
        freeze()
    elif (temp < 10):
        cold()
    elif (temp >= 100):
        boil()
    elif (temp > 30):
        hot()
    else:
        ok()


main()
