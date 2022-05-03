import cv2
import numpy as np

i = 0
j = 0

x = 10
y = 10

#img = np.zeros((512,512,3))
img = np.zeros((x*10, y*10, 3), dtype='uint8')

hex = np.array([[i+5, j],[i, j+5], [i, j+10],[i+5, j+15], [i+10, j+10],[i+10, j+5]],np.int32)

hex2 = np.array([[i+10, j+10],[i+5, j+15], [i+5, j+20], [i+10, j+25], [i+15, j+20], [i+15, j+15]],np.int32)

cv2.polylines(img,[hex],True,(255,255,255))
cv2.polylines(img,[hex2],True,(0,255,255))

cv2.imshow("Polygon", img) # Display the Hexagon
cv2.waitKey(0)
cv2.destroyAllWindows()
