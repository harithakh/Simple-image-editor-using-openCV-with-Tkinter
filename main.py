import tkinter as tk
from tkinter import ttk
from editPane import EditPane
from imageViewer import ImageViewer


# The Main class is inherited from tk.Tk class
class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)  # this line is to keep the inheritance of the parent's __init__() function.

        self.filename = ""
        self.original_image = None
        self.processed_image = None

        self.is_image_selected = False

        self.title("Image Editor")

        self.editPane = EditPane(master=self)  # here we pass the Tk object(master) to EditPane.
        separating_line = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.image_viewer = ImageViewer(master=self)

        self.editPane.pack(pady=10)
        separating_line.pack(fill=tk.X, padx=20, pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)
