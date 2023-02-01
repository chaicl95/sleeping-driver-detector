import cv2 as cv

def draw_boxes(frame, results, width, height):
    boxes, scores, classes, num_detections = results
    pred_labels = classes.numpy().astype('int')[0]
    pred_boxes = boxes.numpy()[0].astype('float')
    pred_scores = scores.numpy()[0]

    #loop throughout the detections and place a box around it  
    for score, (ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
        if score < 0.5:
            continue
        xmin = int(xmin * height)
        ymin = int(ymin * width)
        xmax = int(xmax * height)
        ymax = int(ymax * width)
        score_txt = f'{100 * round(score,0)}'
        frame = cv.rectangle(frame,(xmin, ymax),(xmax, ymin),(0,255,0),1)   
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame,score_txt,(xmax, ymax-10), font, 0.5, (255,0,0), 1, cv.LINE_AA)
    return frame