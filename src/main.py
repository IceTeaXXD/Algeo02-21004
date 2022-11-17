from tkinter import *
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import cv2 as cv
import Eigen as Eig
import EigenFace as EigF
import OperasiMatriks as OM
import InputImage as II
import numpy as np
import time

# Fungsi menerima dataset untuk diubah
# Jika fungsi dijalankan, akan sekaligus menjalankan FR
def select_gambar(dataset):
    start = time.time()
    global img_input, img_result, name, wkt
    if(dataset != None):
        # Buka File
        path = fd.askopenfilename()
        t = 0
        # Baca gambar
        image = cv.imread(path)
        image = cv.resize(image, (256,256))

        # Manipulasi segala 
        # Siapkan himpunan S
        S = II.DataSetToMatrix(dataset)
        print("Done 1")

        # Hitung rata-rata
        mean = OM.RataRataMatrix(S)
        print("Done 2")
        # cv.imwrite("keanure.jpg",np.array(np.reshape(mean,(256,256))))

        # Hitung selisih
        s2 = OM.Selisih(S, len(S))
        print("Done 3")

        # Buat Kovarian
        cov = OM.kovarian(s2, len(s2))
        print("Done 4")

        # Hitung EigenVector dari Kovarian
        eigenval, eigenvec = Eig.getEigen(cov)
        print("Done 5")

        # Hitung EigenFace training Images
        eigface,weightf = EigF.EigenFace(eigenvec, s2, S)
        print("Done 6")
        
        weightnf = EigF.EigenNewFace(path,mean,eigface)
        print("Done 7")

        idx,th = EigF.EuclideanDistance(weightf,weightnf)
        print("Done 8")

        # print the time neede to run the program
        # print("Time needed to run the program: ", time.process_time(), "seconds")

        # Fungsi FR nanti taro disini aja
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Update gambar
        img_input.configure(image=image)
        img_input.image = image

        if (th):
            image_result = Image.fromarray(np.reshape(S[idx], (256,256)))
            image_result = ImageTk.PhotoImage(image_result)
            img_result.configure(image = image_result)
            img_result.image = image_result
            name.configure(text = "Result: ")
        else:
            image_result = Image.open("./not found.png")
            image_result = ImageTk.PhotoImage(image_result)
            img_result.configure(image = image_result)
            img_result.image = image_result
            name.configure(text = "Not Found")
        end = time.time()
        t = end-start
        wkt.configure(text = "Compile time "+ str(t) + " second")
    else:
        name.configure(text="Silakan pilih dataset terlebih dahulu!")

# Memilih folder dataset,
# Mengembalikan folder dataset
def select_dataset():
    global dataset
    dataset_path = fd.askdirectory()
    dataset = dataset_path
    return

# Initialize tkinter
root = Tk()
dataset = None
# Nama Window
root.title("Face Recognition")

# Judul Dari APP
judul = Label(text="Eigenface Face Recognition", font=('14'))
judul.grid(column=0, columnspan=3, row=0)

# Set 2 tempat gambar
img = ImageTk.PhotoImage(Image.open("./default.jpg"))
img_input = Label(image = img, width=256, height=256)
img_result = Label(image = img, width=256, height=256)
img_input.grid(column=1, row=1, rowspan=2,padx=5)
img_result.grid(column=2, row=1, rowspan=2,padx=5)

# The Name
name = Label(root, text="Result: ")
name.grid(row=3, columnspan=3, column=0, pady=5)

# Button select gambar
btn = Button(root, text="Pilih Gambar Input", command=lambda: select_gambar(dataset))
btn.grid(row=2, column=0, padx=5, pady=0)

# Button select dataset
btn_data = Button(root, text = "Pilih Dataset", command=select_dataset)
btn_data.grid(row =1 , column = 0, padx=5, pady=0)

# Compile Time Label
wkt = Label(root, text="Compile Time: ")
wkt.grid(row=3, column = 0, pady=5)

root.mainloop()