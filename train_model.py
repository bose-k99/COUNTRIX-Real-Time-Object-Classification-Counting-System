# train_model.py
from ultralytics import YOLO

# Load a pretrained YOLOv8 nano model (fastest for real-time)
import torch

# Check CUDA
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load model and move to GPU
model = YOLO("yolov8n.pt")  
#model.to(device)

# Train the model on our dataset
model.train(
    data="data.yaml",        # Path to data.yaml in countrix/
    epochs=120,              # Number of training epochs
    imgsz=320,               # Image size for training
    batch=8,                # Batch size (adjust based on your GPU/CPU)
    name="nuts_bolts_coins_screws"  # Folder name for results
)

print("Training complete! Model saved in runs/train/nuts_bolts_coins_screws/")