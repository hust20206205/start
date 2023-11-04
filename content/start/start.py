import shutil
from tkinter import filedialog


thu_muc1 = filedialog.askdirectory(
    initialdir="C:/Users/vvn20206205/Desktop/nghia/src")
print("🐍 File: start/start.py | Line: 7 | undefined ~ thu_muc1", thu_muc1)


thu_muc2 = filedialog.askdirectory(
    initialdir="C:/Users/vvn20206205/Desktop/start/content")
print("🐍 File: start/start.py | Line: 10 | undefined ~ thu_muc2", thu_muc2)


shutil.rmtree(thu_muc1)
print(f"Đã sao chép thư mục {thu_muc2} vào {thu_muc1}")


shutil.copytree(thu_muc2, thu_muc1)
print(f"Đã sao chép thư mục {thu_muc2} vào {thu_muc1}")
