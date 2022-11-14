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
    A = np.array([selisih[0]])
    for i in range(1,len(selisih)):
        A = np.concatenate((A,[selisih[i]]),axis = 0)
    A = np.transpose(A)
    A = A[0]
    A = np.transpose(A)
    for i in range(0,len(S)):
        miu = np.dot(np.transpose(eigenvector[i]),A)
        miuarr.append(miu)
    miuarr = np.array(miuarr)
    return miuarr

def EigenNewFace(FaceDir,mean, eigenvector):
    # Buat wajah jadi matriks
    miuface = []
    faceMatriks = II.ImgToMatrix(FaceDir)
    subtracted = np.subtract(faceMatriks, mean)
    subtracted = np.transpose(subtracted)
    print(eigenvector)
    print(len(eigenvector))
    print(len(eigenvector[0]))
    # for i in range(len(eigenvector)):
    #     miuFace = np.dot(eigenvector[i], subtracted)
    #     miuface.append(miuFace)
    # miuface = np.array(miuface)
    return miuface

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

# Siapkan himpunan S
S = II.DataSetToMatrix("../datasets/DATASET")
# print("Done 1")

# Hitung rata-rata
mean = OM.RataRataMatrix(S)
# print("Done 2")
# cv.imwrite("keanure.jpg",np.array(np.reshape(mean,(256,256))))

# Hitung selisih
selisih = OM.Selisih(S, len(S))
# print("Done 3")

# Buat Kovarian
cov = OM.kovarian(selisih, len(selisih))
# print("Done 4")

# Hitung EigenVector dari Kovarian
eigenval, eigenvec = Eig.getEigen(cov)
# print("Done 5")

# Hitung EigenFace training Images
eigface = EigenFace(eigenvec, selisih, S)
# print("Done 6")

eignf = EigenNewFace("./obama.jpg",mean,eigenvec)
print(len(eignf))
idx = EuclideanDistance(eigface,eignf)
print(idx)

cv.imwrite('gambar1.jpg',S[idx])
#klo bener berarti nanti gambar1 ini sama kyk  adriana lima2 100