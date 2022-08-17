import cv2


def run():
    img = cv2.imread('../../imagenes/duff.png', -1)
    img_baw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    size = img.size
    height, width, channel = img.shape
    type = img.dtype
    print('Size: ' + str(size) + ' bytes')
    print('Height: ' + str(height) + ' pixels')
    print('Width: ' + str(width) + ' pixels')
    print('Channels: ' + str(channel))
    print('Type: ' + str(type))

    cv2.imshow('Cuadro', img)
    cv2.imshow('Cuadro (gris)', img_baw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
