# 🚪 Smart Face Recognition Door Security System 🔐

A smart IoT-based door security system that uses Python, OpenCV, Arduino, and Blynk to detect motion, recognize faces, and control hardware components like LEDs and buzzers. Real-time alerts are sent via email and Blynk for unknown visitors.

![WhatsApp Image 2025-05-14 at 23 19 17_8625dce0](https://github.com/user-attachments/assets/b2f446f8-bad6-4cf6-abf7-fc2c23cac28b)

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

## 🔌 Step-by-Step Wiring with Breadboard Numbers

### 1. ✅ Connect Arduino Power to Breadboard

| Arduino Pin | Breadboard        | Notes                         |
|-------------|-------------------|-------------------------------|
| 5V          | Red rail (top)    | Power rail, use jumper wire  |
| GND         | Blue rail (top)   | Ground rail, jumper wire     |

💡 These rails now provide power to all your components.

---

### 2. 🕵️ PIR SENSOR

| PIR Pin | Breadboard Row | Arduino Pin | Notes                                 |
|---------|----------------|-------------|---------------------------------------|
| VCC     | A5             | —           | Connect to red rail via jumper wire  |
| GND     | A6             | —           | Connect to blue rail via jumper wire |
| OUT     | A7             | D2          | Jumper wire from row 7 to D2         |

---

### 3. 🔴 RED LED

| LED Leg         | Breadboard Row | Arduino Pin | Notes                         |
|-----------------|----------------|-------------|-------------------------------|
| Long (Anode)    | E10            | D7          | Jumper from E10 to D7         |
| Short (Cathode) | E11            | —           | Jumper to blue (GND) rail     |

---

### 4. 🟢 GREEN LED

| LED Leg         | Breadboard Row | Arduino Pin | Notes                         |
|-----------------|----------------|-------------|-------------------------------|
| Long (Anode)    | E14            | D8          | Jumper from E14 to D8         |
| Short (Cathode) | E15            | —           | Jumper to blue (GND) rail     |

---

### 5. 🔊 BUZZER

| Buzzer Pin | Breadboard Row | Arduino Pin | Notes                         |
|------------|----------------|-------------|-------------------------------|
| + (long)   | E18            | D9          | Jumper from E18 to D9         |
| – (short)  | E19            | —           | Jumper to blue (GND) rail     |


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
