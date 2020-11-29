## Libraries imported
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

## Create window
root = tk.Tk()
root.minsize(width = 300, height = 420)
root.maxsize(width = 300, height = 420)

canvas1 = tk.Canvas(root, width = 300, height= 420, bg = 'azure3',
                    relief = 'raised')
canvas1.pack()

## Create label
label1 = tk.Label(root, text = "Image convertor", bg = 'azure3')
label1.config(font = ('helvetica', 20))
canvas1.create_window(150, 20, window = label1)

## Get image
# ----------
def getImage():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

    messagebox.showinfo("Information", "Image is uploaded")

browsImage = tk.Button(text = "Import Image", 
                            command = getImage, 
                            bg = 'royalblue',
                            fg = 'white',
                            font = ('helvetixa', 12, 'bold'),
                            border = 0,
                            activebackground = "green")
canvas1.create_window(150, 60, window = browsImage)
# -------------------------------------------------

## Convert jpg
# ------------
def convertJPG():
    global im1

    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpg')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into JPG")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

jpg_button = tk.Button(text = "Convert to JPG", 
                        command = convertJPG,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 100, window = jpg_button)
# --------------------------------------------------

## Conert to jpeg
# ---------------
def convertJPEG():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpeg')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into JPEG")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

jpeg_button = tk.Button(text = "Convert to JPEG", 
                        command = convertJPEG,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 140, window = jpeg_button)
# ---------------------------------------------------

## Convert to png
# ---------------
def convertPNG():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.png')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into PNG")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

png_button = tk.Button(text = "Convert to PNG", 
                        command = convertPNG,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 180, window = png_button)
# --------------------------------------------------

## Convert to tif
# ---------------
def convertTIF():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.tif')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into TIF")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

tif_button = tk.Button(text = "Convert to TIF", 
                        command = convertTIF,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 220, window = tif_button)
# --------------------------------------------------

## Convert to tiff
# ----------------
def convertTIFF():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.tiff')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into TIFF")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

tiff_button = tk.Button(text = "Convert to TIFF", 
                        command = convertTIFF,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 260, window = tiff_button)
# ---------------------------------------------------

## Convert gif
# ------------
def convertGIF():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.gif')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into GIF")
    except:
        messagebox.showwarning("Warning", "Import image first")

gif_button = tk.Button(text = "Convert to GIF", 
                        command = convertGIF,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 300, window = gif_button)
# --------------------------------------------------

## Convert to eps
# ---------------
def convertEPS():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.eps')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into EPS")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

eps_button = tk.Button(text = "Convert to EPS", 
                        command = convertEPS,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 340, window = eps_button)
# --------------------------------------------------

## Convert to bmp
# ---------------
def convertBMP():
    global im1
    try:
        print("Image info")
        print(im1)
        export_file_path = filedialog.asksaveasfilename(defaultextension = '.bmp')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Converted into BMP")
    except NameError:
        messagebox.showwarning("Warning", "Import image first")

bmp_button = tk.Button(text = "Convert to BMP", 
                        command = convertBMP,
                        bg = 'royalblue',
                        fg = 'white',
                        font = ('helvetica', 12, 'bold'),
                        border = 0)
canvas1.create_window(150, 380, window = bmp_button)
# --------------------------------------------------



root.mainloop()