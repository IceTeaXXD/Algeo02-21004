import cv2 as cv
import os

# Fungsi mengubah suatu input gambar menjadi matriks.
# Gambar dijadikan grayscale, mengembalikan matriks
# I.S. file gambar
# F.S. gambar menjadi grayscale, mengembalikan gambar
def ImgToMatrix(filename):
    # membuat gambar menjadi grayscale
    img = cv.imread(filename)
    img = cv.resize(img, (256,256))
    _grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return _grey

# Mengambil ukuran dari gambar yang diinput
# I.S. matriks gambar
# F.S. mengembalikan ukuran gambar dalam matriks
#       dengan spek [baris, kolom]
def UkuranGambar(gambar):
    baris = gambar.shape[0]
    kolom = gambar.shape[1]
    return [baris,kolom]

def DataSetToMatrix(dir):
    S = []
    for filename in os.listdir(dir):
        temp = ImgToMatrix(f'{dir}/{filename}')
        S += [temp]
    return S

def getAllDir():
    S = []
    dir = './datasets'
    for filename in os.listdir(dir):
        S += [filename]
    return S

def FolderToMatrix(dir):
    S = []
    for i in range(len(dir)):
        temp = DataSetToMatrix(f'./datasets/{dir[i]}')
        S += [temp]
    return S

S = getAllDir()
arr = FolderToMatrix(S)
print(arr)