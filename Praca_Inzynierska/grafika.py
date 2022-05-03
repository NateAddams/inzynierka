import cv2
import numpy as np
from random import randint

x, y = 21, 21
img = np.zeros((x*10, y*10, 3), dtype='uint8')


for i in range(x):
    for j in range(y):
        contours = np.array([[i*10, j*10], [i*10, (j*10)+9], [(i*10)+9, (j*10)+9], [(i*10)+9, j*10]])
        cv2.fillPoly(img, pts=[contours], color=(randint(0, 255), randint(0, 255), randint(0, 255)))

cv2.imwrite("zdjecia/test7.png", img)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
