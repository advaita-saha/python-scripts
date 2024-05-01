import mediapipe as mp
import pyautogui as pd
import cv2
height = 480
width = 640




dix =1920
diy =1080
cap = cv2.VideoCapture(0)

while True:
    state , frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(640,480))
    

    
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    with mp.solutions.hands.Hands(max_num_hands = 1,min_detection_confidence=0.3) as hands:
        results = hands.process(new_frame)

    if results.multi_hand_landmarks:
        for handmarker in results. multi_hand_landmarks:
          landmarks = handmarker.landmark[8]

          x =int(landmarks.x * 1980)
          y =int(landmarks.y * 1100)
          z = int(landmarks.z * 100)
          if y <400:
              pd.scroll(5)

          if y >590:
              pd.scroll(-5)

        


        
    cv2.imshow("frame",frame)

    if cv2.waitKey(2) & 0xFF == ord("d"):
        break
cv2.destroyAllWindows()