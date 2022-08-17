import cv2


def run():
    img = cv2.imread('../../imagenes/figuras_geometricas.png', 1)
    img_blue, img_green, img_red = cv2.split(img)
    cv2.imshow('Original', img)
    cv2.imshow('Blue', img_blue)
    cv2.imshow('Green', img_green)
    cv2.imshow('Red', img_red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
