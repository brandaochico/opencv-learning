
import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Alterar a escala de uma imagem
def rescaleFrame(frame, scale=0.75):
    # Propriedades convertidas para INTEGER porque sempre serão números inteiros

    # Largura = frame.shape[1]
    width = int(frame.shape[1] * scale) 

    # Altura = frame.shape[0]
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    
    # Altera a escala da imagem conforme os valores passados na variável 'dimensions' (tuple) 
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resizedImg = rescaleFrame(img)

cv.imshow('Cat Resized', resizedImg)

cv.waitKey(0)