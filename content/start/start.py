import shutil
from tkinter import filedialog


thu_muc1 = filedialog.askdirectory(
    initialdir="C:/Users/vvn20206205/Desktop/nghia/src",
    title="Select source directory"
)
print(f"Selected source directory: {thu_muc1}")


thu_muc2 = filedialog.askdirectory(
    initialdir="C:/Users/vvn20206205/Desktop/start/content",
    title="Select destination directory"
)
print(f"Selected destination directory: {thu_muc2}")


shutil.rmtree(thu_muc1)
print(f"Removed directory: {thu_muc1}")


shutil.copytree(thu_muc2, thu_muc1)
print(f"Copied directory from {thu_muc2} to {thu_muc1}")
