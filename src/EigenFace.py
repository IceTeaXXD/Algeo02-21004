# filename: EigenFace.py
# deskripsi: melakukan algoritma eigenface

def EigenFace(eigenvector, selisih, S):
    #I.S. eigenvector dan selisih berupa matriks terdefinisi.
            # S set of matriks
    #F.S. mengembalikan nilai eigenface dari satu wajah
    miu = 0
    for i in range(0,len(S)):
        miu += selisih[i] * eigenvector[0][i]
    return miu