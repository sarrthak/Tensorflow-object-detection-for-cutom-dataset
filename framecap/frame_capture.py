import cv2
def FrameCapture(path):
    VidObj=cv2.VideoCapture(path)
    #cv2.CAP_PROP_FPS = 20
    VidObj.set(cv2.CAP_PROP_FPS,10.00)
    print(VidObj.get(cv2.CAP_PROP_FPS))
    """count=0
    success=1
    while success:
        success,image=VidObj.read()
        cv2.imwrite("frame%d.jpg" % count, image)
    """

FrameCapture("C:\\Users\\Admin\\Pictures\\Camera Roll\\WIN_20190621_16_12_05_Pro.mp4")