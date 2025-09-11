import os
import cv2

class_size = 3
data_size = 100

cap = cv2.VideoCapture(0)

for file in range(class_size):
    if not os.path.exists(os.path.join("/data",str(file))):
        os.makedirs(os.path.join("/data" , str(file)))
    
    while True:
        _ , frame = cap.read()
        cv2.putText(frame , "Başlatmak için q'ya bas" , (100,50) , cv2.FONT_HERSHEY_PLAIN , 1.25 , (0,0,255) , 3)
        cv2.imshow("frame" , frame)
        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    
    counter = 0
    
    while counter < data_size:
        _ , frame = cap.read()
        cv2.imshow("frame",frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join("/data" , str(file) , "{}.jpg".format(counter)) , frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
        
