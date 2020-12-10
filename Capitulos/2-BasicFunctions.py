import cv2 as cv2
import numpy as np

img = cv2.imread("C:\\Users\\anton\\Documents\\OpenCV\\Resources\\lena.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# percent by which the image is resized
scale_percent = 25

# calculate the 50 percent of original dimensions
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

outputGray = cv2.resize(imgGray, dsize)
outputBlur = cv2.resize(imgBlur, dsize)
outputCanny = cv2.resize(imgCanny, dsize)
outputDilation= cv2.resize(imgDialation, dsize)
outputErode= cv2.resize(imgEroded, dsize)

cv2.imshow("Gray image", outputGray)
cv2.imshow("Blur image", outputBlur)
cv2.imshow("Canny image", outputCanny)
cv2.imshow("Dialation image", outputDilation)
cv2.imshow("Eroded image", outputErode)
cv2.waitKey(0)