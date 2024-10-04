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
    
    # blur = cv2.GaussianBlur(gray,(3,3),0)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,33,10)
    
    # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 10))
    # threshed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, rect_kernel)

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
        letter_image = thresh[y:y+h, x:x+w]

        # Apply OCR to the cropped letter
        text = pytesseract.image_to_string(letter_image, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 10 preserve_interword_spaces=1')  # '--psm 10' treats it as a single character
        if text.strip() == '' or len(text.strip()) > 1: # the contour around certain letters such as 'I' is too close, increase the contour box and retry
            letter_image = thresh[y-2:y+h+2, x-2:x+w+2]
            text = pytesseract.image_to_string(letter_image, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 7 preserve_interword_spaces=1')  # '--psm 10' treats it as a single character

        letters.append((x,y,text.strip()))

        # Optional: Draw bounding box on original image for debugging
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

    print(letters)

    cv2.imshow("Clipboard Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
