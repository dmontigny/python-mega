# https://www.udemy.com/the-python-mega-course/learn/lecture/4775498#content
"""This app captures video and detects motion"""


import cv2
import pandas
from datetime import datetime

from decors import timer

fframe = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

vid = cv2.VideoCapture(0)
# vid = cv2.VideoCapture('rtsp://dmontigny:37sunrIse@192.168.1.230:88')
# vid = cv2.VideoCapture('rtsp://dmontigny:37sunrIse@192.168.1.230:88/videostream')
# RTSP URL rtsp:// [user name][:password]@IP:Port number/videostream

def get_frame():
    global fframe
    global status_list
    check, frame = vid.read()
    # playing with flips
    frame = cv2.flip(frame, 1)

    status = 0
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if fframe is None:
        # capture reference fram
        fframe = grey
    else:
        # get delta frame
        dframe = cv2.absdiff(fframe, grey)
        thresh_delta = cv2.threshold(dframe, 100, 255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)

        (cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            if cv2.contourArea(contour) < 5000:
                continue
            status = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y+h), (0, 255, 0), 3)

        status_list.append(status)
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())
        status_list = status_list[-2:]


        cv2.imshow("grey", grey)
        cv2.imshow("delta", dframe)
        cv2.imshow("first", fframe)
        cv2.imshow("threshold", thresh_delta)
        cv2.imshow("rectangle", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            if status == 1:
                times.append(datetime.now())
            return key
        # print(status)


while True:
    if get_frame() == 113:
        break


for t in range(0, len(times), 2):
    df = df.append({"Start": times[t], "End": times[t+1]}, ignore_index=True)
df.to_csv('move_times.csv')


vid.release()
cv2.destroyAllWindows()
