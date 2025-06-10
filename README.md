# yolov11-vehicle-speed-tracker
## Introduction
YOLOv11 Surveillance Speed Tracker is a computer vision pipeline that performs real-time vehicle detection, tracking, and speed estimation from video footage. Leveraging YOLOv11 for object detection and ByteTrack for multi-object tracking, it maps vehicle positions from camera space to world space using perspective transformation, enabling accurate speed calculation in km/h.

Designed for use in road surveillance, intelligent traffic systems, and smart city infrastructure, this system integrates with the Supervision library for real-time annotation and visualization.


## Table of Contents
- [Features](#features)
- [Project Structure](#ProjectStructure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Features
- 📦 Object detection with YOLOv11
- 🧭 Perspective transformation for accurate distance mapping
- 🏎️ Speed estimation in real-world units (km/h)
- 🔁 Multi-object tracking using ByteTrack
- 🖥️ Real-time annotation with bounding boxes, traces, and speed labels
- 🛠️ Modular and production-ready Python package structure

## Project Structure
```bash
vehicle_speed_estimation/
│── config/                    # Configuration files (video URL, model path, class filters, constants)
│   ├── settings.py            
│── modules/                   # Core logic modules
│   ├── mapping.py             # Stores evaluation results  
│   ├── speedometer.py         # Cam2WorldMapper for perspective 
│   ├── annotators.py          # Bounding box, trace, and label annotation 
│── zone/                      # Polygon zone definitions and trigger logic
│   ├── zone_trigger.py                 
│── models/                    # Model checkpoints 
│   ├── yolo11n.pt             
│── utils/                     # Utility functions and constants  
│   ├── downloader.py          # Google Drive video downloader      
│   ├── constants.py           # Polygon coordinates and camera calibration points
│── main.py                    # Entry point: runs detection, tracking, and  
│── requirements.txt           # Package dependencies  
 
```
## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/krishnapriya-nynaru/yolov11-vehicle-speed-tracker.git
2. Change to Project Directory
    ```bash
    cd vehicle_speed_estimator
3. Install required packages :
    ```bash
    pip install -r requirements.txt

## Usage
Run the script with Python
```bash
python main.py
```
`Note:`
You can change the YOLOv11 model variant in config/settings.py to experiment with detection performance vs. speed.

For Example:
```bash
# config/settings.py

MODEL_PATH = "yolo11s.pt"  # Or "yolo11m.pt", "yolo11n.pt"
```
- yolo11n.pt – Fastest, least accurate
- yolo11s.pt – Good balance
- yolo11m.pt – More accurate, slower

Try each and observe the trade-off between FPS and accuracy in your environment.

## Results

![alt_text](https://github.com/krishnapriya-nynaru/yolov11-vehicle-speed-tracker/blob/main/vehicle_speed_estimator/results/output.gif?raw=true)


## Contributing 
Contributions are welcome! To contribute to this project:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure the code passes all tests.
4. Submit a pull request with a detailed description of your changes.

If you have any suggestions for improvements or features, feel free to open an issue!

## Acknowledgments
- [**YOLOv11 for object detection.**](https://github.com/ultralytics/yolov11)
- [**ByteTracker for Multi object tracking.**](https://github.com/FoundationVision/ByteTrack)
- [**OpenCV for computer vision functionalities.**](https://opencv.org/)
- [**Supervision by Roboflow, for seamless computer vision annotation tools (bounding boxes, traces, and on-frame labels).**](https://github.com/roboflow/supervision)

### 🎉 Happy coding!
