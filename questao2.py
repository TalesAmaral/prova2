
def erastotenes(n):
    lista = [True for i in range(n+1)]
    lista[0] = False
    lista[1] = False
    for i in range(n+1):
      if lista[i]:
          for g in range(i**2, n+1, i):
              lista[g] = False
    return [ i for i in range(n) if lista[i]] 
def isPrimo(n, listaPrimos):
    for i in listaPrimos:
        if not n%i:
            return 0
    return 1
def isUniaoPrimo(strI,strG):
    somaEsquerda = strI+strG
    somaDireita = strG+strI
    if int(somaEsquerda)>n or int(somaDireita)>n:
        if isPrimo(int(somaDireita), listaPrimos) and isPrimo(int(somaEsquerda), listaPrimos):
            return 1
    elif somaEsquerda in listaStr and somaDireita in listaStr:
        return 1 
    return 0
def isSetMergePrime(setX, setY):
    for i in setX:
        for g in setY:
            if  not isUniaoPrimo(i,g):
                return 0
    return 1
def correnteCinco(lista):
    for i in lista:
        if len(i)==5:
            return 1
    return 0
n = 10000
listaPrimos = erastotenes(n)
listaStr =  [ str(i) for i in listaPrimos]
dictPrimos = { i: set() for i in listaStr}
tamStr = len(listaStr)
for i in range(tamStr):
    strI = listaStr[i]
    for g in range(i+1,tamStr):
        strG = listaStr[g]
        if isUniaoPrimo(strI,strG):
            dictPrimos[strI].add(strG)
            dictPrimos[strG].add(strI)
menor = float("inf")
segundo = float("inf")

for i in dictPrimos:
    setI = dictPrimos[i]
    for g in setI:
        setG = dictPrimos[g]
        intIG = setI.intersection(setG)
        for h in intIG:
            setH = dictPrimos[h]
            intIGH = intIG.intersection(setH)
            for j in intIGH:
                setJ = dictPrimos[j]
                intIGHJ = intIGH.intersection(setJ)
                for k in intIGHJ:
                    setK = set([i,g,h,j,k])
                    soma = int(i)+int(g)+int(h)+int(j)+int(k)
                    if soma < menor:
                        menor = soma
                        vecMenor = setK

print(menor)
print(vecMenor)


