# This file is for the editing buttons bar at the top

from tkinter import Frame, Button, LEFT
from tkinter import filedialog
import cv2

from filterFrame import FilterFrame


class EditPane(Frame):

    def __init__(self, master=None):  # master is a Tk object.
        Frame.__init__(self, master=master)

        # Buttons
        self.new_button = Button(self, text="New")
        self.save_button = Button(self, text="Save")
        self.clear_button = Button(self, text="Clear")
        self.filters_button = Button(self, text="Filters")

        # Binding buttons to the functions
        self.new_button.bind("<ButtonRelease>", lambda e: self.new_button_released())
        self.save_button.bind("<ButtonRelease>", lambda e: self.save_button_released())
        self.clear_button.bind("<ButtonRelease>", lambda e: self.clear_button_released())
        self.filters_button.bind("<ButtonRelease>", lambda e: self.filters_button_released())

        # placing the buttons on the window
        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.filters_button.pack(side=LEFT)
        self.clear_button.pack(side=LEFT)

    def new_button_released(self):
        filename = filedialog.askopenfilename(title='Select an image',
                                              filetypes=[('jpeg Files', r"*.jpeg *.jpg *.png")])
        image = cv2.imread(filename)

        if image is not None:
            self.master.filename = filename
            self.master.original_image = image.copy()
            self.master.processed_image = image.copy()
            self.master.image_viewer.show_image()
            self.master.is_image_selected = True

    def save_button_released(self):
        pass

    def filters_button_released(self):
        self.master.filter_frame = FilterFrame(master=self.master)
        self.master.filter_frame.grab_set()

    def clear_button_released(self):
        self.master.processed_image = self.master.original_image.copy()
        self.master.image_viewer.show_image()
