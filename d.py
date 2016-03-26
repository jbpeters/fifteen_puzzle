#! /usr/bin/python3

import pygame as P
import math as M
import random as R
import time as T

def init(size,color):
    P.init()
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
        if RGB[k] > 127:
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
        if Z[i] < 0 :Z[i] = 0
        if Z[i] > 255 : Z[i] = 255 
    print("Z   = ",Z)
    print("============================")
    return Z

def main():  
    global myfont, S
    boxsize = w,h =  200,200
    S  = init(boxsize,[16,16,16])
    myfont = P.font.SysFont(None , 350//3 )
    _r = R.randint(0,255)
    _g = R.randint(0,255)
    _b = R.randint(0,255)
    #_r,_g,_b = 253,251,252
    kolor = [_r,_g,_b]
    border = 15,15
    Rect = ( border[0],border[1],boxsize[0]-2*border[0],boxsize[1]-2*border[1] )
    P.draw.rect(S,kolor,Rect)
    n = 'O'  
    n = str(n)
    tilesize = myfont.size(n)
    S2 = myfont.render(n,1,contrast(kolor))
    textbox = ((200-tilesize[0])/2,(200-tilesize[1])/2)   
    S.blit( S2 , textbox )
    P.display.flip()
    loop()            
    
if __name__ == "__main__":
    main()

