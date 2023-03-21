import cv2 as cv
import mediapipe as mp
import pyautogui as pg

pg.FAILSAFE = False
video = cv.VideoCapture(0)
video.set(10,90)

screen_x,screen_y = pg.size()

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 1)
draw = mp.solutions.drawing_utils

while True:
    isTrue , frame = video.read()
    frame = cv.flip(frame,1)

    rgbFrame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    frameProcess = hands.process(rgbFrame)
    if(frameProcess.multi_hand_landmarks):
        for hand in frameProcess.multi_hand_landmarks:
            draw.draw_landmarks(frame,hand,mpHands.HAND_CONNECTIONS,connection_drawing_spec=draw.DrawingSpec(color = (255,0,0)),landmark_drawing_spec=draw.DrawingSpec(color = (0,0,0)))
            frame_x,frame_y,c = frame.shape
            for id,lm in enumerate(hand.landmark):
                if(id == 12):
                    cv.circle(frame,(int(lm.x*frame_y),int(lm.y*frame_x)),20,(0,255,255),3)
                    mouse_x = (screen_x/frame_y)*int(lm.x * frame_y)
                    mouse_y = (screen_y/frame_x)*int(lm.y * frame_x)
                    mouseCoordinate = (mouse_x,mouse_y)
                    pg.moveTo(mouseCoordinate)
                if(id == 4):
                    a = int(lm.x*frame_y)
                if(id == 2):
                    b = int(lm.x*frame_y)
                if(id == 8):
                    f = int(lm.y*frame_x)
                if(id == 7):
                    s = int(lm.y*frame_x)

            if((a-b) < 0):
                pg.rightClick()
            if((s-f) < 17):
                pg.leftClick()

    key = cv.waitKey(1)
    if(key == 27):
        break
    cv.imshow('webCam',frame)

video.release()
cv.destroyAllWindows()