from random import randint

def GetRandomAs(t):
    randomAValues = []
    for i in range (t-1):
        randomAValues.append(randint(0,1000))
    return randomAValues

def GetSi(shares, s, sharesToRecover, p, avalues):
    returnSi = []
    for i in range(shares):
        suma = []
        for j in range(sharesToRecover-1):
            suma.append(avalues[j]*pow(i,j))
        returnSi.append([i, s + sum(suma) % p])
    return returnSi

def GetSiList(list, indexes):
    idxes = indexes.split(",")
    returnlist = []
    for idx in idxes:
        returnlist.append(list[int(idx)])
    return returnlist

def RecoverSecret(siIndexes, siList,prime):
    SharesList = GetSiList(siList, siIndexes)
    interpolation = []
    for item in SharesList:
        licznik =1
        mianownik =1
        otherShares = [i for i in SharesList if i[0] != item[0]]
        for otherShare in otherShares:
            licznik *= -otherShare[0]
            mianownik *= (item[0] - otherShare[0])
        interpolation.append([licznik,mianownik])
    count =0
    divmodSum =0
    for item in SharesList:
        divmodSum += DivMod(item[1] * interpolation[count][0],interpolation[count][1],prime)

    print("secret:")
    print(divmodSum % prime)

    return divmodSum % prime


def DivMod(a, den,p):
        inv = ExtendedEuclideanAlgorithm(den, p)
        return a * inv

def ExtendedEuclideanAlgorithm(a, b):
    x0 = 1
    xn = 1
    y0 = 0
    yn = 0
    x1 = 0
    y1 = 1
    r = a%b
    while (r > 0):
        q = a / b
        xn = x0 - q * x1
        yn = y0 - q * y1
        x0 = x1
        y0 = y1
        x1 = xn
        y1 = yn
        a = b
        b = r
        r = a % b
    return xn
