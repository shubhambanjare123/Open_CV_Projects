import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg',cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55] = [255,255,255]

#roi = img[150:300,150:300] = [255,255,255]

mountain = img[150:300,150:350]
img[:150,:200] = mountain

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

