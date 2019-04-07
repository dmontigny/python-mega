import cv2

face_cascade = cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml")

img = cv2.imread("faces/2015_lost.jpg")
print((img.shape))

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow('grey', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
