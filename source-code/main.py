# Program Markirr
# Perangkat lunak sistem manajemen parkir cerdas otomatis oleh
# William Anthony               [16523109]; Lead Presenter
# Muhammad Jafar Fadli          [16523137]; Backend
# Zulfaqqar Nayaka Athadiansyah [19623116]; Software Engineer and GUI Designer
# Abdullah Farhan               [19623305]; Lead Analyst

# KAMUS
## Daftar Variabel

## Daftar Fungsi/Prosedur 

# ALGORITMA

import tkinter as tk
from PIL import ImageTk, Image
import os


# Inisialisasi Awal
## Database
### Kode Wilayah
plat_nomor      = ["A","AA","AB","AD","AE","AG","B","BA","BB","BD","BE","BG","BH","BK","BL","BM","BN",
                   "BP","BR","D","DA","DB","DC","DD","DE","DG","DH","DK","DL","DM","DN","DP","DR","DT","DW",
                   "E","EA","EB","ED","F","G","H","K","KB","KH","KT","KU","L","M","N","P","PA","PB","S","T",
                   "W","Z"]
### Dictionary Data Tempat Parkir
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
## Dictionary Blok Parkir
blokk = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4
}

##
vehicle_type    = ''
slot_id         = ["", 0]
slots           = [[0 for j in range(5)] for i in range(5)]     +   [[0 for i in range(10)] for i in range(4)]
plat            = [["" for j in range(5)] for i in range(5)]    +   [["" for j in range(10)] for i in range(4)]
tersedia_mobil  = 19
tersedia_motor  = 40

# Konfigurasi Window
window  = tk.Tk()
window.geometry("760x570")
window.resizable(False, False)
window.title("Markirr™")

# Import Assets
def gambar(indomie: str) -> str:
    #
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "./Assets/") + indomie

header_img  = ImageTk.PhotoImage(Image.open(gambar("header.png")))
markirrw_img= ImageTk.PhotoImage(Image.open(gambar("markirr-white.png")))
markirrl_img= ImageTk.PhotoImage(Image.open(gambar("markirr_black.png")))
border_img  = ImageTk.PhotoImage(Image.open(gambar("parking_border.png")))
home_img    = ImageTk.PhotoImage(Image.open(gambar("home.png")))
text1_img   = ImageTk.PhotoImage(Image.open(gambar("text1.png")))
text2_img   = ImageTk.PhotoImage(Image.open(gambar("text2.png")))
text3_img   = ImageTk.PhotoImage(Image.open(gambar("text3.png")))

# Fungsi dan Prosedur
## Fungsi isNumeric
def isNumeric(x: str) -> bool:
    # Menentukan apakah suatu string sepenuhnya terdiri atas angka
    yes = True
    for i in range(len(x)):
        if not ('0' <= x[i] <= '9'):
            yes = False
            i = len(x)
    return yes

# Fungsi isAlphabetic
def isAlphabetic(x: str) -> bool:
    # Menentukan apakah suatu string sepenuhnya terdiri atas huruf
    yes = True
    for i in range(len(x)):
        if not ('a' <= x[i] <= 'z' or 'A' <= x[i] <= 'Z'):
            yes = False
            i = len(x)
    return yes

## Prosedur label
def label(label_img: tk.PhotoImage, page: tk.Frame, x: float, y: float, width: float, height: float):
    # Mencetak label Tkinter
    label_l    = tk.Label(page, image = label_img)
    label_l.place(
        x       = x,
        y       = y,
        width   = width,
        height  = height
    )
    return

## Prosedur slot_clicked
def slot_clicked(slot: tk.Button, blok: str, num: int, slot_id = slot_id):
    # Simpan data blok dan nomor parkir secara sementara
    slot_id[0] = blokk[blok]
    slot_id[1] = num-1
    slots[slot_id[0]][slot_id[1]] = 1
    slot.config(state='disabled', background="#A7B8C8")
    # Reset kondisi entri dan dropdown
    kode_wilayah_menu['state']  = 'normal'
    nopol_menu['state']         = 'normal'
    seri_wilayah_menu['state']  = 'normal'
    ok['state']                 = 'normal'
    nopol_menu.delete(0, 4)
    seri_wilayah_menu.delete(0, 4)
    kode_wilayah.set(plat_nomor[0])
    # Menuju p3
    p3.tkraise()
    return 

## Prosedur slot
def slot(x: float, y: float, blok: str, num: int, page: tk.Frame, disabled: bool = False, VIP: bool = False):
    # Membuat button slot parkir
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
    slot_l.configure(borderwidth=0, 
                     highlightthickness=0, 
                     activebackground="#D5DCEE",
                     command= lambda: slot_clicked(slot_l, blok, num))
    return


## Prosedur home
def home(page: tk.Frame):
    # Membuat tombol home
    home_l     = tk.Button(
        page, image = home_img, 
        command = lambda: [p1.tkraise(), home_l.place_forget()])
    home_l.place(
        x       = 701,
        y       = 229,
        width   = 89,
        height  = 79
    )
    home_l.configure(borderwidth=0, highlightthickness=0, activebackground="#243447")
    return

