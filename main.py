import serial, time, cv2, os, face_recognition, yagmail, requests
from datetime import datetime

# === CONFIG ===
ARDUINO_PORT = 'COM8'  # Update to your port
BLYNK_TOKEN = '9ISu71yNYZlgVRILgfPnPl1ILoCxssSl'
OWNER_EMAIL = '22bcscs053@student.rru.ac.in'
YOUR_EMAIL = 'testprojecx@gmail.com'
YOUR_APP_PASSWORD = 'qhrxhonembbmryls'

# === INIT ===
yag = yagmail.SMTP(YOUR_EMAIL, YOUR_APP_PASSWORD)
ser = serial.Serial(ARDUINO_PORT, 9600, timeout=1)

# === BLYNK API ===
BLYNK_BASE = 'https://blynk.cloud/external/api'

def blynk_write(pin, value):
    try:
        requests.get(f'{BLYNK_BASE}/update?token={BLYNK_TOKEN}&{pin}={value}')
    except:
        print("[WARN] Failed to write to Blynk")

def blynk_read(pin):
    try:
        r = requests.get(f'{BLYNK_BASE}/get?token={BLYNK_TOKEN}&{pin}')
        return r.text.strip('"')
    except:
        print("[WARN] Failed to read from Blynk")
        return '0'

# === LOAD KNOWN FACES ===
known_encodings = []
known_names = []
for filename in os.listdir('known_faces'):
    path = f"known_faces/{filename}"
    image = face_recognition.load_image_file(path)
    enc = face_recognition.face_encodings(image)
    if enc:
        known_encodings.append(enc[0])
        known_names.append(os.path.splitext(filename)[0])
    else:
        print(f"[WARN] No face found in {filename}")

# === FACE RECOGNITION FUNCTION ===
def recognize_face():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("[ERROR] Couldn't access webcam.")
        return

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for enc in encodings:
        matches = face_recognition.compare_faces(known_encodings, enc)
        if True in matches:
            name = known_names[matches.index(True)]
            print(f"[INFO] Known: {name}")
            ser.write(b"KNOWN\n")
            ser.write(b"YELLOW\n")
            blynk_write('V0', f'"Welcome, {name}"')
            return
        else:
            print("[ALERT] Stranger Detected!")
            ser.write(b"STRANGER\n")
            ser.write(b"RED_BUZZER\n")

            filename = f"stranger_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)

            blynk_write('V0', '"Stranger detected. Awaiting approval."')
            try:
                yag.send(
                    to=OWNER_EMAIL,
                    subject="⚠ Stranger Detected!",
                    contents="A stranger was detected at your door. Click the Blynk button to approve.",
                    attachments=[filename]
                )
            except Exception as e:
                print("[EMAIL ERROR]", e)

            # Wait for approval
            start = time.time()
            approved = False
            while time.time() - start < 60:
                approval = blynk_read('V1')
                if approval == '1':
                    print("[BLYNK] Owner approved entry")
                    ser.write(b"APPROVED\n")
                    ser.write(b"STOP_BUZZER_YELLOW\n")
                    blynk_write('V0', '"Stranger approved. Entry granted."')
                    blynk_write('V1', '0')
                    approved = True
                    break
                time.sleep(1)

            if not approved:
                blynk_write('V0', '"Access denied. No approval."')
                print("[INFO] No approval given.")

# === MAIN LOOP ===
print("[SYSTEM] Face recognition system running with motion trigger...")
while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        if line == "MOTION":
            print("[EVENT] Motion Detected")
            recognize_face()
    time.sleep(1)
