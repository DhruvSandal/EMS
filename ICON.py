from tkinter import *
from PIL import Image, ImageTk
root =Tk()

image=Image.open("check.jpeg")
photo =ImageTk.Photoimage(image)

root.mainloop()

