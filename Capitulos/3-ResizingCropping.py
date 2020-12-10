import cv2

img = cv2.imread("./Resources/cat.jpg")

print(img.shape)

imgResize = cv2.resize(img, (300, 200))

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)