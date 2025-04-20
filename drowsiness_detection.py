import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance
from pygame import mixer
from datetime import datetime
import os

mixer.init()        # Initialize mixer for alarm sound
mixer.music.load("music.wav")

mp_face_mesh = mp.solutions.face_mesh       # Mediapipe face mesh setup
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)


LEFT_EYE = [33, 160, 158, 133, 153, 144]    # Eye landmark indices for mediapipe
RIGHT_EYE = [263, 387, 385, 362, 380, 373]

def eye_aspect_ratio(eye):      # eye aspect ratio calculation function
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

thresh = 0.25   #threshold 
frame_check = 20
flag = 0

if not os.path.exists("alerts"):    #alerts for ss
    os.makedirs("alerts")

cap = cv2.VideoCapture(0)   #video capture

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        mesh_points = np.array([[int(p.x * frame.shape[1]), int(p.y * frame.shape[0])]
                                for p in results.multi_face_landmarks[0].landmark])

        leftEye = mesh_points[LEFT_EYE]
        rightEye = mesh_points[RIGHT_EYE]

        
        cv2.polylines(frame, [leftEye], True, (0, 255, 0), 1)           #drawing eye landmarks
        cv2.polylines(frame, [rightEye], True, (0, 255, 0), 1)

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        if ear < thresh:
            flag += 1
            print(f"Drowsy frame count: {flag}")

            if flag >= frame_check:
                cv2.putText(frame, "**************** ALERT! ****************", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                if not mixer.music.get_busy():      #play alarm
                    mixer.music.play()

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")    # Save ss with timestamp
                cv2.imwrite(f"alerts/drowsy_{timestamp}.jpg", frame)

                with open("alerts/log.txt", "a") as log_file:   # store log
                    log_file.write(f"Drowsiness detected at {timestamp}\n")
        else:
            flag = 0
            mixer.music.stop()

    cv2.imshow("Drowsiness Detector", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
