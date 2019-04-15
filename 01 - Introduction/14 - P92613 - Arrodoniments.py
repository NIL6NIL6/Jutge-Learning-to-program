#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def main():
    x = float(input())
    fl = math.floor(x)
    cl = math.ceil(x)
    if ((cl - x) <= (x - fl)):
        rd = cl
    else:
        rd = fl
    print(fl, cl, rd)


main()
