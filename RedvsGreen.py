import numpy as np
import cv2

webcam = cv2.VideoCapture(0)


while True:
    _, imageFrame = webcam.read()



    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    

    kernal = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask)

    green_mask = cv2.dilate(green_mask, kernal)
    green_red = cv2.bitwise_and(imageFrame, imageFrame, mask = green_mask)

   


    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x,y), (x+w, y+h),(0, 0, 255), 2)

            cv2.putText(imageFrame, "nonveg", (x,y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))

    
    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x,y), (x+w, y+h),(0, 255, 0), 2)

            cv2.putText(imageFrame, "veg", (x,y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))


    

    cv2.imshow("Color Detection Window", imageFrame)
    if cv2.waitKey(0) & 0xFF -- ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
