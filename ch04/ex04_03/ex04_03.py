import cv2


def run():
    img = cv2.imread('../../imagenes/cuadro.jpg', 1)
    cv2.arrowedLine(img, (200, 100), (300, 150), (0, 0, 255), 4)
    cv2.imshow('Cuadro', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
