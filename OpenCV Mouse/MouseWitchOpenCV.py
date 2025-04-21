import cv2
import mediapipe as mp
import pyautogui as pag

VideoCapture = cv2.VideoCapture(0)
VideoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
VideoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

screen_w, screen_h = pag.size()
pinch_active = False

while True:
    success, frame = VideoCapture.read()

    if success:
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                h, w, _ = frame.shape

                index_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]

                index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
                thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)

                distance = ((index_x - thumb_x)**2 + (index_y - thumb_y)**2) ** 0.5

                if distance >= 50:
                    screen_x = int(index_tip.x * screen_w)
                    screen_y = int(index_tip.y * screen_h)
                    pag.moveTo(screen_x, screen_y)

                if distance < 50 and not pinch_active:
                    pag.click()
                    pinch_active = True
                elif distance >= 50 and pinch_active:
                    pinch_active = False

        cv2.imshow("video", frame)

        if cv2.waitKey(1) == ord('e'):
            break

cv2.destroyAllWindows()
