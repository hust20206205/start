import tkinter as tk
from tkinter import filedialog

def chon_thu_muc1():
    thu_muc1 = filedialog.askdirectory(initialdir="/path/to/initial/folder1")
    label_thu_muc1.config(text=thu_muc1)

def chon_thu_muc2():
    thu_muc2 = filedialog.askdirectory(initialdir="/path/to/initial/folder2")
    label_thu_muc2.config(text=thu_muc2)

app = tk.Tk()
app.title("Chọn Thư Mục")

frame1 = tk.Frame(app)
frame1.pack(pady=10)

label1 = tk.Label(frame1, text="Thư mục 1:")
label1.pack()

button_chon1 = tk.Button(frame1, text="Chọn", command=chon_thu_muc1)
button_chon1.pack()

label_thu_muc1 = tk.Label(frame1, text="")
label_thu_muc1.pack()

frame2 = tk.Frame(app)
frame2.pack(pady=10)

label2 = tk.Label(frame2, text="Thư mục 2:")
label2.pack()

button_chon2 = tk.Button(frame2, text="Chọn", command=chon_thu_muc2)
button_chon2.pack()

label_thu_muc2 = tk.Label(frame2, text="")
label_thu_muc2.pack()

app.mainloop()
