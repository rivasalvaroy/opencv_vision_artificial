import cv2
import numpy


def run():
    ancho = 5
    alto = 7
    # ancho = alto = 300
    img = numpy.ones((ancho, alto), numpy.uint8)*255
    print(img)
    for x in range(ancho):
        for y in range(alto):
            if x % 2 == 0 or y % 2 == 0:
                img[x, y] = 0
    print(img)
    cv2.imshow('Rejilla', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
