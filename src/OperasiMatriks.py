def SumOfMatrix(M1, M):
    for i in range(M1):
        for j in range(M1):
            M[i][j] += M1[i][j]

def RataRataMatrix(S):
    M = len(S)
    sumofmatriks = [[0 for j in range(256)] for i in range(256)]
    for matriks in S:
        SumOfMatrix(sumofmatriks,matriks)
    for i in range (256):
        for j in range(256):
            sumofmatriks[i][j] *= M
    return sumofmatriks