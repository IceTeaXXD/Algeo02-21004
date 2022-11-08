# filename: Eigen.py
# deskripsi: melakukan operasi-operasi eigen
import numpy as np

def VektorSatuan(M):
    # convert numpy array to normal array
    temp = []
    for i in range(256):
        temp.append(M[i])

    sum = 0
    for i in range (256):
        sum = temp[i] * temp[i]
    for i in range (256):
        temp[i] = temp[i] / sum
    temp = np.array(temp)

    return temp
    
def DotProduct(M,N):
    sum = 0
    for i in range (256):
        sum = sum + M[i] * N[i]
    return sum

def GetVectorK(matriks, k):
    temp = []
    for i in range(256):
        for j in range(256):
            if (j == k):
                temp.append(matriks[i][j])
    temp = np.array(temp)
    return temp

def A_to_Q(matriks):
    # buat matriks 256 x 256
    Q = [[0 for i in range (256)] for j in range(256)]
    Q = np.array(Q)
    for i in range(256):
        ak = GetVectorK(matriks,i)
        temp = GetVectorK(matriks,i)
        if (i != 0):
            VektorSatuan(temp)
            Q.extend(temp)
        else:
            temp = ak
            for j in range (i):
                ej = GetVectorK(Q,j)
                temp +=  add(ak,np.dot(DotProduct(ak,ej),ej))
            Q.extend(temp)
    return Q

def A_to_R(Q, A):
    # Make transpose
    temp = Q
    for i in range(256):
        for j in range(256):
            Q[i][j] = temp[j][i]
    R = np.dot(Q,A)
    return R

def getEigen(A):
    # iterasi sebanyak 20 kali saja
    EigenVal = A
    for i in range(20):
        Q = A_to_Q(EigenVal)
        R = A_to_R(EigenVal)
        EigenVal = np.dot(R,Q)
    return EigenVal