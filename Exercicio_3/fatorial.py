def fatorial(n):
    if (n>0 and n <2):
        return 1
    elif(n<0):
        return "Entrada invalida"
    else:
        fat = 1
        for i in range(1,n+1):
            fat *= i
        return fat