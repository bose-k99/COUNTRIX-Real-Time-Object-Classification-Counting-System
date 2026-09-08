from ultralytics import YOLO
import cv2
import torch

# Check CUDA
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load model and move to GPU
model = YOLO("best.pt")
model.to(device)

# Start camera stream
cap = cv2.VideoCapture("http://192.168.77.206:81/stream")

if not cap.isOpened():
    print("❌ Cannot open video stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No frame received")
        continue

    # Resize and convert
    frame = cv2.resize(frame, (320, 320))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run YOLO detection on GPU
    results = model(frame_rgb, device=device)

    # Draw results
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            
            label = model.names.get(cls, "Unknown")

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label} {conf:.2f}"
            y_text = max(y1 - 10, 20)
            cv2.putText(frame, text, (x1, y_text),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("YOLO Object Detection", cv2.resize(frame, (640, 480)))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()