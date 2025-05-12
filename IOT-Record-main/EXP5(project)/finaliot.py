import torch
import cv2
import serial
import time

# ✅ Connect to Arduino (update port if needed)
arduino = serial.Serial('/dev/cu.usbserial-1140', 9600)  # Adjust for your OS
time.sleep(2)

# ✅ Load your custom YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/niranjan/Downloads/best.pt')  # Use full path if needed

# ✅ Start webcam
cap = cv2.VideoCapture(0)

# ✅ Object classes from your trained model
TARGET_CLASSES = ['knife', 'cell phone']

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model(frame)
    detections = results.pandas().xyxy[0]
    detected = False

    # Iterate over detections
    for _, row in detections.iterrows():
        label = row['name']
        conf = row['confidence']

        if label in TARGET_CLASSES and conf > 0.5:
            detected = True
            cv2.rectangle(frame, (int(row['xmin']), int(row['ymin'])),
                          (int(row['xmax']), int(row['ymax'])), (0, 0, 255), 2)
            cv2.putText(frame, f"{label.upper()} DETECTED", (int(row['xmin']), int(row['ymin']) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # ✅ Send detection signal to Arduino
    arduino.write(b'1' if detected else b'0')

    # ✅ Show the camera frame
    cv2.imshow("Weapon Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ✅ Clean up
cap.release()
arduino.close()
cv2.destroyAllWindows()