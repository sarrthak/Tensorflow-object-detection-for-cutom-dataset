import cv2
vidcap = cv2.VideoCapture('C:\\Users\\Admin\\Pictures\\Camera Roll\\WIN_20190621_20_18_04_Pro.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    print(vidcap.get(cv2.CAP_PROP_POS_MSEC))
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image_3_"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 100.00 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    print("value of sec: ",sec)
    success = getFrame(sec)
    print("value of success: ",success)