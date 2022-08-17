import cv2


def run():
    img = cv2.imread('../../imagenes/cuadro.jpg', 1)

    color = (0, 0, 255)
    grosor = 2
    cara_x1, cara_x2 = 300, 550
    cara_y1, cara_y2 = 20, 220
    cv2.rectangle(img, (cara_x1, cara_y1), (cara_x2, cara_y2), color, grosor)

    cv2.imshow('Cuadro', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
