
import cv2
import numpy as np

# https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/

'''
The Hough Transform is a method that is used in image processing to detect any shape,
if that shape can be represented in mathematical form. It can detect the shape even if it is broken or distorted a little bit.

We will see how Hough transform works for line detection using the HoughLine transform method.
To apply the Houghline method, first an edge detection of the specific image is desirable.
For the edge detection technique go through the article Edge detection
'''

# Reading image from folder where it is stored
img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/linesDetected.png')


# Convert the img to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
# Apply edge detection method on the image
edges = cv2.Canny(gray,50,150,apertureSize = 3)
  
# This returns an array of r and theta values
lines = cv2.HoughLines(edges,1,np.pi/180, 200)
  
# The below for loop runs till r and theta values 
# are in the range of the 2d array
for r, theta in lines[0]:
    # Stores the value of cos(theta) in a
    a = np.cos(theta)

    # Stores the value of sin(theta) in b
    b = np.sin(theta)

    # x0 stores the value rcos(theta)
    x0 = a*r

    # y0 stores the value rsin(theta)
    y0 = b*r

    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 1000*(-b))

    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 1000*(a))

    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 1000*(-b))

    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 1000*(a))

    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0,0,255) denotes the colour of the line to be 
    #drawn. In this case, it is red. 
    cv2.line(img,(x1,y1), (x2,y2), (255,0,0),2)
      
# All the changes made in the input image are finally
# written on a new image houghlines.jpg
# cv2.imwrite('linesDetected.jpg', img)

cv2.imshow("linesDetected", img)

cv2.waitKey(0)
cv2.destroyAllWindows()