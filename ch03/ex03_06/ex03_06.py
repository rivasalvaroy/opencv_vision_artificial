import cv2
import numpy


def run():
    ancho = 5
    alto = 7
    # ancho = alto = 300
    img_azul = numpy.ones((ancho, alto, 3), numpy.uint8)*255
    img_azul[:] = (255, 0, 0)
    print(type(img_azul))
    print(img_azul)

    img_verde = numpy.ones((ancho, alto, 3), numpy.uint8)*255
    img_verde[:] = (0, 255, 0)

    img_rojo = numpy.ones((ancho, alto, 3), numpy.uint8)*255
    img_rojo[:] = (0, 0, 255)

    cv2.imshow('Imagen azul', img_azul)
    cv2.imshow('Imagen verde', img_verde)
    cv2.imshow('Imagen rojo', img_rojo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
