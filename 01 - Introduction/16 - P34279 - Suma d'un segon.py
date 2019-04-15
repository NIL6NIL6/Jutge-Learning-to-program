#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    entrada = input().split()
    h = int(entrada[0])
    m = int(entrada[1])
    s = int(entrada[2])
    # formula to add a second
    s += 1
    if (s >= 60):
        s = 0
        m += 1
        if (m >= 60):
            m = 0
            h += 1
            if (h >= 24):
                h = 0
    # adding missing 0s to make a 6 digit long time
    h = str(h)
    m = str(m)
    s = str(s)
    if (len(h) < 2):
        h = "0" + h
    if (len(m) < 2):
        m = "0" + m
    if (len(s) < 2):
        s = "0" + s
    print(':'.join([h, m, s]))


main()
