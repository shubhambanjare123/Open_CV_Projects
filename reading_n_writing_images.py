import cv2
import numpy as np
import matplotlib.pyplot as plt
x = cv2.imread('1.jpg',0)
plt.imshow(x,cmap = 'gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
