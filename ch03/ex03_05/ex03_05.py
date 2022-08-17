import cv2
import numpy


def run():
    ancho = alto = 300
    img = numpy.ones((ancho, alto), numpy.uint8)*255
    print(img)
    cv2.imshow('Imagen blanca', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
