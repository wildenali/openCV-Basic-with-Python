import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# Create a block image
img = np.zeros((512,512,3), np.uint8)

# Draw a rectangle blue, you need top-left corner and bottom-right corner of rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv2.imshow('hasilnya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()