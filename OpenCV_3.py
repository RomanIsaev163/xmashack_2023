import cv2
import numpy as np

    
cv2.namedWindow( "result" ) # создаем главное окно
cap = cv2.VideoCapture(0)
crange = [0,0,0, 0,0,0]

color_red=(0,0,255)
color_blue=(255,0,0)
try:
    while True:
        flag, img = cap.read()
        height,widht=img.shape[:2]
        Centr_X=int(widht/2)
        Centr_Y=int(height/2)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        
        # формируем начальный и конечный цвет фильтра
        h_min = np.array((66, 164, 156), np.uint8)
        h_max = np.array((86, 255, 252), np.uint8)

        # накладываем фильтр на кадр в модели HSV
        thresh = cv2.inRange(hsv, h_min, h_max)
        
        moments=cv2.moments(thresh,1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        
        if dArea>100:
            x=int(dM10 / dArea)
            y=int(dM01 / dArea)
            
            cv2.circle(img,(x,y),5,color_blue,2)
            cv2.putText(img,"x%d;y%d" % (x,y),(x+10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,color_blue,2)
            
            cv2.circle(img,(Centr_X,Centr_Y),5,color_red,2)
            cv2.putText(img,"x%d;y%d" % (Centr_X-x,Centr_Y-y),(Centr_X+10,Centr_Y-10),cv2.FONT_HERSHEY_SIMPLEX,1,color_red,2)
            
            cv2.line(img,(x,y),(Centr_X,Centr_Y),color_blue,2)
    
        cv2.imshow('Origin',img)
        cv2.imshow('result', thresh)
        
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    

except KeyboardInterrupt:
    print(' Exit pressed Ctrl+C')
    cv2.destroyAllWindows() 
