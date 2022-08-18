import cv2
import numpy

img = numpy.zeros((600, 600, 3), numpy.uint8)
img[:] = (255, 255, 255)

color = (0, 0, 255)
grosor = 2
fuente = cv2.FONT_HERSHEY_SIMPLEX
escala = 1

cv2.imshow('Eventos raton', img)


def eventos_raton(evento, x, y, flags, parametros):
    if evento == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, 'Click izquierdo', (x, y),
                    fuente, escala, color, grosor)
    elif evento == cv2.EVENT_RBUTTONDOWN:
        cv2.putText(img, 'Click derecho', (x, y),
                    fuente, escala, color, grosor)
    cv2.imshow('Eventos raton', img)


def run():
    cv2.setMouseCallback('Eventos raton', eventos_raton)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
