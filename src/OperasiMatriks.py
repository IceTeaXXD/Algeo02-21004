import numpy as np

def SumOfMatrix(M1, M):
    for i in range(256):
        for j in range(256):
            M[i][j] += M1[i][j]

def RataRataMatrix(S):
    M = len(S)
    sumofmatriks = [[0 for j in range(256)] for i in range(256)]
    for matriks in S:
        SumOfMatrix(matriks, sumofmatriks)
    for i in range (256):
        for j in range(256):
            sumofmatriks[i][j] /= M
    return sumofmatriks

#cari selisih
def Selisih(S,data):
    sp = np.array(S)
    d = np.array([[[0 for j in range (256)] for i in range (256)] for k in range (data)])
    mp = np.array(RataRataMatrix(S))
    for i in range (data):
        d[i] = np.subtract(sp[i],mp)
    return d

def kovarian(S,data):
    k = np.array([[0 for i in range (256)] for j in range (256)])
    sp = np.array(S)
    for i in range (data):
        k = k + np.dot(sp[i],np.transpose(sp[i]))
    k = np.multiply(k,(1/data))
    return k