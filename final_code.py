import cv2
import numpy as np
import time
import serial
ser1=serial.Serial('COM10',9600)


#LED controll
ser1.write('b'.encode())
ser1.write('d'.encode())
ser1.write('f'.encode())
ser1.write('h'.encode())
ser1.write('j'.encode())

def ORB_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of ORB matches between them
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

    # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
    orb = cv2.ORB_create(1000, 1.2)

    # Detect keypoints of original image
    (kp1, des1) = orb.detectAndCompute(image1, None)

    # Detect keypoints of rotated image
    (kp2, des2) = orb.detectAndCompute(image_template, None)

    # Create matcher 
    # Note we're no longer using Flannbased matching
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
    # Do matching
    matches = bf.match(des1,des2)

    # Sort the matches based on distance.  Least distance
    # is better
    matches = sorted(matches, key=lambda val: val.distance)
    return len(matches)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

# Load our image template, this is our reference image
image_template1 = cv2.imread('get_1.jpg', 0) 
image_template2 = cv2.imread('get_2.jpg', 0)  
image_template3 = cv2.imread('get_3_.jpg', 0) 
image_template4 = cv2.imread('get_4.jpg', 0) 
image_template5 = cv2.imread('get_5.jpg', 0) 
# image_template = cv2.imread('images/kitkat.jpg', 0) 


# FIRST STEP 

while True:
    # Get webcam images
    ret, frame = cap.read()

    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    top_left_x = int(0.3*(int((width / 7) * 6)))
    top_left_y = int(0.55*(int((height / 3) + (height / 6))))
    bottom_right_x = int(0.5*(int((width / 7) * 6)))
    bottom_right_y = int(0.3*(int((height / 3) - (height / 6))))

    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    # Crop window of observation we defined above
    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    # Flip frame orientation horizontally
    #frame = cv2.flip(frame,1)

    # Get number of ORB matches 
    matches1 = ORB_detector(cropped, image_template1)
    

    # Display status string showing the current no. of matches 
    output_string = "Matches = " + str(matches1)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 1, (250,0,150), 2)

    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 350 is essentially a min 35% match
    if matches1 < 270:
        cv2.putText(frame,'Proceed 1st step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('a'.encode())
    # If matches exceed our threshold then object has been detected
    if matches1 > 270:
        cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(frame,'Proceed 2nd step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('b'.encode())
        time.sleep(2)
        break

    cv2.imshow('Object Detector using ORB', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

# SECOND STEP  
        
while True:
    
    ret, frame = cap.read()

    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    top_left_x = int(0.57*(int((width / 7) * 6)))
    top_left_y = int(0.55*(int((height / 3) + (height / 6))))
    bottom_right_x = int(0.68*(int((width / 7) * 6)))
    bottom_right_y = int(0.3*(int((height / 3) - (height / 6))))

    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    # Crop window of observation we defined above
    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    # Flip frame orientation horizontally
    #frame = cv2.flip(frame,1)

    # Get number of ORB matches 
    matches2 = ORB_detector(cropped, image_template2)
    

    # Display status string showing the current no. of matches 
    output_string = "Matches = " + str(matches2)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 1, (250,0,150), 2)

    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 350 is essentially a min 35% match
    if matches2 < 140:
        cv2.putText(frame,'Proceed 2nd step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('c'.encode())
    # If matches exceed our threshold then object has been detected
    if matches2 > 140:
        cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(frame,'Proceed 3rd step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('d'.encode())
        time.sleep(2)
        break;


    cv2.imshow('Object Detector using ORB', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

# THIRD Step
        
while True:
    
    ret, frame = cap.read()

    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    top_left_x = int(0.73*(int((width / 7) * 6)))
    top_left_y = int(0.55*(int((height / 3) + (height / 6))))
    bottom_right_x = int(0.93*(int((width / 7) * 6)))
    bottom_right_y = int(0.3*(int((height / 3) - (height / 6))))

    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    # Crop window of observation we defined above
    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    # Flip frame orientation horizontally
    #frame = cv2.flip(frame,1)

    # Get number of ORB matches 
    matches3 = ORB_detector(cropped, image_template3)
    

    # Display status string showing the current no. of matches 
    output_string = "Matches = " + str(matches3)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 1, (250,0,150), 2)

    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 350 is essentially a min 35% match
    if matches3 < 155:
        cv2.putText(frame,'Proceed 3rd step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('e'.encode())
    # If matches exceed our threshold then object has been detected
    if matches3 > 155:
        cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(frame,'Proceed 4th step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('f'.encode())
        time.sleep(2)
        break;

    cv2.imshow('Object Detector using ORB', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
   
# FOURTH STEP
        
while True:
    
    ret, frame = cap.read()

    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    top_left_x = int(0.72*(int((width / 7) * 6)))
    top_left_y = int(1.1*(int((height / 3) + (height / 6))))
    bottom_right_x = int(0.85*(int((width / 7) * 6)))
    bottom_right_y = int(1.90*(int((height / 3) - (height / 6))))

    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    # Crop window of observation we defined above
    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    # Flip frame orientation horizontally
    #frame = cv2.flip(frame,1)

    # Get number of ORB matches 
    matches4 = ORB_detector(cropped, image_template4)
    

    # Display status string showing the current no. of matches 
    output_string = "Matches = " + str(matches4)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 1, (250,0,150), 2)

    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 350 is essentially a min 35% match
    if matches4 < 60:
        cv2.putText(frame,'Proceed 4th step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('g'.encode())
    # If matches exceed our threshold then object has been detected
    if matches4 > 60:
        cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(frame,'Proceed 5th step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('h'.encode())
        time.sleep(2)
        break;

    cv2.imshow('Object Detector using ORB', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

# FIFTH STEP
        
while True:
    
    ret, frame = cap.read()

    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    top_left_x = int(0.37*(int((width / 7) * 6)))
    top_left_y = int(1.83*(int((height / 3) + (height / 6))))
    bottom_right_x = int(0.85*(int((width / 7) * 6)))
    bottom_right_y = int(1.33*(int((height / 3) + (height / 6))))

    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    # Crop window of observation we defined above
    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    # Flip frame orientation horizontally
    #frame = cv2.flip(frame,1)

    # Get number of ORB matches 
    matches5 = ORB_detector(cropped, image_template5)
    

    # Display status string showing the current no. of matches 
    output_string = "Matches = " + str(matches5)
    cv2.putText(frame, output_string, (50,450), cv2.FONT_HERSHEY_COMPLEX, 1, (250,0,150), 2)

    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 350 is essentially a min 35% match
    if matches5 < 400:
        cv2.putText(frame,'Proceed 5th step',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('i'.encode())
    # If matches exceed our threshold then object has been detected
    if matches5 > 400:
        cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(frame,'Finished',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
        ser1.write('j'.encode())
        time.sleep(5)
        break

    cv2.imshow('Object Detector using ORB', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()