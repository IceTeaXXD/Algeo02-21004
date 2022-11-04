import cv2 as cv

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

gambar = ImgToMatrix("./datasets/edu.png")

cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image', gambar)
cv.waitKey()