from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#BFBFBF")
window.title("Face Recognition")

canvas = Canvas(
    window,
    bg = "#BFBFBF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    853.0,
    145.0,
    1253.0,
    545.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    387.0,
    145.0,
    787.0,
    545.0,
    fill="#000000",
    outline="")

canvas.create_text(
    1015.0,
    644.0,
    anchor="nw",
    text="Academicos",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    673.0,
    554.0,
    anchor="nw",
    text="Result :",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    77.0,
    554.0,
    anchor="nw",
    text="Compile Time :",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    270.0,
    28.0,
    anchor="nw",
    text="Eigen Face Recognition",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=59.0,
    y=332.0,
    width=262.1025390625,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=59.0,
    y=443.0,
    width=262.1025390625,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=59.0,
    y=221.0,
    width=262.1025390625,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
