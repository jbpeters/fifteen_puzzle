#! /usr/bin/python3

import random as R
import pygame as P

P.display.init()
S=P.display.set_mode((1,1))


l = [55,77,215]
grid = 3
looping = True
while looping:
    for E in P.event.get():
        if E.type == P.KEYDOWN:
            if E.key == P.K_ESCAPE:
                looping=False
    rand = [l[R.randint(0,grid-1)],l[R.randint(0,grid-1)],l[R.randint(0,grid-1)]]
    print(rand)
