import cv2
import numpy as np
#import video


def callback(*arg):
    print (arg)

cv2.namedWindow( "result" )

cap = cv2.VideoCapture(0)
# HSV фильтр для зеленых объектов из прошлого урока
hsv_min = np.array((0, 0, 240), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)

while True:
    flag, img = cap.read()
    # преобразуем RGB картинку в HSV модель
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    cv2.imshow('hsv', hsv) 
    # применяем цветовой фильтр
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    # вычисляем моменты изображения
    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    # будем реагировать только на те моменты,
    # которые содержать больше 100 пикселей
    print(dArea)
    if dArea > 10:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(img, (x, y), 10, (0,0,255), -1)

    cv2.imshow('Origin', img) 
    cv2.imshow('result', thresh) 
 
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()