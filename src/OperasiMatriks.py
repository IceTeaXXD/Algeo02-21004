import numpy as np
import InputImage as II
import os
import cv2 as cv

def SumOfMatrix(M1, M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] += M1[i][j]

def RataRataMatrix(S):
    M = len(S)
    sumofmatriks = [[0 for j in range(len(S[0][0]))] for i in range(len(S[0]))]
    for matriks in S:
        SumOfMatrix(matriks, sumofmatriks)
    for i in range (len(sumofmatriks[0])):
        for j in range(len(sumofmatriks)):
            sumofmatriks[j][i] /= M
    return sumofmatriks
def norm(S):
    Sp = np.array(S)
    rata = [0 for i in range (len(S[0]))]
    for i in range(len(S[0])):
        for j in range (len(S)):
            rata[i] += S[j][i]
    rata = np.multiply(rata,1/len(S))
    # print(Sp)
    for i in range (len(S)):
        Sp[i] = np.subtract(Sp[i],rata)
    return Sp
#cari selisih
def rata(S):
    Sp = np.array(S)
    rata = [0 for i in range (len(S[0]))]
    for i in range(len(S[0])):
        for j in range (len(S)):
            rata[i] += S[j][i]
    rata = np.multiply(rata,1/len(S))
    return rata
def Selisih(S,data):
    sp = np.array(S)
    d = np.array([[[0 for j in range (len(S[0][0]))] for i in range (len(S[0]))] for k in range (data)])
    mp = np.array(RataRataMatrix(S))
    for i in range (data):
        d[i] = np.subtract(sp[i],mp)
    return d
sel = [[1,2,3],[1,2,3],[1,2,3]]
# print(Selisih(sel,2))
# print(RataRataMatrix(sel))
    
def kovarian(S,data):
    sp = np.array(S)
    k = np.array([S[0]])
    for i in range(1,data):
        k = np.concatenate((k,[sp[i]]),axis = 0)
    kt = np.transpose(k)
    kt = kt[0]
    k = np.transpose(kt)
    c = np.dot(k, kt)
    return c
# a = [[1,2,3,4],[1,2,3,4]]
# c = kovarian(a,2)
# print(c)
# print(np.cov(a))

def imm(filename):
    # membuat gambar menjadi grayscale
    img = cv.imread(filename)
    img = cv.resize(img, (256,256))
    _grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # _grey = _grey.reshape(65536,1)
    return _grey
S = II.DataSetToMatrix('D:/SemesterIII/Algeo/Tubes2/1/Algeo02-21004/datasets/DATASET')
# print(S)
# selisih = Selisih(S,len(S))
# no = norm(S)
# print(no)
# print(selisih)
# print("--------")
# c = kovarian(selisih,len(selisih))