import cv2 as cv
import numpy as np
import threading
import camera
import torch
import onnxruntime as rt

class Detector:
    def __init__(self, weight_path: str, camera: camera.Camera) -> None:
        self.net = cv.dnn.readNetFromONNX(weight_path)
        # self.label_map = pd.read_csv(label_path, sep=';', index_col='ID')
        self.camera = camera
        self.input_width = camera.width 
        self.input_height = camera.height
        self.results = None
        self.stopped = False
        pass

    def _convert_cvframe_into_nparray(self, frame):
        # frame = cv.resize(frame, dsize=(640, 640), interpolation=cv.INTER_AREA)
        # frame = frame[:, :, ::-1].transpose(2, 0, 1)
        # frame = np.expand_dims(frame, axis=0)
        # frame = frame.astype(np.float32) / 255.0
        blob = cv.dnn.blobFromImage(frame, 1/255 , (640, 640), swapRB=True, mean=(0,0,0), crop= False)
        return blob
    
    def _detect(self):
        while not self.stopped:
            if self.camera.frame is not None:
                tensor = self._convert_cvframe_into_nparray(self.camera.frame)
                self.net.setInput(tensor)
                outputs= self.net.forward(self.net.getUnconnectedOutLayersNames())
                self.results = outputs


    def start(self):
        threading.Thread(target=self._detect, args=()).start()
        return self
    
    def stop(self):
        self.stopped = True




        
