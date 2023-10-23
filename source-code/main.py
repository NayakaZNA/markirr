import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

# Ini jangan diotak-atik rek
import os
khongguan = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./Assets/")
def gambar(indomie: str) -> str:
    return khongguan + indomie

# Inisialisasi Awal
## Tipe Kendaraan
vehicle_type    = ''
slot_mobil      = [[0 for i in range(5)] for i in range(5)]
#slot_motor      =

## Dictionary Data Tempat Parkir
tempat_parkir = {
    'motor': {
        'reguler': {
            'space': 20,
            'rate': 5000  # Tarif per hari
        },
        'VIP': {
            'space': 5,
            'rate': 10000  # Tarif per hari
        }
    },
    'mobil': {
        'reguler': {
            'space': 50,
            'rate': 10000  # Tarif per hari
        },
        'VIP': {
            'space': 10,
            'rate': 20000  # Tarif per hari
        }
    }
}

# Fungsi dan Prosedur
## Prosedur slot
def slot(x: float, y: float, blok: str, num: int, page: tk.Frame, disabled: bool = False):
    # Pembuat Button Slot Parkir
    slot_l   = tk.Button(
    page,
    text= f"{blok}{num}",
    bg="#1F93C5"
    )
    slot_l.place(
        x       = x,
        y       = y,
        width   = 34,
        height  = 51
    )
    slot_l.configure(command= lambda: p3.tkraise())
    if disabled:
        slot_l.configure(borderwidth=0, highlightthickness=0, background="#A7B8C8", state="disabled")
    else:
        slot_l.configure(borderwidth=0, highlightthickness=0, activebackground="#D5DCEE")
    return

## Prosedur label
def label(label_img: tk.PhotoImage, page: tk.Frame, x: float, y: float, width: float, height: float):
    # Pembuat Label Tkinter
    label_l    = tk.Label(page, image = label_img)
    label_l.place(
        x       = x,
        y       = y,
        width   = width,
        height  = height
    )
    return

# Konfigurasi Window
window  = tk.Tk()
window.geometry("760x570")
window.resizable(False, False)
window.title("Markirr™")

# Import Assets
header_img  = ImageTk.PhotoImage(Image.open(gambar("header.png")))
markirrw_img= ImageTk.PhotoImage(Image.open(gambar("markirr-white.png")))
markirrl_img= ImageTk.PhotoImage(Image.open(gambar("markirr_black.png")))
border_img  = ImageTk.PhotoImage(Image.open(gambar("parking_border.png")))
text1_img   = ImageTk.PhotoImage(Image.open(gambar("text1.png")))
text2_img   = ImageTk.PhotoImage(Image.open(gambar("text2.png")))
text3_img   = ImageTk.PhotoImage(Image.open(gambar("text3.png")))

# Halaman-Halaman
p1          = tk.Frame(window, width=760, height=570)
p2_motor    = tk.Frame(window, width=760, height=570)
p2_mobil    = tk.Frame(window, width=760, height=570)
p3          = tk.Frame(window, width=760, height=570)
p4          = tk.Frame(window, width=760, height=570)

for frame in (p1, p2_mobil, p2_motor, p3, p4):
    frame.grid(row=0, column=0, sticky='news')

# Halaman Utama
p1.configure(bg="#243447")
p1.place(anchor='center', relx=0.5, rely=0.5)

## Header
label(header_img, p1, 0, -32, 760, 231)

## Logo & Slogan
label(markirrw_img, p1, 264, 42, 257, 98)

## Instruksi
label(text1_img, p1, 208, 231, 343, 22)

## Mobil
mobil_img   = ImageTk.PhotoImage(Image.open(gambar("mobil.png")))
mobil_l     = tk.Button(
    p1, image = mobil_img, 
    command = lambda: [p2_mobil.tkraise(), lambda vehicle_type: ("mobil")])
mobil_l.place(
    x       = 116, 
    y       = 296,
    width   = 199,
    height  = 205
)
mobil_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

## Motor
motor_img   = ImageTk.PhotoImage(Image.open(gambar("motor.png")))
motor_l     = tk.Button(
    p1, image = motor_img, 
    command = lambda: [p2_motor.tkraise()]
    )
motor_l.place(
    x       = 444, 
    y       = 296,
    width   = 199,
    height  = 197
)
motor_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")


# Halaman 2 (Mobil)
p2_mobil.configure(bg="#243447")
p2_mobil.place(anchor='center', relx=0.5, rely=0.5)

## Tombol Home
home1_img   = ImageTk.PhotoImage(Image.open(gambar("home.png")))
home1_l     = tk.Button(
    p2_mobil, image = home1_img, 
    command = lambda: [p1.tkraise()])
home1_l.place(
    x       = 701,
    y       = 229,
    width   = 89,
    height  = 79
)
home1_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

## Layout Parkir
### Border
label(border_img, p2_mobil, 70, 85, 593, 342)

### Tersedia?
label(text2_img, p2_mobil, 486, 404, 144, 83)

### Markirr Logo
label(markirrl_img, p2_mobil, 26, 506, 125, 42)

### Button Parkir
#### Blok A
slot(117, 98, 'A', 1, p2_mobil)
slot(159, 98, 'A', 2, p2_mobil)
slot(201, 98, 'A', 3, p2_mobil)
slot(243, 98, 'A', 4, p2_mobil)
slot(285, 98, 'A', 5, p2_mobil, disabled=True)

### Blok B
slot(404, 98, 'B', 1, p2_mobil)
slot(446, 98, 'B', 2, p2_mobil, disabled=True)
slot(488, 98, 'B', 3, p2_mobil, disabled=True)
slot(530, 98, 'B', 4, p2_mobil, disabled=True)
slot(572, 98, 'B', 5, p2_mobil)

### Blok C
slot(160, 234, 'C', 1, p2_mobil)
slot(230, 234, 'C', 2, p2_mobil, disabled=True)
slot(300, 234, 'C', 3, p2_mobil)
slot(370, 234, 'C', 4, p2_mobil)

#### Blok D
slot(117, 363, 'D', 1, p2_mobil, disabled=True)
slot(159, 363, 'D', 2, p2_mobil)
slot(201, 363, 'D', 3, p2_mobil)
slot(243, 363, 'D', 4, p2_mobil, disabled=True)
slot(285, 363, 'D', 5, p2_mobil)

# Halaman 2 (Motor)
p2_motor.configure(bg="#243447")
p2_motor.place(anchor='center', relx=0.5, rely=0.5)

## Tombol Home
home2_img   = ImageTk.PhotoImage(Image.open(gambar("home.png")))
home2_l     = tk.Button(
    p2_motor, image = home2_img,
    command = lambda: [p1.tkraise()])
home2_l.place(
    x       = 701,
    y       = 229,
    width   = 89,
    height  = 79
)
home2_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")

# Halaman 3 (Plat Nomor)
p3.configure(bg="#243447")
p3.place(anchor='center', relx=0.5, rely=0.5)
## Header
label(header_img, p3, 0, -32, 760, 231)

## Logo & Slogan
label(markirrw_img, p3, 264, 42, 257, 98)

# Eksekusi
p1.tkraise()
window.mainloop()
