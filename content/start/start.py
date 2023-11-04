import shutil
from tkinter import filedialog


folder1 = filedialog.askdirectory(
    initialdir="C:/Users/vvn20206205/Desktop/nghia/src",
    title="Select source directory"
)
print(f"Selected source directory: {folder1}")


folder2 = filedialog.askdirectory(
    initialdir="C:/Users/vvn20206205/Desktop/start/content",
    title="Select destination directory"
)
print(f"Selected destination directory: {folder2}")


shutil.rmtree(folder1)
print(f"Removed directory: {folder1}")


shutil.copytree(folder2, folder1)
print(f"Copied directory from {folder2} to {folder1}")
