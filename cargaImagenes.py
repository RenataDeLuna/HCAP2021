import cv2
import numpy as np

#Cargas la imagen a color
IRGB=cv2.imread('003.jpg')
print(IRGB)
print(IRGB.shape)
print("Líneas agregadas en la rama2")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)

