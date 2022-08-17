import cv2


def run():
    img = cv2.imread('../../imagenes/cuadro.jpg', 1)

    cv2.namedWindow('Cuadro', cv2.WINDOW_NORMAL)
    cv2.moveWindow('Cuadro', 0, 0)
    cv2.imshow('Cuadro', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
