#buat stopwatch
import tkinter as tk

#inisiasi tkinter
root = tk.Tk()

# label
stopwatch = tk.Label(root, text="Test")
stopwatch.pack()

menit = 0
detik = 0

def update_stopwatch():
    global menit
    global detik

    if detik < 59:
        detik += 1
    elif detik == 59:
        detik = 0
        menit +=1

    # perbarui Label.
    time_string = "{:02d}:{:02d}".format(menit, detik)
    stopwatch.config(text=time_string)

    root.after(1000, update_stopwatch)  #memanggil kembali dalam 1000 ms


update_stopwatch() #mulai mengupdet stopwatch
root.mainloop()
