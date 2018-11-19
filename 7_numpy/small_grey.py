import numpy as np
import cv2

def load_img(img_name = 'smallgray.png'):
    im_grey = cv2.imread(img_name, 0)
    print(np.vstack((im_grey, im_grey)))

def load_gal(img_name = 'galaxy.jpg'):
    img = cv2.imread(img_name, 1)
    print(type(img))
    print(np.vstack((img, img)))
    print(img.shape, img.ndim)

    resized_img=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imshow("galaxy", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def change_pix(img_path='sample-images'):
    import glob, os
    os.chdir(img_path)
    for file in glob.glob('*.jpg'):
        img = cv2.imread(file, 1)
        print(type(img))
        resized=cv2.resize(img,(100, 100))
        print((file.split('.')[0] + '_resized.' + file.split('.')[1]))
        cv2.imwrite((file.split('.')[0] + '_resized' + file.split('.')[1]), resized)

change_pix()



