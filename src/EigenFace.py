# filename: EigenFace.py
# deskripsi: melakukan algoritma eigenface
from PIL import Image
import cv2 as cv
import numpy as np
import OperasiMatriks as OM
import Eigen as Eig
import InputImage as II
import time

def EigenFace(eigenvector, selisih, S):
    #I.S. eigenvector dan selisih berupa matriks terdefinisi.
            # S set of matriks
    #F.S. mengembalikan nilai eigenface dari satu wajah
    eigFace = []
    A = np.array([selisih[0]])
    for i in range(1,len(selisih)):
        A = np.concatenate((A,[selisih[i]]),axis = 0)
    A = np.transpose(A)
    A = A[0]
    A = np.transpose(A)
    for i in range(0,len(S)):
        miu = np.dot(np.transpose(eigenvector[i]),A)
        eigFace.append(miu)
    eigFace = np.array(eigFace)
    # normalize miuarr
    for i in range(len(eigFace)):
        eigFace[i] = eigFace[i] / np.linalg.norm(eigFace[i])

    # calculate the weight of each eigenface
    weight = [[0 for x in range(20)] for y in range(len(eigFace))]

    for i in range(len(selisih)):
        for j in range(20):
            weight[i][j] = np.dot(eigFace[j],selisih[i])
    weight = np.array(weight)
    return eigFace, weight

def EigenNewFace(FaceDir,mean, eigFace):
    # Buat wajah jadi matriks
    faceMatriks = II.ImgToMatrix(FaceDir)
    subtracted = np.subtract(faceMatriks, mean)
    subtracted = np.transpose(subtracted)
    subtracted = subtracted[0]
    subtracted = np.transpose(subtracted)

    weight = [[0 for i in range(20)] for j in range(1)]
    for i in range(1):
        for j in range(20):
            weight[i][j] = np.dot(eigFace[j],subtracted)
    weight = np.array(weight)
    print(np.shape(weight))
    return weight

def EuclideanDistance(faceMatriks, EigenNewFace):
    # I.S. faceMatriks dan EigenNewFace terdefinisi
    # F.S. mengembalikan nilai jarak euclidean dari wajah baru dengan wajah yang sudah ada
    distance = []
    for i in range(len(faceMatriks)):
        distance.append(np.linalg.norm(faceMatriks[i] - EigenNewFace))
    
    # return the minimum distance
    print(distance)
    return distance.index(min(distance))

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
eigface,weightf = EigenFace(eigenvec, selisih, S)
# print("Done 6")

# print the time neede to run the program

weightnf = EigenNewFace("hemscort.png",mean,eigface)
idx = EuclideanDistance(weightf,weightnf)
print(idx)

print("Time needed to run the program: ", time.process_time(), "seconds")
cv.imwrite("gambarkontolhenry.jpg",np.array(np.reshape(S[idx],(256,256))))
#klo bener berarti nanti gambar1 ini sama kyk  adriana lima2 100


# TEMP
    # min = 999999999999
    # for i in range (len(faceMatriks)):
    #     temp = np.subtract(faceMatriks[i],EigenNewFace)
    #     for j in range (len(temp[i])):
    #         for k in range (256):
    #             distance = temp[i][j]**2
    #             if (distance < min).any():
    #                 min = distance
    #                 idxdistance = i
    # # print(min)
    # return idxdistance