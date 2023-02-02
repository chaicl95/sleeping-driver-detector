import tkinter
import camera as cam
import detector
import threading
import cv2
from PIL import Image, ImageTk
from tkinter import ttk
from utils import draw_boxes

class App():
    def __init__(self, window : tkinter.Tk, weight_path) -> None:
        self.window = window
        self.window.title("Sleeping Driver Detector")
        self.window.config(background="#FFFFFF")
        
        self.camera = cam.Camera().start()
        self.detector = detector.Detector(weight_path, self.camera).start()

        # Display Canvas
        self.img_frame = ttk.Frame(self.window, width=self.camera.width, height=self.camera.height)
        self.img_frame.grid(row=0, column=0, padx=10, pady=2)
        self.display = ttk.Label(self.img_frame)
        self.display.grid(row=0, column=0)

        # Initiate
        self.delay = 5


    def _print_to_canvas(self):
        if self.camera.frame is not None:
            img = cv2.cvtColor(self.camera.frame, cv2.COLOR_BGR2RGBA)
            if self.detector.results is not None:
                img = draw_boxes(img, self.detector.results, self.detector.input_width, self.detector.input_height)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.display.imgtk = imgtk
            self.display.configure(image=imgtk)

    def update(self):
        self._print_to_canvas()
        self.window.after(self.delay, self.update)

    def start(self):
        self.update()
        self.window.mainloop()
        self.detector.stop()
        self.camera.stop()