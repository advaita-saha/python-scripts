import cv2 
import mediapipe as mp
import pyautogui as pd 


face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()

    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame, (frame_width, frame_height))

    
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    output = face_mesh.process(new_frame)
    landmarks_points = output.multi_face_landmarks

    
    if landmarks_points:
        landmarks = landmarks_points[0].landmark

        
        x = int(landmarks[1].x * frame_width)
        y = int(landmarks[1].y * frame_height)
        if y < 200:
            pd.press("up")
        elif y>250:
            pd.press("down")
        if x > 320:
            pd.press("right")
           
          
        elif x < 180:
            
            pd.press("left")
            
           
           

  
    cv2.imshow("face", frame)

   
    if cv2.waitKey(2) & 0xFF == ord("d"):
        break


cap.release()
cv2.destroyAllWindows()
