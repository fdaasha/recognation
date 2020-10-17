import cv2
import imutils

cap = cv2.VideoCapture(-1)


ret, frame = cap.read()
cv2.imwrite('webcam.png', frame)
image = cv2.imread('webcam.png', 0)

cv2.imwrite('ok.png', image)

image = cv2.imread('ok.png')

gray = cv2.rectangle(image, (300, 300), (150, 150), (255, 0, 200), 20)
gray = cv2.line(gray, (100, 150), (400, 200), (0, 200, 255), 5)

cv2.imwrite('webcam_result.png', gray)

cv2.imshow('gray', gray)
cv2.imshow('frame', frame)

cv2.destroyAllWindows()
