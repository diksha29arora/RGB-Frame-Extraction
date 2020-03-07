import cv2 as cv
import numpy as np

img = cv.imread('rgb.jpg')

b = img[ : , : , : 1]
g = img[ : , : ,1: 2]
r = img[ : , : ,2 : ]

cv.imwrite("Blue.jpg",b)
cv.imwrite("Green.jpg",g)
cv.imwrite("Red.jpg",r)