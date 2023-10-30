import tkinter as tk

# Inisiasi tkinter
root = tk.Tk()

# Label
stopwatch = tk.Label(root, text="00:00")
stopwatch.pack()

jam, menit, detik = 0, 0, 0
berjalan    = True
def update_stopwatch():
    global jam, menit, detik
    
    if berjalan:
        detik += 1
        detik %= 60
        if detik == 59:
            menit += 1
            menit %= 60
        if menit == 59:
            jam += 1

    # Perbarui Label.
    time_string = "{:02d}:{:02d}:{:02d}".format(jam, menit, detik)
    stopwatch.config(text=time_string)

    root.after(100, update_stopwatch)  # Memanggil kembali dalam 1000 ms

update_stopwatch()  # Mulai mengupdate stopwatch

# Fungsi untuk menghentikan dan melanjutkan stopwatch
def stop_stopwatch():
    global berjalan
    berjalan = not berjalan
    if berjalan:
        stop_button.config(text="Stop")
    else:
        stop_button.config(text="Start")

# Fungsi untuk mereset stopwatch
def reset_stopwatch():
    global jam, menit, detik
    jam, menit, detik = 0, 0, 0

# Tombol "Stop"
stop_button = tk.Button(root, text="Stop", command=stop_stopwatch)
stop_button.pack()

# Tombol "Reset"
reset_button = tk.Button(root, text="Reset", command=reset_stopwatch)
reset_button.pack()

root.mainloop()
