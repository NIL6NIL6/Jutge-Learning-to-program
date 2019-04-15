#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    letter = input()
    if (letter.isupper()):
        print('majuscula')
    else:
        print('minuscula')
    if (letter.upper() == 'A' or
        letter.upper() == 'E' or
        letter.upper() == 'I' or
        letter.upper() == 'O' or
        letter.upper() == 'U'):
        print('vocal')
    else:
        print('consonant')

main()
