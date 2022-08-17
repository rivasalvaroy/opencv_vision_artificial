import cv2


def run():
    img = cv2.imread('../../imagenes/cuadro.jpg', 1)

    color = (0, 0, 255)
    grosor = 4
    fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    escala = 2

    cv2.arrowedLine(img, (200, 100), (300, 150), color, grosor)
    cv2.putText(img, 'Isabel', (100, 75), fuente, escala, color, grosor)

    cv2.imshow('cuadro', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
