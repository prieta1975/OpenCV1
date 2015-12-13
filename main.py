# Python with OPenCV Project 1
# Image

import numpy
import cv2

# Read an image
img = cv2.imread('C:\\Users\\Admin\\Desktop\\P1070543.JPG',0)

# Show image in a window
cv2.imshow('Ventana de imagen',img)

k = cv2.waitKey(0)

if k == ord('e'):
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('C:\\Users\\Admin\\Desktop\\P1070543_B.JPG',img)
    cv2.destroyAll_Windows()
