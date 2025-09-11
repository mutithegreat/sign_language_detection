import os
import pickle
import mediapipe as mp
import cv2
#import json

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True , min_detection_confidence=0.3)
dir_data = "data"

data = list()
labels = list()

for dir_ in os.listdir(dir_data):
    for image_path in os.listdir(os.path.join(dir_data , dir_)):
        data_aux = list()
        x_ = list()
        y_ = list()
        img = cv2.imread(os.path.join(dir_data , dir_ , image_path))
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)
                    
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
            if len(data_aux) == 42:
                data.append(data_aux)
                labels.append(dir_)
                

f = open("data.pickle" , "wb")
pickle.dump({"data" : data , "labels" : labels} , f)
f.close()

"""with open("data.json" , "w" , encoding="utf-8") as f:
    json.dump({"data" : data , "labels" : labels} , f , ensure_ascii=False , indent=4)
"""    