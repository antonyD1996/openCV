import cv2
import numpy as np

img = cv2.imread("./Resources/chica.jpg")

imgHorizontal = np.hstack((img, img))
imgVertical = np.vstack((img, img))

cv2.imshow("Stack Horizontal", imgHorizontal)
cv2.imshow("Stack Vertical", imgVertical)

cv2.waitKey(0)