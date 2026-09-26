"""
Virtual Mouse Using Hand Gestures - cvzone Version
Works with cvzone library (more reliable than MediaPipe)
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import random
import numpy as np
from pynput.mouse import Button, Controller

# Initialize
mouse = Controller()
screen_width, screen_height = pyautogui.size()

# Initialize hand detector
detector = HandDetector(detectionCon=0.7, maxHands=1)

def get_angle(a, b, c):
    """Calculate angle between three points."""
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radians))
    return angle

def get_distance(landmark_list):
    """Calculate distance between two landmarks."""
    if len(landmark_list) < 2:
        return 0
    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    L = np.hypot(x2 - x1, y2 - y1)
    return np.interp(L, [0, 1], [0, 1000])

def move_mouse(landmark_list):
    """Move cursor based on index finger tip."""
    if len(landmark_list) >= 9:
        # Index finger tip is landmark 8
        x = int(landmark_list[8][0])
        y = int(landmark_list[8][1] / 2)
        pyautogui.moveTo(x, y)

def is_left_click(landmark_list, thumb_index_dist):
    """Detect left click gesture."""
    if len(landmark_list) < 13:
        return False
    return (
        get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) > 90 and
        thumb_index_dist > 50
    )

def is_right_click(landmark_list, thumb_index_dist):
    """Detect right click gesture."""
    if len(landmark_list) < 13:
        return False
    return (
        get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90 and
        thumb_index_dist > 50
    )

def is_double_click(landmark_list, thumb_index_dist):
    """Detect double click gesture."""
    if len(landmark_list) < 13:
        return False
    return (
        get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        thumb_index_dist > 50
    )

def is_screenshot(landmark_list, thumb_index_dist):
    """Detect screenshot gesture."""
    if len(landmark_list) < 13:
        return False
    return (
        get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        thumb_index_dist < 50
    )

def detect_gesture(frame, landmark_list):
    """Detect and execute gestures."""
    if len(landmark_list) >= 21:
        # Normalize coordinates
        normalized_landmarks = []
        for lm in landmark_list:
            normalized_landmarks.append((lm[0] / screen_width, lm[1] / screen_height))

        thumb_index_dist = get_distance([normalized_landmarks[4], normalized_landmarks[5]])

        # Check gestures
        if get_distance([normalized_landmarks[4], normalized_landmarks[5]]) < 50 and \
           get_angle(normalized_landmarks[5], normalized_landmarks[6], normalized_landmarks[8]) > 90:
            move_mouse(landmark_list)
        elif is_left_click(normalized_landmarks, thumb_index_dist):
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif is_right_click(normalized_landmarks, thumb_index_dist):
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif is_double_click(normalized_landmarks, thumb_index_dist):
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        elif is_screenshot(normalized_landmarks, thumb_index_dist):
            im1 = pyautogui.screenshot()
            label = random.randint(1, 1000)
            im1.save(f'my_screenshot_{label}.png')
            cv2.putText(frame, "Screenshot Taken", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

def main():
    """Main function."""
    print("🎮 Virtual Mouse with cvzone Started!")
    print("Press 'q' to quit\n")
    print("Gestures:")
    print("- Move index finger to move cursor")
    print("- Index finger bent + others extended: Left Click")
    print("- Middle finger bent + others extended: Right Click")
    print("- Both bent (far apart): Double Click")
    print("- Both bent (close together): Screenshot\n")

    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)

            # Detect hands
            hands, frame = detector.findHands(frame, draw=True)

            if hands:
                hand = hands[0]
                landmark_list = hand['lmList']  # List of 21 landmarks

                # Detect gestures
                detect_gesture(frame, landmark_list)

            cv2.imshow('Virtual Mouse (cvzone) - Press Q to Quit', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("\n👋 Virtual Mouse Stopped!")

if __name__ == '__main__':
    main()
