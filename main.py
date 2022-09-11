import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.title("The Image Editor")
window.minsize(width=1000, height=600)  # window size at start
window.config(padx=10, pady=10)  # padding


def upload_image():
    global img
    file_types = [('jpeg Files', '*.jpeg'),  # these are the file types
                  ('jpg Files', '*.jpg'),
                  ('png Files', '*.png')]
    file_name = filedialog.askopenfilename(title='Select an image',
                                           filetypes=file_types)  # this returns the full file path
    img = ImageTk.PhotoImage(file=file_name)
    button_2 = tk.Button(window, image=img)
    button_2.grid(row=1, column=1)


button_1 = tk.Button(window, text="New", width=10, command=upload_image)
button_1.grid(row=0, column=0)

window.mainloop()  # loop to keep the window open
