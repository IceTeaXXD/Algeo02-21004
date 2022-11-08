# filename: Eigen.py
# deskripsi: melakukan operasi-operasi eigen
import numpy as np
import math
from numpy.linalg import qr

def VektorSatuan(M):
    # convert numpy array to normal array
    temp = []
    for i in range(3):
        temp.append(M[i])

    sum = 0
    for i in range (3):
        sum += temp[i] ** 2

    sum = math.sqrt(sum)

    for i in range (3):
        temp[i] = temp[i] / sum
    temp = np.array(temp)

    return temp
    
def DotProduct(M,N):
    sum = 0
    for i in range (3):
        sum = sum + M[i] * N[i]
    return sum

def GetVectorK(matriks, k):
    temp = []
    for i in range(3):
        for j in range(3):
            if (j == k):
                temp.append(matriks[i][j])
    temp = np.array(temp)
    return temp

def A_to_Q(matriks):
    # buat matriks 256 x 256
    Q = []
    tempMat = []

    for i in range(3):
        tempMat.append(matriks[i])
        
    for i in range(3):
        ak = GetVectorK(tempMat,i)
        if (i == 0):
            temp = GetVectorK(tempMat,i)
            Q.extend([VektorSatuan(temp)])
        else:
            temp = ak
            for j in range (i):
                ej = GetVectorK(np.transpose(Q),j)
                ej = VektorSatuan(ej)
                temp = np.subtract(temp,DotProduct(ak,ej)*ej)
            Q.extend([VektorSatuan(temp)])

    Q = np.array(Q)
    Q = np.transpose(Q)
    return Q

def A_to_R(Q, A):
    # Make transpose
    temp = Q
    for i in range(3):
        for j in range(3):
            Q[i][j] = temp[j][i]
    R = np.dot(Q,A)
    return R

def getEigen(A):
    # iterasi sebanyak 20 kali saja
    EigenVal = A
    for i in range(20):
        Q = A_to_Q(EigenVal)
        R = A_to_R(Q,EigenVal)
        EigenVal = np.dot(R,Q)
    return EigenVal

A = [[2, 2, 4], [1, 3, 5],[2, 3, 4]]
print(getEigen(A))


a = np.array([[2, 2, 4], 
              [1, 3, 5],
              [2, 3, 4]])
p = [1, 5, 10, 20]
for i in range(20):
    q, r = qr(a)
    a = np.dot(r, q)

print(a)