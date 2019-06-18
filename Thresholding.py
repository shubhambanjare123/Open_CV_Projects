import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('book_page2.jpg')

retval,threshold = cv2.threshold(img,70,255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold2 = cv2.threshold(grayscaled,70,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,155,1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
