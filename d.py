#! /usr/bin/python3

import pygame as P
import math as M
import random as R
import time as T

def init(size,color):
    P.display.init()
    P.font.init()
    S=P.display.set_mode(size)
    S.fill(color)
    P.display.flip()
    return S

def loop():
    looping=True
    while looping:
        for E in P.event.get():
            if E.type == P.KEYDOWN:
                if E.key == P.K_ESCAPE:
                    looping = False
    return

def least(A):
    if  A[0] <= A[1]:
        if A[0] <= A[2]:
            return 0
        else:
            return 2
    elif A[1] <= A[2]:
        return 1
    else:
        return 2

def contrast(RGB):
    print("RGB = ",RGB, least(RGB))
    Z=[0,0,0]
    C=[127,127,127]
    S=[ C[0]-RGB[0],C[1]-RGB[1],C[2]-RGB[2]]
    print("S   = ",S,least(S))
    L=[0,0,0]
    for k in range(3):
        if RGB[k] >= 127:
            L[k]=255-RGB[k]
        else:
            L[k]=RGB[k]
    ll=least(L)
    print("L   = ",L,ll)
    if RGB[ll] <= 127:
        w=255
    else:
        w=0
    t=(w-RGB[ll])/S[ll]
    print("t   =  ",t)
    for i in range(3):
        Z[i] = int(RGB[i] + t * S[i])
    return Z

def main():
    x,y = 100,100
    w,h = 200,200
    size = [400,400]
    white = [255,255,255]
    blue = [0,0,255]
    S = init(size,white)
    n = 5
    myfont=P.font.SysFont(None,350//n)
    KK=[R.randint(0,255),R.randint(0,255),R.randint(0,255)] 
    #KK = [1,2,8]
    P.draw.rect(S,KK,(x,y,w,h),0)
    kolor=contrast(KK)
    print("F   = ",kolor)
    label='733t'
    surf2=myfont.render(str(label),1,kolor)
    ss= myfont.size(str(label))
    S.blit(surf2,(x+(w-ss[0])/2,y+(h-ss[1])/2))
    P.display.flip()
    loop()

if __name__ == "__main__":
    main()

