import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from io import BytesIO

def search_files():
    file_paths = filedialog.askopenfilenames(
        title = "Select files",
        filetypes = (("All Files", "*.*"), ("WebP Files", "*.webp"))
    )
    return file_paths

def convert_to_gif(file_paths):
    for file_path in file_paths:
        with Image.open(file_path) as img:
            gif_path = file_path.rsplit(".", 1)[0] + ".gif"
            png_path = file_path.rsplit(".", 1)[0] + ".png"
            print(f'file opened = {file_path}')
            if hasattr(img, 'is_animated') and img.is_animated:
                print(f'frames = {img.n_frames}')
                img.save(gif_path,
                    'gif',
                    background=0,
                    quality=100,
                    lossless=True,
                    save_all=True,
                    subsampling=0)
            else:
                print('not animated')
                img.save(png_path, background=0, lossless=True, quality=100, subsampling=0)

root = tk.Tk()
root.geometry("300x100")
root.title("File Converter")

search_button = tk.Button(root, text="Search", command=lambda: convert_to_gif(search_files()))
search_button.pack()

root.mainloop()
