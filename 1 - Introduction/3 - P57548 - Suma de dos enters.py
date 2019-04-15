#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def readNumbers(maxnums):
    result = []
    currnums = 0
    # llegeix linies
    for line in sys.stdin:
        # ignora espais
        for x in line.split():
            x = int(x)
            result.append(x)
            currnums += 1
            if (currnums == maxnums):
                return result


def old():
    a = input().split(' ')
    if (len(a) > 1):
        print(int(a[0]) + int(a[1]))
    else:
        b = input().split(' ')
        print(int(a[0]) + int(b[0]))


def main():
    entrada = readNumbers(2)
    result = sum(entrada)
    print(result)


main()
#old()
