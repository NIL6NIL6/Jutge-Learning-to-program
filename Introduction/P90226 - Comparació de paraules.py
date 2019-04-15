#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    entrada = input().split()
    a = entrada[0]
    b = entrada[1]
    if (a == b):
        print(a, '=', b)
    elif (a < b):
        print(a, '<', b)
    else:
        print(a, '>', b)


main()
