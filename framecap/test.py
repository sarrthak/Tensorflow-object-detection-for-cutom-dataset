import cv2

cap=cv2.VideoCapture("C:\\Users\\Admin\\Pictures\\Camera Roll\\WIN_20190621_22_32_10_Pro.mp4")
print("The value of frames per second: ",cap.get(cv2.CAP_PROP_FPS))
cv2.CAP_PROP_FPS = 10
#cap.set(cv2.CAP_PROP_FPS,20)
print("The value of frames per second (after change): ",cap.get(cv2.CAP_PROP_FPS))
    