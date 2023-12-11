# import modules 
import time
import numpy as np
import cv2
import pytesseract as tes


cam = cv2.VideoCapture(0)
start = time.time()
buffer = start
keep = None

# shows camera for 3 seconds with a countdown, at the end of countdown takes a picture to analyze
wait = True
while wait == True:
    # reads the camera
    ret, frame = cam.read()
    
    #keeps track of time
    laptime = round((time.time()-start), 2)
    
    #  when it reaches 3 seconds stop displaying number because we don't want it in the final image
    if laptime <= 3:
        cv2.putText(frame, str(laptime), (500, 400), cv2.FONT_HERSHEY_COMPLEX,5,(255, 50, 50), 4)
    
    # slight buffer at 3.1 to give time for text to go away
    if 3.1-laptime <= 0:
        keep = frame
        wait = False
    

    
    cv2.imshow('hi', frame)
    

    if cv2.waitKey(10) & 0xFF == ord('q'):
        r = frame
        break


while wait == False:
    bw = cv2.cvtColor(keep, cv2.COLOR_BGR2GRAY)
    h, w = bw.shape

    img_text = tes.image_to_string(bw)
    print(img_text)

    boxes = tes.image_to_boxes(bw)
    for box in boxes.splitlines():
        box = box.split(' ')
        fr = cv2.rectangle(bw, (int(box[1]), h - int(box[2])), (int(box[3]), h - int(box[4])), (0, 255, 0), 2)
    cv2.imshow('hello', fr)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break