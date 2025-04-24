import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# BGR -> Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR -> HSV (hue, saturation, value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR -> L*a*b* (lightness, [vermelho, verde], [azul, amarelo])
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR -> RGB
# Acontece uma inversão de cores pois (BGR = BLUE, GREEN, RED) e (RGB = RED, GREEN, BLUE)
# Portanto, as cores azuis e vermelhas são invertidas
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

""" Não é possível converter uma imagem em GRAYSCALE diretamente para HSV ou LAB
# O processo envolveria converter primeiro para BGR, e depois para o outro espaço desejado """

cv.waitKey(0)