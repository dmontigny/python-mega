import numpy as np
import cv2

def load_img(img_name = 'smallgray.png'):
    im_grey = cv2.imread(img_name, 0)
    print(np.vstack((im_grey, im_grey)))

load_img('smallgray.png')