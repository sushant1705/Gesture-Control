import cv2 as cv
import mediapipe as mp
import pyautogui as gui

capture= cv.VideoCapture(0)
mp_hands = mp.solutions.hands.Hands()
mp_hand = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
x1=x2=y1=y2=0
while True:
    isTrue, image = capture.read()
    frame_height,frame_width,_ = image.shape
    image = cv.cvtColor(cv.flip(image,1),cv.COLOR_BGR2RGB)
    result = mp_hands.process(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    hands = result.multi_hand_landmarks
    
    if hands:
        for hand_landmarks in hands:
            # Draw dots and lines on hand
            # drawing_utils.draw_landmarks(image,hand_landmarks,mp_hand.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style())
            landmarks = hand_landmarks.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv.circle(img=image, center=(x,y),radius=5, color=(0,255,255),thickness=2)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv.circle(img=image, center=(x,y),radius=5, color=(0,255,255),thickness=2)
                    x2 = x
                    y2 = y
        distance = ((x2-x1)**2  + (y2-y1)**2 )**(0.5)//2
        cv.line(image, (x1,y1), (x2,y2), (50,50,50), thickness=2)
        if distance > 50:
            gui.press("volumeup")
        else:
            gui.press("volumedown")
    cv.imshow('Hand Tracker', image)
    if cv.waitKey(10)==13:                
        break
    
