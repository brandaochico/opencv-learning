import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park', img)

# Translação
# -x --> Esquerda
# -y --> Cima
# x --> Direita
# y --> Baixo
def translate(img, x, y):
   transMatrix = np.float32([[1,0,x],[0,1,y]])
   dimensions = (img.shape[1], img.shape[0])

   return cv.warpAffine(img, transMatrix, dimensions)

translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

# Rotação
# rotPoint > 0 --> Antihorário
# rotPoint < 0 --> Horário
def rotate(img, angle, rotPoint=None):
    # height = img.shape[0] :: width = img.shape[1]
    (height, width) = img.shape[:2]

    # Se o PONTO DE ROTAÇÃO (rotPoint) não for informado, é setado como o centro da imagem
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Virar imagem
# -1 --> Verticalmente e horizontalmente
# 0 --> Verticalmente
# 1 --> Horizontalmente
flipped = cv.flip(img, 0)
cv.imshow('Flipped', flipped)

cv.waitKey(0)