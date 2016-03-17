#! /usr/bin/python3
import pygame as P
import random as R
box   = (w,h) = (700,700)
white = [255,255,255]
grid  = 4 
num   = [[0 for _ in range(grid)] for _ in range(grid)]
kolor = [[0 for _ in range(grid)] for _ in range(grid)]
D     = [[0 for _ in range(grid)] for _ in range(grid)]
def init (size,kolor):
    P.display.init()
    P.font.init()
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
    Z=[0,0,0]
    C=[127,127,127]
    S=[ C[0]-RGB[0],C[1]-RGB[1],C[2]-RGB[2]]
    L=[0,0,0]
    for k in range(3):
        if RGB[k] > 127:
            L[k]=255-RGB[k]
        else:
            L[k]=RGB[k]
    ll=least(L)
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
    P.draw.rect(surf,kolor,(x,y,width,height))
    if num !="":
        P.draw.rect(surf,[0,0,0],(x,y,width,height),4)
        k2 = contrast(kolor)
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
    tile(S,c2*width,r2*height,width,height, kolor[c1][r1], num[c1][r1], myfont )
    k=kolor[c2][r2]
    kolor[c2][r2] = kolor[c1][r1]
    kolor[c1][r1] = k
    n = num[c2][r2]
    num[c2][r2] = num[c1][r1]
    num[c1][r1] = n
def fetch(G):    
    px = R.randint(0,G-1)
    py = R.randint(0,G-1)
    while ( px == G-1 and py== G-1  ):
        px=R.randint(0,G-1)
        py=R.randint(0,G-1)
    f = px,py
    return f
def display():
    for row in range(grid):
        for col in range(grid):
            D[col][row]=num[row][col]
    return D
def loop(S,width,height,myfont):
    looping = True
    print("looping")
    while looping:
        for Ev in P.event.get():
            if Ev.type == P.KEYDOWN:
                if Ev.key == P.K_ESCAPE:
                    looping = False
                if Ev.key == P.K_d:
                    print(display())
                if Ev.key == P.K_m:                   
                    for of_pair in range(22):
                        E=fetch(grid)
                        F=fetch(grid)
                        while  E == F:
                            E=fetch(grid)
                            F=fetch(grid)                        
                        to  = E[0], E[1]
                        fro = F[0], F[1]
                        switch_flip(S,to,fro,width,height,myfont)
            if Ev.type == P.MOUSEBUTTONDOWN:
                mx,my = P.mouse.get_pos()
                atcol = mx * grid // box[0]
                atrow = my * grid // box[1]
                width=box[0]/grid
                height=box[1]/grid
                if atcol == target[0] or atrow == target[1]:
                    if atcol == target[0]-1 or atcol == target[0]+1: 
                        switch_flip(S,[atcol,atrow],target,width,height,myfont)
                        target[0]=atcol
                    if atrow == target[1]-1 or atrow == target[1]+1:
                        switch_flip(S,[atcol,atrow],target,width,height,myfont)
                        target[1]=atrow
    P.display.quit()
    return
def main():
    global num,target
    S = init(box,white)
    width=w/grid
    height=h/grid
    myfont = P.font.SysFont(None , 350//grid )
    for row in range(grid):
        for col in range(grid):
            num[col][row] = row*grid+col+1
            if col == grid - 1 and row == grid - 1:
                kolor[col][row]=white
                num[col][row]=""
                target=[col,row]
                continue
            kolor[col][row]=[R.randint(0,255),R.randint(0,255),R.randint(0,255)]
            tile(S,col*width,row*height,width,height,kolor[col][row],num[col][row],myfont)
            P.time.delay(37)
    loop(S,width,height,myfont)
if __name__ =="__main__":
    main()

