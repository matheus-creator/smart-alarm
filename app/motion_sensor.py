import cv2
import numpy as np

def run():
    frame_count = 0
    frame_rate_division = 1
    previous_frame = None
    webcam = cv2.VideoCapture(0)

    while True:
        frame_count += 1
        ret, frame = webcam.read()
        if frame_count % frame_rate_division == 0:
            prepared_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            prepared_frame = cv2.GaussianBlur(prepared_frame, ksize=(5, 5), sigmaX=0)        
            if previous_frame is None:
                previous_frame = prepared_frame
                continue
            
            diff_frame = cv2.absdiff(previous_frame, prepared_frame)
            previous_frame = prepared_frame

            kernel = np.ones((5, 5))
            diff_frame = cv2.dilate(diff_frame, kernel, 1)

            thresh_frame = cv2.threshold(diff_frame, thresh=25, maxval=255, type=cv2.THRESH_BINARY)[1]

            contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) < 50:
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
            
            cv2.imshow('Motion Sensor', frame)

            if cv2.waitKey(1) == 27:
                break