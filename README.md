# COUNTRIX: Real-Time-Object-Classification-Counting-System

Countrix is an automated object detection and counting system that combines **YOLOv8, ESP32-CAM, and Arduino UNO** to detect and count small objects such as **coins, screws, nuts, and bolts**.

The ESP32-CAM captures images of objects as they fall onto a counting platform. A custom-trained YOLOv8n model processes the images and identifies the objects using bounding boxes. An Arduino-controlled servo operates a flap mechanism that raises and lowers the platform, controlling the movement of the objects. The detected counts are then sent back to the Arduino and displayed on a **16×2 I2C LCD**.

## Architecture

```text
        Objects
           │
           ▼
 ┌───────────────────┐
 │ Arduino UNO       │
 │                   │
 │ Controls Servo    │
 └─────────┬─────────┘
           │
           ▼
   Servo-controlled
      Flap/Platform
           │
     Objects fall
           │
           ▼
 ┌───────────────────┐
 │    ESP32-CAM      │
 │                   │
 │ Captures Images   │
 └─────────┬─────────┘
           │
        Wi-Fi
           │
           ▼
 ┌───────────────────┐
 │     Computer      │
 │                   │
 │ OpenCV            │
 │      ↓            │
 │ YOLOv8n           │
 │      ↓            │
 │ Object Counting   │
 └─────────┬─────────┘
           │
     Serial Data
           │
           ▼
 ┌───────────────────┐
 │    Arduino UNO    │
 │                   │
 │ 16×2 I2C LCD      │
 └───────────────────┘
           │
           ▼
     Final Counts
```

## How It Works

1. **Object movement:** The Arduino controls a servo motor that acts as a flap, raising and lowering the counting platform.
2. **Image capture:** Objects fall onto the platform and are captured by the ESP32-CAM.
3. **Image processing:** The camera streams the images to a computer over Wi-Fi.
4. **Object detection:** OpenCV receives the frames and passes them to the custom-trained YOLOv8n model.
5. **Classification & localization:** YOLOv8n detects and locates four classes:

   * Coin
   * Screw
   * Nut
   * Bolt
6. **Counting:** The detected objects are counted based on their predicted classes.
7. **Result transmission:** The counts are sent from the computer to the Arduino through serial communication.
8. **Output:** The Arduino displays the final counts on the 16×2 I2C LCD.

## Machine Learning

The project uses **YOLOv8n**, a lightweight one-stage object detection model trained on a custom dataset.

### Training Configuration

| Parameter  | Value                  |
| ---------- | ---------------------- |
| Model      | YOLOv8n                |
| Image Size | 320 × 320              |
| Epochs     | 50                     |
| Classes    | Coin, Screw, Nut, Bolt |
| Task       | Object Detection       |

The training results and trained weights are available in:

```text
runs/detect/train8/
```

## Hardware

* ESP32-CAM — image capture and Wi-Fi streaming
* Arduino UNO — control and communication
* Servo Motor — flap/platform mechanism
* 16×2 I2C LCD — displaying object counts
* FTDI USB-to-TTL — ESP32-CAM programming
* Counting platform — object collection and detection area

## Software & Technologies

* **Python**
* **YOLOv8 / Ultralytics**
* **OpenCV**
* **PyTorch**
* **CUDA**
* **Arduino C/C++**
* **Serial Communication**
* **Wi-Fi / MJPEG Streaming**

## Project Structure

```text
countrix/
│
├── arduino_code/
│   └── arduino_code.ino
│
├── data.yaml
├── detect_stream.py
├── train_model.py
├── yolov8n.pt
│
└── runs/
    └── detect/
        └── train8/
            ├── args.yaml
            ├── confusion_matrix.png
            ├── confusion_matrix_normalized.png
            ├── results.csv
            ├── results.png
            └── weights/
                └── best.pt
```

## Future Improvements

* Automated sorting of detected objects
* Addition of more classification of objects
* Improved detection under varying lighting conditions
* Real-time monitoring dashboard
* Deployment on edge hardware

