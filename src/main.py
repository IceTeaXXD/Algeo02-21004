from tkinter import *
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import cv2 as cv

# Fungsi menerima dataset untuk diubah
# Jika fungsi dijalankan, akan sekaligus menjalankan FR
def select_gambar(dataset):
    global img_input, img_result, name
    if(dataset != None):
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
img = ImageTk.PhotoImage(Image.open("./src/default.jpg"))
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
time = Label(root, text="Compile Time: ")
time.grid(row=3, column = 0, pady=5)

root.mainloop()