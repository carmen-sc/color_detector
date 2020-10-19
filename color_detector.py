#!/usr/bin/env python3
import cv2
import numpy as np
from time import sleep

N_SPLITS = 20
width = 640
height = 480
seg_height = int(height/N_SPLITS)
out_array = np.zeros(((N_SPLITS-1), 3))

cap = cv2.VideoCapture(2)

def Dominant_Color(n_r, n_y, n_w, n_b):
    if n_r > n_y and n_r > n_w and n_r > n_b:
        return "red"

    if n_y > n_r and n_y > n_w and n_y > n_b:
        return "yellow"

    if n_w > n_y and n_w > n_r and n_w > n_b:
        return "white"

    if n_b > n_y and n_b > n_w and n_b > n_r:
        return "black"

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # convert frame to HSV
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Set range for red color 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 

    # Set range for yellow color 
    yellow_lower = np.array([10, 87, 111], np.uint8) 
    yellow_upper = np.array([40, 255, 255], np.uint8) 

    # Set range for white
    white_lower = np.array([0, 0, 150], np.uint8) 
    white_upper = np.array([179, 110, 255], np.uint8) 

    # Set range for black 
    black_lower = np.array([0, 111, 0], np.uint8) 
    black_upper = np.array([179, 255, 50], np.uint8) 

    print("Dominant color of red, yellow, white, or black")
    
    #split image into N_SPLITS horizontal segments
    for i in range(0, (N_SPLITS-1)):
        
        seg = frame[(seg_height*i):(seg_height*(i+1)), : , :]

        # define masks and count colored pixels
        red_mask = cv2.inRange(seg, red_lower, red_upper) 
        n_red_pix = np.sum(red_mask == 255)

        yellow_mask = cv2.inRange(seg, yellow_lower, yellow_upper)
        n_yellow_pix = np.sum(yellow_mask == 255)

        white_mask = cv2.inRange(seg, white_lower, white_upper) 
        n_white_pix = np.sum(white_mask == 255)

        black_mask = cv2.inRange(seg, black_lower, black_upper) 
        n_black_pix = np.sum(black_mask == 255)
        
        print(Dominant_Color(n_red_pix, n_yellow_pix, n_white_pix, n_black_pix))
 


        

    print('\n')

    sleep(1)
