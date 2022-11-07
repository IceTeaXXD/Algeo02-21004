from tkinter import *
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import cv2 as cv

def select_gambar():
    global img_input, img_result, name

    # Buka File
    path = fd.askopenfilename()

    # Baca gambar
    image = cv.imread(path)
    image = cv.resize(image, (256,256))

    # Manipulasi segala disini
    # Fungsi FR nanti taro disini aja
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    # Update gambar
    img_input.configure(image=image)
    img_input.image = image

    # contoh not found
    found = True
    if (not found):
        image_result = Image.open("./src/not found.png")
        image_result = ImageTk.PhotoImage(image_result)
        img_result.configure(image = image_result)
        img_result.image = image_result
        name.configure(text = "Not Found")
    else:
        name.configure(text = "Someone's Name")


# Initialize tkinter
root = Tk()

# Nama Window
root.title("Face Recognition")

# Judul Dari APP
judul = Label(text="Eigenface Face Recognition", font=('14'))
judul.grid(column=0, columnspan=2, row=0)

# Set 2 tempat gambar
img = ImageTk.PhotoImage(Image.open("./src/default.jpg"))
img_input = Label(image = img, width=256, height=256)
img_result = Label(image = img, width=256, height=256)
img_input.grid(column=0, row=1, padx=5)
img_result.grid(column=1, row=1, padx=5)

# The Name
name = Label(root, text="Name Space")
name.grid(row=2, columnspan=2, column=0)

# Button select gambar
btn = Button(root, text="Pilih Gambar", command=select_gambar)
btn.grid(row=3, columnspan=2, column=0)

root.mainloop()