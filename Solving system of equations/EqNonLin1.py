#Librairies nécessaires
import numpy as np
import math
import time

#Fonctions Dicho, Secante et Newton  

def Dicho(f,a,b,N):
    A=np.zeros(N+1)
    B=np.zeros(N+1)
    X=np.zeros(N+1)
    if f(a)*f(b)>0:
        print("La fonction doit changer de signe entre a et b.")
        return []
    else:
        A[0]=a
        B[0]=b
        X[0]=(a+b)/2
        for k in range(N):
            if f(A[k])*f(X[k]) <= 0:
                A[k+1]=A[k]
                B[k+1]=X[k]
                X[k+1]=(A[k+1]+B[k+1])/2
            else:
                A[k+1]=X[k]
                B[k+1]=B[k]
                X[k+1]=(A[k+1]+B[k+1])/2
        return X

def Secante(f,a,b,N):
    X=np.zeros(N+1)
    X[0]=a;
    X[1]=b;
    for k in range(1,N):
        if X[k]==X[k-1]:
            X[k+1]=X[k]
        else:
            X[k+1]=X[k] - f(X[k])*(X[k]-X[k-1])/(f(X[k])-f(X[k-1]))
    return X

print(Secante(math.sin,2,4,100))

def Newton(f,g,a,b,N):
    X=np.zeros(N+1)
    X[0]=(a+b)/2
    for k in range(N):
        X[k+1]=X[k] - f(X[k])/g(X[k])
    return X

###################################
#Fonctions Nb_iterations

def NbIterations_Dicho(f,a,b,epsilon,s):
    N=2
    x=Dicho(f,a,b,N)
    while abs(x[N]-s)>epsilon:
        N=N+1
        x=Dicho(f,a,b,N)
    return N

def NbIterations_Secante(f,a,b,epsilon,s):
    N=2
    x=Secante(f,a,b,N)
    while abs(x[N]-s)>epsilon:
        N=N+1
        x=Secante(f,a,b,N)
    return N

def NbIterations_Newton(f,g,a,b,epsilon,s):
    N=2
    x=Newton(f,g,a,b,N)
    while abs(x[N]-s)>epsilon:
        N=N+1
        x=Newton(f,g,a,b,N)
    return N

###################################
#Fonctions des exemples 2 et 3

def f2(x):
    return x*x-2

def g2(x):
    return 2*x

def f3(x):
    return x**3-2*x-5

def g3(x):
    return 3*x**2-2


###################################
#valeurs théoriques

s2=math.sqrt(2)

alpha=math.sqrt(643)/(2*3*math.sqrt(3)) + 5/2
s3=alpha**(1/3)+2/(3*alpha**(1/3))