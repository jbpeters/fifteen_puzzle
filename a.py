#! /usr/bin/python3

import pygame as P
import random as R

box   = (w,h) = (700,700)
white = [255,255,255]
grid  = 4 
num   = [[0 for _ in range(grid)] for _ in range(grid)]
kolor = [[0 for _ in range(grid)] for _ in range(grid)]

 
def init (size,kolor):
    P.display.init()
    P.font.init()
    #myfont = P.font.SysFont(None,30)
    S = P.display.set_mode((size))
    S.fill(kolor)
    P.display.flip()
    return S

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
    #print("RGB = ",RGB, least(RGB))
    Z=[0,0,0]
    C=[127,127,127]
    S=[ C[0]-RGB[0],C[1]-RGB[1],C[2]-RGB[2]]
    #print("S   = ",S,least(S))
    L=[0,0,0]
    for k in range(3):
        if RGB[k] > 127:
            L[k]=255-RGB[k]
        else:
            L[k]=RGB[k]
    ll=least(L)
    #print("L   = ",L,ll)
    if RGB[ll] <= 127:
        w=255
    else:
        w=0
    t=(w-RGB[ll])/S[ll]
    for i in range(3):
        Z[i] = int(RGB[i] + t * S[i])
        if Z[i] < 0 :
            Z[i] = 0
        if Z[i] > 255 :
            Z[i] = 255    
    return Z

def tile(surf,x,y,width,height,kolor,num,myfont):
    print(kolor,end="")
    P.draw.rect(surf,kolor,(x,y,width,height))
    if num !="":
        P.draw.rect(surf,[0,0,0],(x,y,width,height),4)
        k2 = contrast(kolor)
        print(k2)
        surf2 = myfont.render(str(num),1,k2)
        ss = myfont.size(str(num))
        surf.blit(surf2,(x+(width-ss[0])/2,y+(height-ss[1])/2))
    P.display.flip()
    return

def switch_flip(S, P1, P2, width, height, myfont):
    c1,r1 = P1
    c1=int(c1)
    r1=int(r1)
    c2,r2 = P2
    c2=int(c2)
    r2=int(r2)
    tile(S,c1*width,r1*height,width,height, kolor[c2][r2], num[c2][r2], myfont )
    #print("tiling ",c2,r2,num[c1][r1])
    tile(S,c2*width,r2*height,width,height, kolor[c1][r1], num[c1][r1], myfont )
    #print("tiling ",c1,r1,num[c2][r2])
    #print("switching ", num[c1][r1] , " and ", num[c2][r2] )
    k=kolor[c2][r2]
    kolor[c2][r2] = kolor[c1][r1]
    kolor[c1][r1] = k
    n = num[c2][r2]
    num[c2][r2] = num[c1][r1]
    num[c1][r1] = n

def loop(S,width,height,myfont):
    looping = True
    print("looping")
    while looping:
        for E in P.event.get():
            if E.type == P.KEYDOWN:
                if E.key == P.K_ESCAPE:
                    looping = False
                if E.key == P.K_m:                    
                    for of_pair in range (2):
                        to  = R.randint(0,grid-1),R.randint(0,grid-1)
                        fro = R.randint(0,grid-1),R.randint(0,grid-1)
                        while to == fro or to ==( grid-1,grid-1) or fro == (grid-1,grid-1) :
                            fro = R.randint(0,grid-1),R.randint(0,grid-1)
                    switch_flip(S,to,fro,width,height,myfont)
            if E.type == P.MOUSEBUTTONDOWN:
                mx,my = P.mouse.get_pos()
                atcol = mx * grid // box[0]
                atrow = my * grid // box[1]
                width=box[0]/grid
                height=box[1]/grid
                x=atcol*width
                y=atrow*height
    P.display.quit()
    return

def main():
    global num
    S = init(box,white)
    width=w/grid
    height=h/grid
    myfont = P.font.SysFont(None , 350//grid )
      
    for row in range(grid):
        for col in range(grid):
            #print(col,row,row*grid+col+1)
            num[col][row] = row*grid+col+1
            if col == grid - 1 and row == grid - 1:
                kolor[col][row]=white
                num[col][row]=""
                continue
            
            kolor[col][row]=[R.randint(0,255),R.randint(0,255),R.randint(0,255)]
            tile(S,col*width,row*height,width,height,kolor[col][row],num[col][row],myfont)
            P.time.delay(37)
           
    loop(S,width,height,myfont)

if __name__ =="__main__":
    main()

