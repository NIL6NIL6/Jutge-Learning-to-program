#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    entrada = input().split()
    eur = int(entrada[0])
    cent = int(entrada[1])
    
    eur500 = eur // 500
    eur = eur % 500
    print('Bitllets de 500 euros:', eur500)
    eur200 = eur // 200
    eur = eur % 200
    print('Bitllets de 200 euros:', eur200)
    eur100 = eur // 100
    eur = eur % 100
    print('Bitllets de 100 euros:', eur100)
    eur50 = eur // 50
    eur = eur % 50
    print('Bitllets de 50 euros:', eur50)
    eur20 = eur // 20
    eur = eur % 20
    print('Bitllets de 20 euros:', eur20)
    eur10 = eur // 10
    eur = eur % 10
    print('Bitllets de 10 euros:', eur10)
    eur5 = eur // 5
    eur = eur % 5
    print('Bitllets de 5 euros:', eur5)
    eur2 = eur // 2
    eur = eur % 2
    print('Monedes de 2 euros:', eur2)
    print('Monedes de 1 euro:', eur)

    cent50 = cent // 50
    cent = cent % 50
    print('Monedes de 50 centims:', cent50)
    cent20 = cent // 20
    cent = cent % 20
    print('Monedes de 20 centims:', cent20)
    cent10 = cent // 10
    cent = cent % 10
    print('Monedes de 10 centims:', cent10)
    cent5 = cent // 5
    cent = cent % 5
    print('Monedes de 5 centims:', cent5)
    cent2 = cent // 2
    cent = cent % 2
    print('Monedes de 2 centims:', cent2)
    print('Monedes de 1 centim:', cent)


main()
