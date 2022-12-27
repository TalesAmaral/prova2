def erastotenes(n):
    lista = [True for i in range(n+1)]
    lista[0] = False
    lista[1] = False
    for i in range(n+1):
      if lista[i]:
          for g in range(i**2, n+1, i):
              lista[g] = False
    return ( i for i in range(n) if lista[i]) 
def isPrimo(n, listaPrimos):
    for i in listaPrimos:
        if not n%i:
            return 0
    return 1

n = 1000
listaPrimos = erastotenes(n)

listaStr =  [ str(i) for i in listaPrimos]
duplas = []
print(listaStr)
lenStr = len(listaStr)
for i in range(lenStr):
    strI = listaStr[i]
    for g in range(i+1,lenStr):
        strG = listaStr[g]
        somaEsquerda = strI+strG
        somaDireita = strG+strI
        if int(somaEsquerda)>n or int(somaDireita)>n:
            if isPrimo(int(somaDireita), listaPrimos) and isPrimo(int(somaEsquerda), listaPrimos):
                duplas.append((i,g))
        elif somaEsquerda in listaStr and somaDireita in listaStr:
            duplas.append((i,g))
trios  = []
for i in duplas:
    
print(len(duplas))
            

