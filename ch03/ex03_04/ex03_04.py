import cv2
import numpy


def run():
    # matriz = [[0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 0]]

    # img = numpy.array(matriz)
    # print(type(img))
    # print(img)

    img = numpy.zeros((5, 5, 3), numpy.uint8)
    print(type(img))
    print(img)
    # ancho = alto = 300
    # img = numpy.zeros((ancho, alto), numpy.uint8)
    cv2.imshow('Imagen negra', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
