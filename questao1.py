def maneirasPossiveis(n):
    # 1p -> (x^0 +x^1+x^2+...+x^n)
    # 2p -> (x^0 +x^2+...+x^{2 * n//2})
    # 5p -> (x^0 +x^5+...+x^{5* n//5})
    # 50p -> (x^0 +x^50+...+x^{50* n//50})
    # 100 -> (x^0 +x^100+...+x^{100* n//100})
    # 200 -> (x^0 +x^200+...+x^{200* n//200})
    # coeficiente do termo x^n = 
    qtd = 0
    for n200 in range(0, n+1,200) :
        total200 = n -n200
        for n100 in range(0,total200+1,100):
            total100 = total200-n100
            for n50 in range(0,total100+1,50):
                total50 = total100-n50
                for n20 in range(0,total50+1,20):
                    total20 = total50-n20
                    for n10 in range(0,total20+1,10):
                        total10 = total20-n10
                        for n5 in range(0,total10+1,5):
                            total5 = total10-n5
                            for n2 in range(0,total5+1,2):
                                qtd += 1
    return qtd

def maiorManeira(n,peso):
    # 1p -> (x^0 +x^1+x^2+...+x^n)
    # 2p -> (x^0 +x^2+...+x^{2 * n//2})
    # 5p -> (x^0 +x^5+...+x^{5* n//5})
    # 50p -> (x^0 +x^50+...+x^{50* n//50})
    # 100 -> (x^0 +x^100+...+x^{100* n//100})
    # 200 -> (x^0 +x^200+...+x^{200* n//200})
    # coeficiente do termo x^n = 
    maior = 0
    for n200 in range(0, n+1,200) :
        total200 = n -n200
        for n100 in range(0,total200+1,100):
            total100 = total200-n100
            for n50 in range(0,total100+1,50):
                total50 = total100-n50
                for n20 in range(0,total50+1,20):
                    total20 = total50-n20
                    for n10 in range(0,total20+1,10):
                        total10 = total20-n10
                        for n5 in range(0,total10+1,5):
                            total5 = total10-n5
                            for n2 in range(0,total5+1,2):
                                nupla = (total5-n2,n2/2,n5/5,n10/10,n20/20,n50/50,n100/100,n200/200) 
                                atual = sum([nupla[i]*peso[i] for i in range(8)])
                                if atual>maior:
                                    maior = atual
                                    maiorPilha = nupla
    return maiorPilha

print(maneirasPossiveis(200))
#print(maiorManeira(200, (1.52,1.85,1.89,2.05,1.7,1.78,2.8,2.5)))
#print(maiorManeira(200, (3.56,7.12,3.25,6.5,5,8,8.75,12)))

        