## Prosedur caps
def caps(*args):
   # Mengubah entri menjadi uppercase
   seri_wilayah.set(seri_wilayah.get().upper())
   return

## Prosedur limit_n
def limit_n(n: int, entri: tk.StringVar, input_type: str):
    # Membatasi panjang entri menjadi n karakter dan membatasi jenis input
    if len(entri.get()) > n-1:
        entri.set(entri.get()[:n])
    if input_type == 'alphabetic':
        if not isAlphabetic(entri.get()):
            entri.set(entri.get()[:len(entri.get()) - 1])
    elif input_type == 'numeric':
        if not isNumeric(entri.get()):
            entri.set(entri.get()[:len(entri.get()) - 1])

    return
        

## Prosedur update_tnkb
def update_tnkb():
    # Memasukkan TNKB ke dalam matriks `plat`
    plat[slot_id[0]][slot_id[1]] = f"{kode_wilayah.get()} {nopol.get()} {seri_wilayah.get()}"
    return

## Prosedur ok_clicked
def ok_clicked():
    # Menjalankan sejumlah proses setelah button `ok` ditekan
    ## Mengambil nopol dan seri wilayah
    nopol_value = nopol.get()
    seri_wilayah_value = seri_wilayah.get()
    ## Percabangan: aksi dilakukan jika kolom entri sudah diisi
    if nopol_value.strip() and seri_wilayah_value.strip():
        # Update data TNKB
        update_tnkb()
        # Disable button
        kode_wilayah_menu['state']  = 'disabled'
        nopol_menu['state']         = 'disabled'
        seri_wilayah_menu['state']  = 'disabled'
        ok['state']                 = 'disabled'
        # Munculkan tombol home di halaman tersebut
        home(p3)
    else: # Entri nopol atau seri wilayah belum diisi
        print("Kolom Nopol dan Seri Wilayah tidak boleh kosong.")

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
home(p2_mobil)

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
slot(285, 98, 'A', 5, p2_mobil)

### Blok B
slot(404, 98, 'B', 1, p2_mobil)
slot(446, 98, 'B', 2, p2_mobil)
slot(488, 98, 'B', 3, p2_mobil)
slot(530, 98, 'B', 4, p2_mobil)
slot(572, 98, 'B', 5, p2_mobil)

### Blok C
slot(160, 234, 'C', 1, p2_mobil)
slot(230, 234, 'C', 2, p2_mobil)
slot(300, 234, 'C', 3, p2_mobil)
slot(370, 234, 'C', 4, p2_mobil)

#### Blok D
slot(117, 363, 'D', 1, p2_mobil)
slot(159, 363, 'D', 2, p2_mobil)
slot(201, 363, 'D', 3, p2_mobil)
slot(243, 363, 'D', 4, p2_mobil)
slot(285, 363, 'D', 5, p2_mobil)

# Halaman 2 (Motor)
p2_motor.configure(bg="#243447")
p2_motor.place(anchor='center', relx=0.5, rely=0.5)

## Tombol Home
home(p2_motor)

# Halaman 3 (Plat Nomor)
p3.configure(bg="#243447")
p3.place(anchor='center', relx=0.5, rely=0.5)
## Header
label(header_img, p3, 0, -32, 760, 231)

## Logo & Slogan
label(markirrw_img, p3, 264, 42, 257, 98)

## Instruksi
label(text3_img, p3, 227, 285, 304, 21)

## Tombol Home

## TNKB
tnkb = "          "

### Dropdown Kode Wilayah
kode_wilayah = tk.StringVar(p3)
kode_wilayah.set(plat_nomor[0])
kode_wilayah_menu   = tk.OptionMenu(p3, kode_wilayah, *plat_nomor)
kode_wilayah_menu.place(
    x       = 244,
    y       = 350,
    width   = 53,
    height  = 37
)

## Nopol
nopol       = tk.StringVar(p3)
nopol_menu  = tk.Entry(p3, textvariable=nopol,font='Garamond 15', justify="center")
nopol_menu.place(
    x       = 317,
    y       = 350,
    width   = 68,
    height  = 37
)
nopol.trace("w", lambda *args: limit_n(4, nopol, 'numeric'))

## Seri Wilayah
seri_wilayah        = tk.StringVar(p3)
seri_wilayah_menu   = tk.Entry(p3, textvariable=seri_wilayah, font='Garamond 15', justify="center")
seri_wilayah_menu.place(
    x       = 405,
    y       = 350,
    width   = 53,
    height  = 37
)
seri_wilayah_menu.bind("<KeyRelease>", caps)
seri_wilayah.trace("w", lambda *args: limit_n(3, seri_wilayah, 'alphabetic'))

## OK
ok          = tk.Button(p3, text='OK', 
                        command=lambda:[ok_clicked(),
                                        print(slots),
                                        print(plat)])
ok.place(
    x       = 470,
    y       = 350,
    width   = 37,
    height  = 37
)


# Eksekusi perulangan utama
p1.tkraise()
window.mainloop()
