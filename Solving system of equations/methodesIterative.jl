
function Dicho(f,a,b,N)
    s = []
    if f(a)*f(b) < 0 
        x0 = (a+b)/2
        i = 1
        while i <= N+1 
            if f(x0)*f(a) <= 0 
                b = x0
            elseif f(x0)*f(a) > 0 
                a  = x0
            i += 1
            append!(s,x0)
            end
        x0 = (a+b)/2
        end
    else
        print("Les valeurs de a et b ne verifient pas la condition!")
    end
    return s
end

function Secante(f,a,b,N)
    s = []
    append!(s,a); append!(s,b)
    i = 2       #i represente le nombre de terme ici
    while i <= N 
        x1 = b - (f(b)*(b-a))/(f(b)-f(a))
        a,b = b,x1
        i +=1
        append!(s,b)
        if a == b || s[i] == s[i-1]
            break
        end
    end
    return s
end

function Newton(f,g,a,b,N)
    s = []
    x = (a+b)/2
    append!(s,x)
    i = 1
    while i <= N
        x = x - f(x)/g(x)
        i +=1
        append!(s,x)
        if g(x) == 0 || s[i] == s[i-1]
            break
        end
    end
    return s
end

#----------------

function fonction1(x)
    return x^2 - 2
end

function fonction2(x)
    x = 2*x
    return x^3 - 2*x - 5
end

#----------------
using Plots

function Newton1(f,g,a,b,sol) 
    s = []
    x0 = (a+b)/2
    x1 = x0 - f(x0)/g(x0)
    append!(s,x0); append!(s,x1)
    i = 2               #i represente le nombre d'iterations ici

    while abs(s[end]-sol)/max(s[i],s[i-1]) > 10^-12 
        x0 = x1
        x1 = x0 - f(x0)/g(x0)
        if g(x1) == 0 || s[i] == s[i-1] 
            break
        end
        i +=1
        append!(s,x1)
    end

    return i-1
end

function Secante1(f,a,b,sol)
    s = []
    append!(s,a); append!(s,b)
    i = 0

    while abs(s[end]-sol) > 10^-12 
        x1 = b - (f(b)*(b-a))/(f(b)-f(a))
        a,b = b,x1
        append!(s,b)
        i +=1
        if a == b
            break
        end
    end
    return i
end

function Dicho1(f,a,b,sol)
    s = []

    if f(a)*f(b) < 0 
        x0 = (a+b)/2
        append!(s,x0)
        i = 0
        while abs(s[end]-sol) > 10^-12 
            if f(x0)*f(a) <= 0 
                b = x0
            elseif f(x0)*f(a) > 0 
                a  = x0
            end
            i += 1
            x0 = (a+b)/2
            append!(s,x0)
        end
    else 
        print("Les valeurs de a et b ne verifient pas la condition!")
    end

    return i
end

function CompareTemps(f,g,a,b,sol)

    d = Dicho1(f,a,b,sol)
    n = Newton1(f,g,a,b,sol)
    s = Secante1(f,a,b,sol)

    temps_dicho = @elapsed(Dicho(f,a,b,d))
    temps_newton = @elapsed(Newton(f,g,a,b,n))
    temps_secante = @elapsed(Secante(f,a,b,s))

    print("Dicho:", temps_dicho,"\n")
    print("Newton:", temps_newton,"\n")
    print("Secante:", temps_secante,"\n")

    return f
end


