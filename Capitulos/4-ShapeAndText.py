import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# Formas
# print(img.shape)
# img[200:300, 100:300] = 255, 0, 0 #colorear la imagen de azul

# LIneas
cv2.line(img, (0, 100), (300, 300), (0, 250, 0), 3)
# Especificando un punto dentro del cuadro
cv2.line(img, (300, 300), (400, 0), (0, 50, 250), 3)
# desde el origen hasta el limiete de la imagen
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (200, 0, 50), 3)
#crea un rectangulo lleno
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
#crear un circulo
cv2.circle(img, (400,100), 50, (255, 255, 0), 3)
#poner texto en las imagenes
cv2.putText(img, " OpenCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX,1,(255,150,0),2)

cv2.imshow("Image", img)


cv2.waitKey(0)
