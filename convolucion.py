import numpy as np
import cv2
def convolucion(Ioriginal,Kernel):
    fr = len(Ioriginal) - (len(Kernel)-1)
    cr = len(Ioriginal[0]) - (len(Kernel[0])-1)
    Resultado = np.zeros((fr, cr),np.uint8)
    #For para recorrer las filas
    for i in range(len(Resultado)):
        #For para recorrer las columnas
        for j in range(len(Resultado[0])):
            suma = 0
            #Hace las multiplicaciones y la suma
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma += Kernel[m][n] * Ioriginal[m+i][n+j]
            if suma<=255:
                Resultado[i][j] =round(suma)
    return Resultado

#Generar artificialemente imágenes 
K = [[-1,0,1],[-1,0,1],[-1,0,1]]
I = [[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]

#Pasar las imágenes a np arrays
In = np.array(I) 
Kn = np.array(K)

IRGB=cv2.imread('003.jpg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#Mandar llamar a la función convolución
R = convolucion(IGS, Kn)

print(R)
print(R.shape)
cv2.imwrite('004C.jpg',R)
