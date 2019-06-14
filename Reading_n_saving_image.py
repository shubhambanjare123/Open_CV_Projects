import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(img, cmap ='gray',interpolation='bicubic')
##plt.plot([500,1250],[200,800],'c',linewidth=1)
##plt.show()

cv2.imwrite('1.png',img)






