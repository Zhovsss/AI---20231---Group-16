import os

from ultralytics import YOLO

# Load a model
model = YOLO('yolov8x.pt')  # load a custom model

# Predict with the model
image_folder = 'Image'
for image in os.listdir(image_folder):
    results = model(image_folder+'/'+image, save=True, save_txt=True, classes=[0, 3])  # predict on an image