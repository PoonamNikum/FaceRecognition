import cv2
import sys

print("started")
# img = cv2.imread('/Users/gitesh/Desktop/Python Programming/FaceRecognition/LinkedIn.jpeg')
# if img is None:
#    sys.exit("Could not read the image.")
# cv2.imshow('Beba', img)
# cv2.waitKey(0)
# cap = cv2.VideoCapture('/Users/gitesh/Desktop/Python Programming/FaceRecognition/Teasar.mpg')
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("not open")
# success, img = cap.read()
print("after video")
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)


cap.set(15, -8.0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    print("in loop")
    success, img = cap.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow("Video", img)
    k = cv2.waitKey(1)
    if k == ord("s"):
        break
cap.release()
cv2.destroyAllWindows()
