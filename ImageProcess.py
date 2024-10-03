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
    
    # blur = cv2.GaussianBlur(gray,(5,5),0)
    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,13,4)

    cv2.imshow("Clipboard Image", th2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
