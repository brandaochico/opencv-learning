import cv2 as cv
import numpy

# Dimensões: Largura, Altura e Canais de Cores
blank = numpy.zeros((500, 500, 3), dtype='uint8')

# 1. Pintando a imagem vazia de verde
# blank[intervalo y, intervalo x]
# Coordenada y é invertida
## blank[200:300, 300:400] = 0, 255, 0

## cv.imshow('Green', blank)

# 2. Criando um retângulo
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), 3)
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]), (0,255,0), cv.FILLED)

# 3. Criando um círculo
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), -1)

# 4. Criando uma linha
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), 3)

# 5. Escrevendo texto
cv.putText(blank, 'Hello, world!', (225,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)

cv.imshow('Rectangle', blank)

cv.waitKey(0)