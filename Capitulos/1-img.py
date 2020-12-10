# Lectura de imagenes, videos y webcams

import cv2

img = cv2.imread("C:\\Users\\anton\\Documents\\OpenCV\\Resources\\lena.jpg")
# percent by which the image is resized
scale_percent = 25

# calculate the 50 percent of original dimensions
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

output = cv2.resize(img, dsize)

cv2.imshow("Output", output)
cv2.waitKey(0)