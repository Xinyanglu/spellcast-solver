import subprocess
from io import BytesIO

import cv2
import numpy as np
import pytesseract
from PIL import Image


def getImageFromClipboard():
    # Use xclip to get image data from the clipboard
    try:
        imgData = subprocess.check_output(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-o'])

        img = Image.open(BytesIO(imgData))
        img = np.array(img)

        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    except subprocess.CalledProcessError:
        print("No image found in clipboard.")
        return None

def findBoard(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (250,250))
    
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,33,10)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    lowerBound = 5 * 10
    upperBound = 30 * 30

    letters = []
    for contour in contours:
        # Get bounding box around contour
        area = cv2.contourArea(contour)
        if area < lowerBound or area > upperBound:
            continue
        x, y, w, h = cv2.boundingRect(contour)

        if(gray[y-1][x-1] < 230): #top left corner of contour isn't white
            continue

        # Crop the region containing the letter
        letter_image = gray[y:y+h, x:x+w]

        # Apply OCR to the cropped letter
        text = pytesseract.image_to_string(letter_image, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 10') 
        if text.strip() == '' or len(text.strip()) > 1: # the contour around certain letters such as 'I' is too close, increase the contour box and retry
            letter_image = gray[y-3:y+h+3, x-3:x+w+3]
            text = pytesseract.image_to_string(letter_image, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ -l eng --psm 13') 

        letters.append((x,y,text.strip()))

    letters = sorted(letters, key= lambda x: x[0]/5 + x[1]) # sort by Y first, then by X. Divide 5 for 5 elements per row

    letters = [x[2] for x in letters]

    return np.reshape(letters, (5,5))


def printBoard(board):
    row = ""
    for i in range(5):
        for j in range(5):
            row += board[j][i] + " "
        print(row)
        row = ""


