import cv2 as cv
import numpy as np

def draw_boxes(frame, results, width, height):
    out= results[0]
    n_detections= out.shape[1]
    img_height, img_width= frame.shape[:2]
    x_scale= img_width/width
    y_scale= img_height/height
    conf_threshold= 0.7
    score_threshold= 0.25
    nms_threshold=0.2
    class_ids=[]
    score=[]
    boxes=[]

    for i in range(n_detections):
        detect=out[0][i]
        confidence= detect[4]
        if confidence >= conf_threshold:
            class_score= detect[5:]
            class_id= np.argmax(class_score)
            if (class_score[class_id]> score_threshold):
                score.append(confidence)
                class_ids.append(class_id)
                x, y, w, h = detect[0], detect[1], detect[2], detect[3]
                left= int((x - w/2)* x_scale )
                top= int((y - h/2)*y_scale)
                width = int(w * x_scale)
                height = int(y * y_scale)
                box= np.array([left, top, width, height])
                boxes.append(box)

    indices = cv.dnn.NMSBoxes(boxes, np.array(score), conf_threshold, nms_threshold)
    for i in indices:
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3] 
        cv.rectangle(frame, (left, top), (left + width, top + height), (0, 0, 255), 3)
    return frame