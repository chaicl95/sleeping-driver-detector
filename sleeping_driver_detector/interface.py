import cv2
import tkinter
import camera as cam
from PIL import Image, ImageTk
from tkinter import ttk


class App(tkinter.Frame):
    def __init__(self) -> None:
        self.camera = cam.Camera()
        self.window = tkinter.Tk()
        self.window.wm_title("Sleeping Driver Detector")
        self.window.config(background="#FFFFFF")
        self.img_frame = ttk.Frame(self.window, width=600, height=500)
        self.img_frame.grid(row=0, column=0, padx=10, pady=2)
        self.display = ttk.Label(self.img_frame)
        self.display.grid(row=0, column=0)

    def _read_to_imgtk(self):
        frame = self.camera.read()
        frame = cv2.flip(frame, 1)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        return imgtk

    def _stream_camera(self):
        imgtk = self._read_to_imgtk()
        self.display.imgtk = imgtk
        self.display.configure(image=imgtk)
        self.display.after(10, self._stream_camera)
    
    def start(self):
        self._stream_camera()
        self.window.mainloop()