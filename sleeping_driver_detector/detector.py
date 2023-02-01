import cv2 as cv
import threading
import camera
import tensorflow as tf

class Detector:
    def __init__(self, weight_path: str, input_width: int, input_height: int, camera: camera.Camera) -> None:
        self.model = tf.saved_model.load(weight_path)
        # self.label_map = pd.read_csv(label_path, sep=';', index_col='ID')
        self.input_width = input_width 
        self.input_height = input_height
        self.camera = camera
        self.results = None
        self.stopped = False
        pass

    def _convert_cvframe_into_tensor(self, frame):
        #Resize to respect the input_shape
        inp = cv.resize(frame, (self.input_width , self.input_height))
        #Convert img to RGB
        rgb = cv.cvtColor(inp, cv.COLOR_BGR2RGB)
        rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)
        rgb_tensor = tf.expand_dims(rgb_tensor , 0)
        return rgb_tensor
    
    def _detect(self):
        while not self.stopped:
            if self.camera.frame is not None:
                tensor = self._convert_cvframe_into_tensor(self.camera.frame)
                results = self.model(tensor)
                scores = results.get("detection_scores")
                boxes = results.get("detection_boxes")
                classes = results.get("detection_classes")
                num_detections = results.get("num_detections")
                self.results = (boxes, scores, classes, num_detections)

    def start(self):
        threading.Thread(target=self._detect, args=()).start()
        return self
    
    def stop(self):
        self.stopped = True




        
