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


def main():
    entrada = readNumbers(2)
    result = max(entrada)
    print(result)


main()
