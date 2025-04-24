import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

""" Separação dos CANAIS DE CORES """
""" Onde há mais concentração daquela cor, mais CLARA será a imagem """
b,g,r = cv.split(img)

# # Imagens em escala cinza
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# Juntando os canais com uma imagem vazia, forçando a imagem original a ter três canais de cores
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# Imagens apenas com o canal desejado
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Propriedades das imagens
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Juntandos os canais de novo
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)