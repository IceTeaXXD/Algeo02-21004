from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    706.0,
    158.0,
    1048.0,
    500.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    139.0,
    526.0,
    605.0,
    600.0,
    fill="#333A47",
    outline="")

canvas.create_rectangle(
    706.0,
    526.0,
    1172.0,
    600.0,
    fill="#333A47",
    outline="")

canvas.create_rectangle(
    233.0,
    158.0,
    575.0,
    500.0,
    fill="#000000",
    outline="")

canvas.create_text(
    896.0,
    20.0,
    anchor="nw",
    text="Copyright © 2022 Academicos",
    fill="#D4D4D4",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    736.0,
    547.0,
    anchor="nw",
    text="Result :",
    fill="#D4D4D4",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    163.0,
    547.0,
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
    x=536.0,
    y=669.0,
    width=198.06346130371094,
    height=35.0
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
    x=89.0,
    y=670.0,
    width=150.0634765625,
    height=35.0
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
    x=980.0,
    y=669.0,
    width=230.0,
    height=33.0
)
window.resizable(True, True)
window.mainloop()
