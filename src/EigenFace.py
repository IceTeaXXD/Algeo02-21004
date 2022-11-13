# filename: EigenFace.py
# deskripsi: melakukan algoritma eigenface
from PIL import Image
import cv2 as cv
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

def EuclideanDistance(faceMatriks, EigenNewFace):
    min = 999999999999
    for i in range (len(faceMatriks)):
        temp = np.subtract(faceMatriks[i],EigenNewFace)
        for j in range (len(temp[i])):
            for k in range (256):
                distance = temp[i][j]**2
                if (distance < min).any():
                    min = distance
                    idxdistance = i
    return idxdistance

def arrEigenFace(S,data):
    #membuat suatu array of matrix dari eigen face
    ret = []
    selisih = OM.Selisih(S,data)
    for i in range (data):
        Val,Vec = Eig.getEigen(S[i])
        eFace = EigenFace(Vec,selisih[i],S)
        np.append(ret,eFace)
    return ret


S = II.DataSetToMatrix("D:/SemesterIII/Algeo/Tubes2/1/Algeo02-21004/datasets/pins_Adriana Lima")
arrOfEigen = arrEigenFace(S,213)
mean = OM.RataRataMatrix(S)
idx = EuclideanDistance(arrOfEigen,EigenNewFace("D:/SemesterIII/Algeo/Tubes2/1/Algeo02-21004/datasets/pins_Adriana Lima/Adriana Lima2_100.jpg",mean))

cv.imwrite('gambar1',S[idx])
#klo bener berarti nanti gambar1 ini sama kyk  adriana lima2 100