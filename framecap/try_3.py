import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1


print("aba")
a = argparse.ArgumentParser()
a.add_argument("--pathIn", help="C:\\Users\\Admin\\Pictures\\Camera Roll\\WIN_20190620_19_50_11_Pro.mp4")
a.add_argument("--pathOut", help="F:\\Internship\\Nokia_work\\framecap\\data")
args = a.parse_args()
print(args)
extractImages(args.pathIn, args.pathOut)