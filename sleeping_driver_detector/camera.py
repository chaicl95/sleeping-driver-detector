import cv2 as cv
import numpy as np

class Camera:
    def __init__(self) -> None:
        self.cap = cv.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("Camera is not initialized")
        
    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Can't receive frame")
        return frame

    


