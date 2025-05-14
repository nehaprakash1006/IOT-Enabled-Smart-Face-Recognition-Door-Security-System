# 🚪 Smart Face Recognition Door Security System 🔐

A smart IoT-based door security system that uses Python, OpenCV, Arduino, and Blynk to detect motion, recognize faces, and control hardware components like LEDs and buzzers. Real-time alerts are sent via email and Blynk for unknown visitors.

---

## ✨ Features

- 🎯 Motion detection using PIR sensor  
- 📸 Face recognition via webcam  
- 🚨 Stranger triggers RED LED + buzzer + email alert  
- ✅ Known person triggers GREEN LED  
- 📬 Sends snapshot email to owner on unknown detection  
- 📱 Owner can approve via Blynk app (cloud control)  
- 🤖 Arduino handles real-time output feedback  

---

## 🔌 Hardware Requirements

- Arduino UNO or Nano  
- PIR Motion Sensor  
- Red LED + Green LED  
- Buzzer  
- Breadboard and jumper wires  
- Webcam (for computer)  

---

## 🧠 Software Requirements

- Python 3.x  
- Arduino IDE  
- Python Libraries:
  - `opencv-python`
  - `face_recognition`
  - `yagmail`
  - `requests`

Install dependencies:

pip install opencv-python face_recognition yagmail requests

## 🛠️ Setup & Usage

### 🔌 Arduino

1. Open **Arduino IDE**
2. Paste your Arduino code into a new sketch
3. Save the file as `arduino_code.ino`
4. Connect your Arduino via USB
5. Select the correct COM port from **Tools > Port**
6. Click **Upload** to flash the code

---

### 👁️‍🗨️ Face Recognition Script (Python)

1. Clone/download this repository
2. Create a folder named `known_faces/` and add images of known people  
   *(e.g., `john.jpg`, `alice.png`)*
3. Edit the following variables in `main.py`:
   - `ARDUINO_PORT` (e.g., `'COM8'`)
   - `YOUR_EMAIL`, `YOUR_APP_PASSWORD`
   - `OWNER_EMAIL` (email to receive alerts)
   - `BLYNK_TOKEN` (from Blynk dashboard)

4. Run the script:
```bash
python main.py
