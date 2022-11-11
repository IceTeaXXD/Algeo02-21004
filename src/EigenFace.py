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

mean = II.DataSetToMatrix("../datasets/pins_Adriana Lima/")
arr = EigenNewFace("../datasets/pins_Adriana Lima/Adriana Lima0_0.jpg",mean)
print(arr)


def EuclideanDistance(FaceDir, EigenNewFace):
    arr = []
    min = 99999999
    faceMatriks = II.ImgToMatrix(FaceDir)
    for i in range (len(faceMatriks)):
        temp = np.subtract(faceMatriks[i],EigenNewFace)
        for j in range (256):
            for k in range (256):
                distance = temp[i][j]**2
                if distance < min:
                    min = distance
                    idxdistance = i
        arr.append(distance)
    return idxdistance
    