# filename: EigenFace.py
# deskripsi: melakukan algoritma eigenface

import numpy as np
import OperasiMatriks as OM
import Eigen as Eig
import InputImage as II

def EigenFace(eigenvector, selisih, S):
    #I.S. eigenvector dan selisih berupa matriks terdefinisi.
            # S set of matriks
    #F.S. mengembalikan nilai eigenface dari satu wajah
    miuarr = []
    for i in range(0,len(S)):
        miu = 0
        for k in range(0, len(S[0])):
            miu += selisih[i] * eigenvector[i][k]
        miuarr.append(miu)
    miuarr = np.array(miuarr)
    return miuarr

def EigenNewFace(FaceDir,mean):
    # Buat wajah jadi matriks
    faceMatriks = II.ImgToMatrix(FaceDir)
    EigenVal, EigenVec = Eig.getEigen(faceMatriks)
    subtracted = np.subtract(faceMatriks,mean)
    miuFace = np.dot(EigenVec, subtracted)

    return miuFace

def EuclideanDistance(FaceDir, EigenNewFace):
    arr = []
    min = 99999999
    faceMatriks = II.ImgToMatrix(FaceDir)
    for i in range (len(faceMatriks)):
        temp = np.subtract(faceMatriks[i],EigenNewFace)
        for j in range (len(temp[i])):
            for k in range (256):
                distance = temp[i][j]**2
                if (distance < min).any():
                    min = distance
                    idxdistance = i
        arr.append(distance)
    return idxdistance

mean = II.DataSetToMatrix("../datasets/pins_Adriana Lima/")
idx = EuclideanDistance("../datasets/pins_Adriana Lima/Adriana Lima173_74.jpg",EigenNewFace("../datasets/pins_Adriana Lima/Adriana Lima173_74.jpg",mean))
print(idx)