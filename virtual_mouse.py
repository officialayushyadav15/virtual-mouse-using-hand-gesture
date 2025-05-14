import cv2
import mediapipe as mp
import util
import pyautogui
from pynput.mouse import Button, Controller
import random

mouse = Controller()

screen_width, screen_height = pyautogui.size()

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.7,  #minimum code required for hand to be valid is 0.7
    min_tracking_confidence = 0.7,
    max_num_hands = 1
)

def find_finger_tip(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
        return hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
    
    return None

def move_mouse(index_finger_tip):
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width) # since we get values ranged from 0 to 1 hence we multiplu it by screen width so that movement is easy and can be traced so that system know what used is asking for him to do so we multiply x axis with screen wisth and y axis with screen height
        y = int(index_finger_tip.y * screen_height)

        pyautogui.moveTo(x,y)

def is_left_click(landmarks_list, thumb_index_dist):
    return(util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) > 90 and thumb_index_dist > 50 and util.get_angle(landmarks_list[13], landmarks_list[14], landmarks_list[16]) < 50 and util.get_angle(landmarks_list[17], landmarks_list[18], landmarks_list[20]) < 50) 

def is_right_click(landmarks_list, thumb_index_dist):
    return(util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90 and util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and thumb_index_dist > 50 and util.get_angle(landmarks_list[13], landmarks_list[14], landmarks_list[16]) < 50 and util.get_angle(landmarks_list[17], landmarks_list[18], landmarks_list[20]) < 50) 

def is_double_click(landmarks_list, thumb_index_dist):
    return(util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and util.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and thumb_index_dist > 50 and util.get_angle(landmarks_list[13], landmarks_list[14], landmarks_list[16]) < 50 and util.get_angle(landmarks_list[17], landmarks_list[18], landmarks_list[20]) < 50) 

def is_screenshot(landmarks_list, thumb_index_dist):
    return(thumb_index_dist > 50 and util.get_distance([landmarks_list[8] ,landmarks_list[5]]) > 50 and util.get_distance([landmarks_list[16] ,landmarks_list[13]]) < 50 and util.get_distance([landmarks_list[12] ,landmarks_list[9]]) < 50 and util.get_distance([landmarks_list[20] ,landmarks_list[17]]) > 50 ) 

def detect_gestures(frame, landmarks_list, processed):
    if len(landmarks_list)>=21:
        
        index_finger_tip = find_finger_tip(processed)
        thumb_index_dist = util.get_distance([landmarks_list[4] ,landmarks_list[5]])

        if thumb_index_dist<50 and util.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]):
            move_mouse(index_finger_tip)
            

        elif is_left_click(landmarks_list,thumb_index_dist) : # check for left click
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # it shows that we are clicking or using this functionality on frame

        elif is_right_click(landmarks_list,thumb_index_dist) : # check for right click
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        elif is_double_click(landmarks_list,thumb_index_dist) : # check for double click
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)


        elif is_screenshot(landmarks_list,thumb_index_dist) : # check for screenshot click
            im1 = pyautogui.screenshot()
            label = random.randint(1,1000)
            im1.save(f'my_screenshot_{label}.png')
            cv2.putText(frame, "Screenshot", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

def main():
    cap = cv2.VideoCapture(0)
    draw = mp.solutions.drawing_utils

    try:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.flip(frame,1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            processed = hands.process(frameRGB) # will detect and contain all of the landmarks

            landmarks_list = []

            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS) #this shows/ draws all of the hand landmarks

                for lm in hand_landmarks.landmark:
                    landmarks_list.append((lm.x,lm.y))

            detect_gestures(frame, landmarks_list, processed)



            cv2.imshow('Frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  #wat for 1 millisecond after each frame and if input in keyboard is q then break i.e. to close the video capturing  and ord('q') take ascii value of q
                break

    except KeyboardInterrupt:
        print("\n[INFO] Exiting program...")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


