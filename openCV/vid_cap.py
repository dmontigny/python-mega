# https://www.udemy.com/the-python-mega-course/learn/lecture/4775498#content
"""This app captures video"""


import cv2
from decors import timer

fframe = None


vid = cv2.VideoCapture(0)

@timer
def get_frame():
    global fframe
    check, frame = vid.read()
    # print(check, frame)
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
            if cv2.contourArea(contour) < 1000:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y+h), (0, 255, 0), 3)

        cv2.imshow("grey", grey)
        cv2.imshow("delta", dframe)
        cv2.imshow("first", fframe)
        cv2.imshow("threshold", thresh_delta)
        cv2.imshow("rectangle", frame)


        key = cv2.waitKey(1)
        if key == ord('q'):
            return key


while True:
    if get_frame() == 113:
        break


vid.release()
cv2.destroyAllWindows()


