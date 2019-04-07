"""Practice file for opencv tutorial"""

import cv2


def galaxy_pic():
    img = cv2.imread("images/galaxy.jpg", 0)

    print(type(img))
    print(img.shape[1])

    size_ratio = 3
    resized_image = cv2.resize(img, (int(img.shape[1]/size_ratio), int(img.shape[0]/size_ratio)))
    cv2.imshow("milky way", resized_image)
    cv2.imwrite("images/galaxy_resized.png", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize_pics():
    import cv2
    import glob

    images = glob.glob("images/*.jpg")
    print(images)

    for image in images:
        print(image[7:])
        img = cv2.imread(image, 0)
        re = cv2.resize(img, (100, 100))
        cv2.imshow("Hey", re)
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.imwrite("images/resized_" + image[7:], re)


resize_pics()
