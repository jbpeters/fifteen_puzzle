#! /usr/bin/python3

A=[3]

def L(A):
    if  A[0] <= A[1]:
        if A[0] <= A[2]:
            return 0
        else:
            return 2
    elif A[1] <= A[2]:
        return 1
    else:
        return 2





X = [0,0,0]
print(X,L(X))
X = [0,0,1]
print(X,L(X))
X = [0,0,2]
print(X,L(X))
X = [0,1,0]
print(X,L(X))
X = [0,1,1]
print(X,L(X))
X = [0,1,2]
print(X,L(X))
X = [0,2,0]
print(X,L(X))
X = [0,2,1]
print(X,L(X))
X = [0,2,2]
print(X,L(X))
X = [1,0,0]
print(X,L(X))
X = [1,0,1]
print(X,L(X))
X = [1,0,2]
print(X,L(X))
X = [1,1,0]
print(X,L(X))
X = [1,1,1]
print(X,L(X))
X = [1,1,2]
print(X,L(X))
X = [1,2,0]
print(X,L(X))
X = [1,2,1]
print(X,L(X))
X = [1,2,2]
print(X,L(X))
X = [1,2,2]
print(X,L(X))
X = [2,0,0]
print(X,L(X))
X = [2,0,1]
print(X,L(X))
X = [2,0,2]
print(X,L(X))
X = [2,1,0]
print(X,L(X))
X = [2,1,1]
print(X,L(X))
X = [2,1,2]
print(X,L(X))
X = [2,2,0]
print(X,L(X))
X = [2,2,1]
print(X,L(X))
X = [2,2,2]
print(X,L(X))
