💤 Drowsiness Detection System using OpenCV & Mediapipe
📸 Overview
This project is a real-time drowsiness detection system built using OpenCV, Mediapipe, and Python.
It tracks eye movement via facial landmarks and triggers an alarm if the user's eyes remain closed for too long — a crucial safety feature for drivers and machine operators.


🎯 Features
✅ Real-time eye tracking using Mediapipe Face Mesh
✅ Calculates Eye Aspect Ratio (EAR) to measure eye openness
✅ Plays an alarm sound when drowsiness is detected
✅ Captures screenshots and logs timestamps of drowsy moments
✅ Lightweight and fast — no external models to download
✅ Works with any webcam

📂 Project Structure
.
├── music.wav                 # Alarm sound file
├── alerts/                   # Folder for saved screenshots and logs
│   ├── drowsy_YYYYMMDD_HHMMSS.jpg
│   └── log.txt
├── drowsiness_detector.py     # Main detection script
├── README.md                  # This file!
├── requirements.txt


🛠️ Installation
📦 Requirements
Python 3.x
OpenCV
Mediapipe
SciPy
Pygame
NumPy

💾 Install Dependencies
pip install -r requirements.txt


🚀 How to Run
Clone this repository:

git clone https://github.com/yourusername/drowsiness-detector
cd drowsiness-detector
- Place an alarm sound file named music.wav in the project folder.

Run the main script:
python drowsiness_detector.py
- Press q to quit the application.

📊 How It Works
- Face Detection & Landmark Tracking:
- Uses Mediapipe's Face Mesh to locate eye landmarks in each video frame.

Eye Aspect Ratio (EAR) Calculation:
- Calculates EAR based on 6 key eye landmarks for both eyes.
- If the EAR drops below a threshold for a set number of consecutive frames, the system considers the user drowsy.

Drowsiness Alert:
- Plays a continuous alarm sound
- Captures a screenshot
- Logs the detection time in alerts/log.txt

📸 Example Detection
“Eyes closed for too long — system triggers an alarm, logs the event, and saves a snapshot.”

Log Example

Drowsiness detected at 2025-04-20 18:43:12
Drowsiness detected at 2025-04-20 18:55:07


🎨 Future Ideas
- Add a real-time graph for EAR values
- Include head pose detection
- Support multiple faces
- Mobile camera streaming support
- Voice notifications

🙌 Credits
OpenCV
Mediapipe
Pygame
SciPy



🌟 Star this repo if you like it!
