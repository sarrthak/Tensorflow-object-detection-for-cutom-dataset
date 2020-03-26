import cv2
import os

#FPS = 2.00
#playing video from file:
cap=cv2.VideoCapture("C:\\Users\\Admin\\Pictures\\Camera Roll\\WIN_20190623_17_30_25_Pro.mp4")

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0
while(True):
    #capture frame-by-frame
    ret, frame = cap.read()
    if not ret: break
        #if no ret then break the loop
        #saves image of the current frame in jpg file
        
    name = './data/WIN_20190623_' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cap.set(cv2.CAP_PROP_POS_FRAMES,currentFrame)
    print("printing value of current frame: ",cap.get(cv2.CAP_PROP_POS_FRAMES)) 
    frm=cap.get(cv2.CAP_PROP_POS_FRAMES)
    cv2.imwrite(name,frame)
    cv2.waitKey(1000)
    print("the value of frm is: ",frm)
    if frm==1000:
        exit()
    #To stop duplicate images
    currentFrame +=5

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()    