def multiplosDeTresOuCinco(x):
    resultado = 0
    for i in range(1,x):
        if(i%3==0):
            resultado+=i
        elif(i%5==0):
            resultado+=i
    return resultado