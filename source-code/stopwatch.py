import tkinter as tk

# Inisiasi tkinter
root = tk.Tk()

# Label
stopwatch = tk.Label(root, text="00:00")
stopwatch.pack()

menit = 0
detik = 0
berjalan = True
def update_stopwatch():
    global menit
    global detik
    
    if berjalan:
        if detik < 59:
            detik += 1
        elif detik == 59:
            detik = 0
            menit += 1

    # Perbarui Label.
    time_string = "{:02d}:{:02d}".format(menit, detik)
    stopwatch.config(text=time_string)

    root.after(1000, update_stopwatch)  # Memanggil kembali dalam 1000 ms

update_stopwatch()  # Mulai mengupdate stopwatch

# Fungsi untuk menghentikan dan melanjutkan stopwatch
def stop_stopwatch():
    global berjalan
    berjalan = not berjalan

# Fungsi untuk mereset stopwatch
def reset_stopwatch():
    global menit, detik
    menit = 0
    detik = 0
    stopwatch.config(text="00:00")

# Tombol "Stop"
stop_button = tk.Button(root, text="Stop", command=stop_stopwatch)
stop_button.pack()

# Tombol "Reset"
reset_button = tk.Button(root, text="Reset", command=reset_stopwatch)
reset_button.pack()

root.mainloop()
