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

def EigenNewFace(FaceDir):

    # Buat wajah jadi matriks
    faceMatriks = II.ImgToMatrix(FaceDir)
    avgFace = OM.RataRataMatrix(faceMatriks)
    EigenVal, EigenVec = Eig.getEigen(avgFace)
    subtracted = np.subtract(faceMatriks,avgFace)
    miuFace = np.dot(EigenVec, subtracted)

    return miuFace