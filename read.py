import cv2 as cv

# Ler imagem
img = cv.imread('Resources/Photos/cat.jpg')

# Mostrar imagem
cv.imshow('Cat', img)

# Espera um tempo indefinido para fechar a janela
# Quando a tecla '0' é pressionada, fecha a janela
cv.waitKey(0)