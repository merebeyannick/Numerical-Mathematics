#Fonctions Dicho, Secante et Newton  

function Dicho(f,a,b,N)
    A=zeros(N+1,1)
    B=zeros(N+1,1)
    X=zeros(N+1,1)
    if f(a)*f(b)>0
        error("La fonction doit changer de signe entre a et b.")
    end
    A[1]=a;
    B[1]=b;
    X[1]=(a+b)/2;
    for k=1:N
        if f(A[k])*f(X[k]) <= 0
            A[k+1]=A[k]
            B[k+1]=X[k]
            X[k+1]=(A[k+1]+B[k+1])/2
        else
            A[k+1]=X[k]
            B[k+1]=B[k]
            X[k+1]=(A[k+1]+B[k+1])/2
        end
    end
    return X
end

function Secante(f,a,b,N)
    X=zeros(N+1,1)
    X[1]=a;
    X[2]=b;
    for k=2:N
        if X[k]==X[k-1]
            X[k+1]=X[k]
        else
            X[k+1]=X[k] - f(X[k])*(X[k]-X[k-1])/(f(X[k])-f(X[k-1]))
        end
    end
    return X
end

function Newton(f,g,a,b,N)
    X=zeros(N+1,1)
    X[1]=(a+b)/2
    for k=1:N
        X[k+1]=X[k] - f(X[k])/g(X[k])
    end
    return X
end
###################################
#Fonctions Nb_iterations

function NbIterations_Dicho(f,a,b,epsilon,s)
    N=2;
    x=Dicho(f,a,b,N);
    while abs(x[N+1]-s)>epsilon
        N=N+1;
        x=Dicho(f,a,b,N);
    end;
    return N;
end

function NbIterations_Secante(f,a,b,epsilon,s)
    N=2;
    x=Secante(f,a,b,N);
    while abs(x[N+1]-s)>epsilon
        N=N+1;
        x=Secante(f,a,b,N);
    end;
    return N;
end

function NbIterations_Newton(f,g,a,b,epsilon,s)
    N=2;
    x=Newton(f,g,a,b,N);
    while abs(x[N+1]-s)>epsilon
        N=N+1;
        x=Newton(f,g,a,b,N);
    end;
    return N;
end

###################################
#Fonctions des exemples 2 et 3

function f2(x)
    return x*x-2
end

function g2(x)
    return 2*x
end

function f3(x)
    return x^3-2*x-5
end

function g3(x)
    return 3*x^2-2
end


###################################
#valeurs théoriques

s2=sqrt(2);

alpha=sqrt(643)/(2*3*sqrt(3)) + 5/2;
s3=alpha^(1/3)+2/(3*alpha^(1/3));