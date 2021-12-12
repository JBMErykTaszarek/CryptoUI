from random import randint

def SubstractShares(shares,secret):
    currentShare = secret
    for i in range(len(shares)):
        currentShare -= shares[i]
    print(currentShare)
    return  currentShare

def GenerateShares(sharesCount,k,secret):
    sharesTable = []
    for i in range (sharesCount-1):
        sharesTable.append(randint(0,k-1))
    sharesTable.append(SubstractShares(sharesTable, secret)%k)
    return sharesTable

def GenerateSecret(shares,k):
    return (sum(shares))%k
