from pathlib import Path
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
import tkinter as tk
import PIL

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")
def detectCam(dataset):
    start = time.time()
    path = "./face.jpg"
    if (dataset!=None):
        image = cv.imread(path)
        image = cv.resize(image, (256,256))

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        S, FNS = II.DataSetToMatrix(dataset)
        print("Done 1")

        # Hitung rata-rata
        mean = OM.RataRataMatrix(S)
        print("Done 2")

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

        if (th):
            image_result = Image.fromarray(np.reshape(S[idx], (256,256)))
            image_result = ImageTk.PhotoImage(image_result)
            canvas.itemconfig(img_result,image = image_result)
            label_result.image = image_result
            canvas.itemconfig(name,text = f"Result: {FNS[idx]}", font=("Poppins Bold", 20 * -1))
        else:
            image_result = Image.open("not found.png")
            image_result = image_result.resize((256,256))
            image_result = ImageTk.PhotoImage(image_result)
            canvas.itemconfig(img_result,image = image_result)
            label_result.image = image_result
            canvas.itemconfig(name,text = "Not Found")
        end = time.time()
        t = end-start
        canvas.itemconfig(wkt,text = "Compile time: "+ str(round(t,2)) + " second", font=("Poppins Bold", 20 * -1))
    else:
        canvas.itemconfig(name,text="Silakan pilih dataset terlebih dahulu!",font=("Poppins Bold", 20 * -1))

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

        # Update Gambar
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Update gambar
        canvas.itemconfig(img_input,image=image)
        label_input.image = image

        # Manipulasi segala 
        # Siapkan himpunan S
        S, FNS = II.DataSetToMatrix(dataset)
        print("Done 1")

        # Hitung rata-rata
        mean = OM.RataRataMatrix(S)
        print("Done 2")

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

        if (th):
            image_result = Image.fromarray(np.reshape(S[idx], (256,256)))
            image_result = ImageTk.PhotoImage(image_result)
            canvas.itemconfig(img_result,image = image_result)
            label_result.image = image_result
            canvas.itemconfig(name,text = f"Result: {FNS[idx]}", font=("Poppins Bold", 20 * -1))
        else:
            image_result = Image.open("./not found.png")
            image_result = image_result.resize((256,256))
            image_result = ImageTk.PhotoImage(image_result)
            canvas.itemconfig(img_result,image = image_result)
            label_result.image = image_result
            canvas.itemconfig(name,text = "Not Found")
        end = time.time()
        t = end-start
        canvas.itemconfig(wkt,text = "Compile time: "+ str(round(t,2)) + " second", font=("Poppins Bold", 20 * -1))
    else:
        canvas.itemconfig(name,text="Silakan pilih dataset terlebih dahulu!",font=("Poppins Bold", 20 * -1))

# Memilih folder dataset,
# Mengembalikan folder dataset
def select_dataset():
    global dataset
    dataset_path = fd.askdirectory()
    dataset = dataset_path
    return

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
dataset = None
window.geometry("1280x720")
window.configure(bg = "#12151D")
window.title("Face Recognition")

canvas = Canvas(
    window,
    bg = "#12151D",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

#Dummy Image
canvas.place(x = 0, y = 0)
# camera = tk.scale
# Gambar Input
img = Image.open("default.jpg")
img = img.resize((256,256))
img = ImageTk.PhotoImage(img)
img_input = canvas.create_image(
    200,
    150,
    anchor = "nw",
    image = img
)
label_input = Label(image = img)

img_result = canvas.create_image(
    750,
    150,
    anchor = "nw",
    image = img
)
label_result = Label(image = img)

canvas.create_rectangle(
    139.0,
    426.0,
    505.0,
    480.0,
    fill="#333A47",
    outline="")

canvas.create_rectangle(
    706.0,
    426.0,
    1072.0,
    480.0,
    fill="#333A47",
    outline="")

canvas.create_text(
    896.0,
    # 1000,
    20.0,
    anchor="nw",
    text="Copyright © 2022 Academicos",
    fill="#D4D4D4",
    font=("Poppins Regular", 20 * -1)
)

name = canvas.create_text(
    736.0,
    437.0,
    anchor="nw",
    text="Result :",
    fill="#D4D4D4",
    font=("Poppins Bold", 32 * -1)
)

wkt = canvas.create_text(
    163.0,
    437.0,
    anchor="nw",
    text="Compile Time :",
    fill="#D4D4D4",
    font=("Poppins Bold", 32 * -1)
)
canvas.create_text(
    403.0,
    82.0,
    anchor="nw",
    text="Eigen Face Recognition",
    fill="#D4D4D4",
    font=("Poppins Bold", 40 * -1)
)

#Button image
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [select_gambar(dataset)],
    relief="flat"
)
button_1.place(
    x=676.0,
    y=569.0,
    width=198.06346130371094,
    height=35.0
)
#---------------------------------------------------------------------
cap = None
def Stream():
    global cap
    cap = cv.VideoCapture(0)
    Cam()
def Cam():
# Load the cascade
    face_cascade = cv.CascadeClassifier('./face_detector.xml')
    global cap
    _, img = cap.read()
    tempimg = img
    # roi_color = None
    if _== True:
        # Read the frame
        gray = img
        # Convert to grayscale
        gray = cv.cvtColor(gray, cv.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            # capture every 5 seconds
            if time.time() % 5 < 0.1:
                print("Image Captured!")
                detectCam(dataset)
                cv.imwrite("face.jpg", roi_color)
        tempimg = cv.cvtColor(tempimg, cv.COLOR_BGR2RGB)
        gambar = Image.fromarray(tempimg)
        rgambar = gambar.resize((256,256))
        gambar2 = ImageTk.PhotoImage(image=rgambar)
        video.place(x=200,y=150)
        video.configure(image = gambar2)
        video.image = gambar2
        video.after(10,Cam)
    else:
        video.image = ""
        cap.release()

def Quit():
    global cap
    video.place_forget()
    cap.release()
#---------------------------------------------------------------------
video = tk.Label(window)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= Stream,
    relief="flat"
)
button_2.place(
    x=89.0,
    y=570.0,
    width=200.0634765625,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=select_dataset,
    relief="flat"
)
button_3.place(
    x=980.0,
    y=569.0,
    width=220.0,
    height=33.0
)
button_image_4 = PhotoImage(
    file = relative_to_assets("button_4.png")
)
button_4 = Button(
    image = button_image_4,
    borderwidth= 0,
    highlightthickness=0,
    command = Quit,
    relief="flat"
)
button_4.place(
    x = 360,
    y = 569,
    width = 175,
    height = 42,
)
window.resizable(False, False)
window.mainloop()
