from tkinter import Toplevel, Button, RIGHT
import numpy as np
import cv2


class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.filtered_image = None

        self.black_white_button = Button(master=self, text="Black White")

        self.black_white_button.bind("<ButtonRelease>", lambda e: self.black_white_released())

        self.black_white_button.pack()

    def black_white_released(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.show_image()

    # this function updates image_viewer object's show_image function
    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)




