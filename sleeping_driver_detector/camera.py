import cv2 as cv
from typing import Tuple

class Camera:
    def __init__(self, video_source =0) -> None:
        self.cap = cv.VideoCapture(video_source)
        if not self.cap.isOpened():
            raise Exception("Camera is not initialized")
        self.height = self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        self.width = self.cap.get(cv.CAP_PROP_FRAME_WIDTH)
        
    def get_frame(self):
        ret = 0
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return (ret, frame)
            return (ret, None)
        return (ret, None)
        
    def __del__(self):
        if self.cap.isOpened():
            self.cap.released()
    


            
            

    


