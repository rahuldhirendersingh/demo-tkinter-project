from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

def swap_image():
    global counter
    img_label.config(image=img_list[counter % len(img_list)])
    print(counter)
    counter += 1

counter = 1

root.title("Wallpaper Viewer")
root.configure(background="black")
root.geometry("500x600")

files = os.listdir('wallpapers')
img_list = []

for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    resized_img = img.resize((400, 300))
    img_list.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image=img_list[0])
img_label.pack(pady=(50,15))

btn = Button(root, text="Next", fg="black", bg="white", width=28, height=2, command=swap_image)
btn.pack()
btn.config(font=('verdana', 12))
root.mainloop()