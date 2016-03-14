#! /usr/bin/python3

import pygame as P
import random as R
import  time  as T


def init(size,kolor):
    P.display.init()
    S=P.display.set_mode(size,1)
    S.fill(kolor)
    P.display.flip()
    return S

def loop():
    looping = True
    while looping:
        for E in P.event.get():
            if E.type == P.KEYDOWN:
                if E.key == P.K_ESCAPE:
                    looping = False
    P.display.quit()

box = w,h = 300,300
red = [255,0,0]
white = [255,255,255]
blue = [0,0,255]
S=init(box,white)
grid =8 
W,H = w/grid, h/grid
#  position is x,y -> col,row  


# place tile  in random location 
for count in range(60):
    start= col0,row0 = R.randint(0,grid-1),R.randint(0,grid-1)
    end  = col1,row1 = R.randint(0,grid-1),R.randint(0,grid-1)
    while (start == end):
        end  = col1,row1 = R.randint(0,grid-1),R.randint(0,grid-1)

    #print(start,end)

    ww0 = col0*W
    hh0 = row0*H

    ww1 = col1*W
    hh1 = row1*H


    P.draw.rect(S,red,(ww0,hh0,W,H),0)
    P.draw.rect(S,blue,(ww1,hh1,W,H),0)
    P.display.flip()
    T.sleep(.3)

    P.draw.rect(S,red, (ww1,hh1,W,H),0)
    P.draw.rect(S,blue,(ww0,hh0,W,H),0)
    P.display.flip()
    T.sleep(.3)

    S.fill(white)
    P.display.flip()

#print("Press 'esc' to proceed")
#loop()
