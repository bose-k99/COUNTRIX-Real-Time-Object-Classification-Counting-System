from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("runs/detect/train/weights/best.pt")

# ESP32 stream URL (MJPEG)
url = "http://10.195.53.206:81/stream"

# Open stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Cannot open stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize to match training (important)
    frame = cv2.resize(frame, (320, 320))

    # Run YOLO detection
    results = model(frame)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()