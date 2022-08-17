import cv2


def run():
    img = cv2.imread('../../imagenes/cuadro.jpg', 1)
    img_baw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Cuadro', img)
    cv2.imshow('Cuadro (gris)', img_baw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
