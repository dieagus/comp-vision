# comp-vision
Program essentially uses pytesseract to detect objects in the camera

# detection.py
Program records camera and takes a single picture in 3 seconds from start of program. Once picture is taken, the program runs a pytesseract model on it to find characters in the image. 
The program boxes the characters and prints it to the screen. Program is also supposed to convert the picture to text, or find any text in the image, but doesn't seem to work unless the text is very big.

# video.py
Video.py was the first program I created because I originally wanted a program that used the frames from the camera and detected objcets live as the camera updated. 
I think it was too much being ran for 60 pictures per second
