#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    year = int(input())
    if ((((year % 4) == 0) and
         ((year % 100) != 0)) or
        (((year % 100) == 0) and
         (((year // 100) % 4) == 0))):
        print('YES')
    else:
        print('NO')


main()
