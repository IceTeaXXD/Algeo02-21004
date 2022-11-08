# filename: Eigen.py
# deskripsi: melakukan operasi-operasi eigen

def VektorSatuan(M):
    sum = 0
    for i in range (256):
        sum = M[0][i] * M[0][i]
    for i in range (256):
        M[0][i] = M[0][i] / sum

def DotProduct(M,N):
    sum = 0
    for i in range (256):
        sum = sum + M[i] * N[i]
    return sum