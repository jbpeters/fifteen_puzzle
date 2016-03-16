#! /usr/bin/python3

import pygame as P
import random as R

def loop():
    looping=True
    while looping:
        for E in P.event.get():
            #print("E= ",E)
            if E.type == P.KEYDOWN:
                if E.key == P.K_ESCAPE:
                    looping = False
        r[13]=0
        for i in range(0,2):            
            r[i] = R.randint(0,15)
            print(i, r[i])
        print(r)
    P.display.quit()
    return

def main():
    P.display.init()
    S=P.display.set_mode((1,1))
    P.display.flip()
    print ("hit escape to halt")
    loop()

if __name__ =="__main__":
    main()
