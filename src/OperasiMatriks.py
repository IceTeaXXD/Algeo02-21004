import numpy as np

def SumOfMatrix(M1, M):
    for i in range(len(M[0])):
        for j in range(len(M)):
            M[j][i] += M1[j][i]

def RataRataMatrix(S):
    M = len(S)
    sumofmatriks = [[0 for j in range(len(S[0][0]))] for i in range(len(S[0]))]
    for matriks in S:
        SumOfMatrix(matriks, sumofmatriks)
    for i in range (len(sumofmatriks[0])):
        for j in range(len(sumofmatriks)):
            sumofmatriks[j][i] /= M
    return sumofmatriks

#cari selisih
def Selisih(S,data):
    sp = np.array(S)
    d = np.array([[[0 for j in range (len(S[0][0]))] for i in range (len(S[0]))] for k in range (data)])
    mp = np.array(RataRataMatrix(S))
    for i in range (data):
        d[i] = np.subtract(sp[i],mp)
    return d

def kovarian(S,data):
    sp = np.array(S)
    k = np.array([S[0]])
    for i in range (1,data):
        k = np.concatenate((k,[sp[i]]),axis = 0) 
    kt = np.transpose(k)
    c = np.dot(np.transpose(kt[0]), kt[0])
    return c