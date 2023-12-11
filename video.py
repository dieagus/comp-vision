# import modules
import numpy as np
import cv2
import pytesseract as tes


# cam is video camera capture
cam = cv2.VideoCapture(0)

custom_config = r'--oem 3 --psm 6 outputbase digits'

# continuously running reading camera
while True:
    
    # ret is a t/f bool if a frame is captured
    # frame is the data of the frame
    ret, frame = cam.read()

    # converts frame to black & white
    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # height width color
    h, w = bw.shape
    boxes = tes.image_to_boxes(bw) #config = custom_config

    #img_text = tes.image_to_string(bw)
    
    # creates box around the letters

    for box in boxes.splitlines():
        box = box.split(' ')
        frame = cv2.rectangle(frame, (int(box[1]), h - int(box[2])), (int(box[3]), h - int(box[4])), (0, 255, 0), 2)
    
    #print(tes.image_to_string(bw, config=custom_config))
    
    #print(img_text)
    # shows frame 
    cv2.imshow("hi", frame)
    
    # quit command 
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        