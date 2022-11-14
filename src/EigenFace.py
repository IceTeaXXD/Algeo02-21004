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
            miu += np.dot(eigenvector[i][k], selisih[i])
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
    # print(min)
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


# Siapkan himpunan S
S = II.DataSetToMatrix("../datasets/DATASET")
# print("Done 1")

# Hitung rata-rata
mean = OM.RataRataMatrix(S)
# print("Done 2")
# cv.imwrite("keanure.jpg",np.array(np.reshape(mean,(256,256))))

# Hitung selisih
selisih = OM.Selisih(S, len(S))
print(selisih)
# print("Done 3")

# Buat Kovarian
cov = OM.kovarian(selisih, len(selisih))
print("------------------------------------\n")
print(cov)
# print("Done 4")

# Hitung EigenVector dari Kovarian
# eigenval, eigenvec = Eig.getEigen(cov)
# print("Done 5")

# Hitung EigenFace training Images
# eigface = EigenFace(eigenvec, selisih, S)
# print("Done 6")

# idx = EuclideanDistance(eigface,EigenNewFace("./obama.jpg",mean))
# print(idx)

# cv.imwrite('gambar1.jpg',S[idx])
#klo bener berarti nanti gambar1 ini sama kyk  adriana lima2 100