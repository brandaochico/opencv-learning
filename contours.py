import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Borrando a imagem para diminuir o número de bordas
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Mostrando as bordas da imagem borrada
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Threshold é usado para converter uma imagem em escala de cinza para BINÁRIO
# Todos os pontos viram PRETO (0) ou BRANCO (1)
ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Contando os contornos achados com base nas bordas 
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# Desenhando os contornos
# drawContours necessita de uma imagem para desenhar por cima, de preferẽncia um quadro em branco
# -1 indica que todos os elementos da lista 'contours' serão utilizados
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)