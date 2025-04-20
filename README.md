# 🚙🚨😴Drowsiness Detection System using OpenCV & Mediapipe

## 📸 Overview  
This project is a **real-time drowsiness detection system** built using **OpenCV**, **Mediapipe**, and **Python**.  
It tracks eye movement via facial landmarks and triggers an alarm if the user's eyes remain closed for too long — a crucial safety feature for drivers and machine operators.

---

## 🎯 Features  
- ✅ Real-time eye tracking using **Mediapipe Face Mesh**  
- ✅ Calculates **Eye Aspect Ratio (EAR)** to measure eye openness  
- ✅ Plays an **alarm sound** when drowsiness is detected  
- ✅ Captures **screenshots** and **logs timestamps** of drowsy moments  
- ✅ Lightweight and fast — no external models to download  
- ✅ Works with any webcam  

---

## 📂 Project Structure  
```
.
├── music.wav                 # Alarm sound file  
├── alerts/                   # Folder for saved screenshots and logs  
│   ├── drowsy_YYYYMMDD_HHMMSS.jpg  
│   └── log.txt  
├── drowsiness_detector.py     # Main detection script  
├── README.md                  # This file!  
├── requirements.txt  
```

---

## 🛠️ Installation  

### 📦 Requirements  
- Python 3.x  
- OpenCV  
- Mediapipe  
- SciPy  
- Pygame  
- NumPy  

### 💾 Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run  

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/drowsiness-detector
   cd drowsiness-detector
   ```

2. Place an alarm sound file named `music.wav` in the project folder.

3. Run the main script:
   ```bash
   python drowsiness_detector.py
   ```

4. Press `q` to quit the application.

---

## 📊 How It Works  

### Face Detection & Landmark Tracking  
Uses **Mediapipe's Face Mesh** to locate eye landmarks in each video frame.

### Eye Aspect Ratio (EAR) Calculation  
Calculates EAR based on **6 key eye landmarks** for both eyes.  
If the EAR drops below a threshold for a set number of consecutive frames, the system considers the user drowsy.

### Drowsiness Alert  
- Plays a continuous **alarm sound**  
- Captures a **screenshot**  
- Logs the **detection time** in `alerts/log.txt`  

---

## 📸 Example Detection  

> _“Eyes closed for too long — system triggers an alarm, logs the event, and saves a snapshot.”_

**Log Example**
```
Drowsiness detected at 2025-04-20 18:43:12  
Drowsiness detected at 2025-04-20 18:55:07  
```

---

## 🎨 Future Ideas  

- Add a **real-time graph** for EAR values  
- Include **head pose detection**  
- Support **multiple faces**  
- **Mobile camera streaming** support  
- **Voice notifications**  

---

## 👌 Credits  

- [OpenCV](https://opencv.org/)  
- [Mediapipe](https://mediapipe.dev/)  
- [Pygame](https://www.pygame.org/news)  
- [SciPy](https://scipy.org/)  

---

## 🌟 Star this repo if you like it!