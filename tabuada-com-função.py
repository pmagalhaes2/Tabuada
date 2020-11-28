def tabuada(x):
    for cont in range (1, 11):
        print("{} x {} = {}".format(x, cont, x*cont))
    
num = int(input("Digite um número inteiro: "))
tabuada (num)
