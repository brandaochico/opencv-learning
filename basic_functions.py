import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converter para cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Borrar imagem
# Kernel size tem que ser um número ÍMPAR
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT) 
cv.imshow('Blur', blur)

# Mostrar bordas
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)

# Dilatar a imagem / deixar mais grossa
# Utilizando as bordas
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Erodir a imagem (contrário de dilatar)
# Utilizando a imagem dilatada tentando retornar às bordas originais
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Alterar o tamanho
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cortar imagem
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)