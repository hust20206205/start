import tkinter as tk
from tkinter import filedialog


def chon_thu_muc1():
    thu_muc1 = filedialog.askdirectory(
        initialdir="C:/Users/vvn20206205/Desktop/nghia/src")
    label_thu_muc1.config(text=thu_muc1)


def chon_thu_muc2():
    thu_muc2 = filedialog.askdirectory(
        initialdir="C:/Users/vvn20206205/Desktop/start/content")
    label_thu_muc2.config(text=thu_muc2)


def chon_thu_muc3():
    exit()


app = tk.Tk()
app.title("Chọn Thư Mục")

frame1 = tk.Frame(app)
frame1.pack(pady=10)
button_chon1 = tk.Button(
    frame1, text="Chọn thư mục nghia", command=chon_thu_muc1)
button_chon1.pack()
label_thu_muc1 = tk.Label(frame1, text="")
label_thu_muc1.pack()

frame2 = tk.Frame(app)
frame2.pack(pady=10)
button_chon2 = tk.Button(
    frame2, text="Chọn thư mục start", command=chon_thu_muc2)
button_chon2.pack()
label_thu_muc2 = tk.Label(frame2, text="")
label_thu_muc2.pack()

frame3 = tk.Frame(app)
frame3.pack(pady=10)
button_chon3 = tk.Button(
    frame3, text="Chuyển đổi", command=chon_thu_muc3)
button_chon3.pack()


app.mainloop()
