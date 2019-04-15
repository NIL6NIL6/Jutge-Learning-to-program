#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def readWords(maxWords):
    result = []
    currWords = 0
    # read lines
    for line in sys.stdin:
        # ignore spaces & tabs
        for x in line.split():
            result.append(x)
            currWords += 1
            if (currWords == maxWords):
                return result


def old():
    a = input().split(' ')
    print(a[2],a[1],a[0])


def main():
    result = readWords(3)
    result.reverse()
    print(' '.join(result))


main()
#old()
