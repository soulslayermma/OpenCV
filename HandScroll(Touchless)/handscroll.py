import cv2
import mediapipe as mp
import pyautogui


datas=[('C:/Users/gauri/AppData/Local/Programs/Python/Python312/Lib/site-packages/mediapipe/modules/hand_landmark/hand_landmark_tracking_cpu.binarypb', 'mediapipe/modules/hand_landmark')]
# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Open Webcam
cap = cv2.VideoCapture(0)

while True:  # Keep the program running indefinitely
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    wrist_positions = []  # Store wrist positions

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get fingertip positions
            finger_tips = [
                hand_landmarks.landmark[i].y
                for i in [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                          mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
            ]
            finger_mcp = [
                hand_landmarks.landmark[i].y
                for i in [mp_hands.HandLandmark.INDEX_FINGER_MCP, mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                          mp_hands.HandLandmark.RING_FINGER_MCP, mp_hands.HandLandmark.PINKY_MCP]
            ]

            # Detect closed palm (if fingertips are lower than MCP joints)
            if all(tip > mcp for tip, mcp in zip(finger_tips, finger_mcp)):
                wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x

                if wrist_x < 0.5:  # Left Hand → Scroll Down
                    pyautogui.scroll(-75)
                    print("Scrolling Down ⬇️")
                else:  # Right Hand → Scroll Up
                    pyautogui.scroll(75)
                    print("Scrolling Up ⬆️")

            # Store wrist position for hand-cross detection
            wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
            wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
            wrist_positions.append((wrist_x, wrist_y))

        # Check if two hands are crossing (close wrist positions)
        if len(wrist_positions) == 2:
            x_diff = abs(wrist_positions[0][0] - wrist_positions[1][0])
            y_diff = abs(wrist_positions[0][1] - wrist_positions[1][1])

            if x_diff < 0.1 and y_diff < 0.1:  # Small threshold to detect overlap
                print("Hands crossed! Closing program...")
                break  # Exit loop → Close program

    cv2.imshow("Hand Gesture Scrolling + Close on Cross", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit manually
        break

cap.release()
cv2.destroyAllWindows()