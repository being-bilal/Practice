import cv2 as cv  
import numpy as np
import matplotlib.pyplot as plt

# Reads into the image (as a colored image)
img = cv.imread("python/opencv/images/lake.jpg", cv.IMREAD_COLOR)
#cv.imshow('original image', img)


# prints the RGB value of each of the pixel of the imge
print(img) # **Open CV stores the images in BGR format and not RGB**

# gives the dimensions of the file [length, width, chanel]
img_shape = img.shape
print(img_shape)

#Spliting the image in GBR components
b, g, r = cv.split(img)

#merging all the color components back
merged_image = cv.merge((b,g,r))
#cv.imshow('merged image', merged_image)

# converting from one color space to another (bgr to hsv)
hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV) #hsv stands for hue, saturation, and value

h,s,v = cv.split(hsv_image)
h_new = h + 20 #modifying the hue value
hsv_image = cv.merge((h_new, s, v)) #merging the new hsv chanels
modified_img = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR) #converting back to rgb with new hue value


"""
cv.imshow("modified image", modified_img)
cv.imshow('original image', img)
cv.waitKey(0)
"""
