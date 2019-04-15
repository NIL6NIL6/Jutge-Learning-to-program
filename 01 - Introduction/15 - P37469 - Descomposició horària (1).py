#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    t = int(input())
    h = t // 3600
    m = t // 60 % 60
    s = t % 3600 % 60
    print(h, m, s)


main()
