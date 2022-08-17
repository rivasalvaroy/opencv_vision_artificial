import cv2
import numpy


def run():
    ancho = alto = 300
    img = numpy.ones((ancho, alto, 3), numpy.uint8)*255
    img[:] = (255, 255, 255)
    for x in range(ancho):
        for y in range(alto):
            if x % 50 == 0 or y % 50 == 0:
                img[x, y] = (0, 0, 255)
    cv2.imshow('Rejilla', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
