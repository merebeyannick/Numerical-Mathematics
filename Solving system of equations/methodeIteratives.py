import time
from math import *

import math
def Dicho(f,a,b,N):
    s = []
    if f(a)*f(b) < 0 :
        #x0 = (a+b)/2
        i = 1
        while i != N+1 :
            x0 = (a+b)/2
            if f(x0)*f(a) <= 0 :
                b = x0
            elif f(x0)*f(a) > 0 :
                a  = x0
            i += 1
            s.append(x0)
            #x0 = (a+b)/2
    else :
        print("Les valeurs de a et b ne verifient pas la condition!")
    return s

#print(Dicho(sin,2,4,60))

def Secante(f,a,b,N):
    s = []
    s.append(a); s.append(b)
    i = 2       #i represente le nombre de terme ici
    while i <= N :
        x1 = b - (f(b)*(b-a))/(f(b)-f(a))
        a,b = b,x1
        s.append(b)
        i +=1
        if a == b :
            break
    return s

#print(Secante(sin,2,4,15))


def Newton(f,g,a,b,N) :
    s = []
    x = (a+b)/2
    s.append(x)
    i = 0
    while i <= N :
        x = x - f(x)/g(x)
        i +=1
        s.append(x)
        if g(x) == 0 or s[i] == s[i-1] :
            break
    return s

def f1(x):
    return 2*x**3 +3*x**2 - 4*x -4

def f2(x):
    return 6*x**2 +6*x - 4

def f3(x):
    return 12*x + 6

print(Secante(f1,0,10,10))


#----------------

def fonction1(x):
    return x**2 - 2

def fonction2(x):
    x = 2*x
    return (x**3 - 2*x - 5)

#----------------

def Newton1(f,g,a,b,sol) :
    s = []
    x0 = (a+b)/2
    x1 = x0 - f(x0)/g(x0)
    s.append(x0); s.append(x1)
    i = 1               #i represente le nombre d'iterations ici

    #while abs(s[-1]-sol)/max(s[i],s[i-1]) > 10**-12 :
    while abs(s[-1]-sol) > 10**-12 :

        x0 = x1
        x1 = x0 - f(x0)/g(x0)
        if g(x1) == 0 or s[i] == s[i-1] :
            break
        i +=1
        s.append(x1)

    return i

#print(Newton1(sin,cos,2,4))

def Secante1(f,a,b,sol):
    s = []
    s.append(a); s.append(b)
    i = 0

    #while abs(s[-1]-sol)/max(a,b) > 10**-12 :
    while abs(s[-1]-sol) > 10**-12 :

        x1 = b - (f(b)*(b-a))/(f(b)-f(a))
        a,b = b,x1
        s.append(b)
        i +=1
        if a == b:
            break

    return i

print(Secante1(sin,2,4,pi))

def Dicho1(f,a,b,sol):
    s = []

    if f(a)*f(b) < 0 :
        i = 0
        x0 = (a+b)/2
        s.append(x0)
        #while abs(s[-1]-sol)/max(a,b) > 10**-12 :
        while abs(s[-1]-sol) >= 10**-12 :

            if f(x0)*f(a) <= 0 :
                b = x0
            elif f(x0)*f(a) > 0 :
                a  = x0
            i += 1
            x0 = (a+b)/2
            s.append(x0)
        return i
    else :
        print("Les valeurs de a et b ne verifient pas la condition!")


#print(Dicho1(fonction1,0,2,sqrt(2)))
#print(Dicho1(sin,2,4,pi))

def CompareTemps(f,g,a,b,sol):

    d = Dicho1(f,a,b,sol)
    n = Newton1(f,g,a,b,sol)
    s = Secante1(f,a,b,sol)

        #Dichotomie
    g1 = time.time()
    Dicho(f,a,b,d)
    g2 = time.time()
    temps_dicho = g2-g1
    print("Dicho:", temps_dicho)

        #Newton
    g1 = time.time()
    Newton(f,g,a,b,n)
    g2 = time.time()
    temps_newton = g2-g1
    print("Newton:", temps_newton)

        #Secante
    g1 = time.time()
    Secante(f,a,b,s)
    g2 = time.time()
    temps_secante = g2-g1
    print("Secante:", temps_secante)

    return []

#CompareTemps(sin,cos,2,4,pi)

