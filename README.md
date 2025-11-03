# OJD_ObjectDetection
**Real-Time Object Identification & Counting (YOLOv8 + OpenCV)**

This repository contains a lightweight demo project for real-time object detection using YOLOv8 (Ultralytics)
and OpenCV, with a modern side-panel that counts detected objects by class.

## Features
- Real-time object detection from webcam using YOLOv8 (ultralytics).
- Modern right-side panel with colored badges per object class and counts.
- Lightweight default model (yolov8n) and default camera resolution 640x480.
- Simple launcher `main.py` and main detection script `camera_object_count.py`.

## Quickstart
1. Clone repository
```bash
git clone https://github.com/apdaniswara-sys/OJD_ObjectDetection.git
cd OJD_ObjectDetection
```
2. Create virtual environment and activate it
```bash
python -m venv env_obj_dtc
# Windows PowerShell
.\env_obj_dtc\Scripts\Activate.ps1
# or cmd
env_obj_dtc\Scripts\activate.bat
```
If PowerShell blocks execution, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run counting demo
```bash
python src/camera_object_count.py
```

Press `q` to quit the camera window.

## Files
- `src/camera_object_count.py` — main real-time detection + counting script
- `src/utils/draw_utils.py` — helper functions for drawing the side panel
- `demo.png` — preview image (mockup) showing sample output
- `requirements.txt` — minimal dependencies
- `.gitignore` — ignores virtual environment and caches

## Notes
- The `yolov8n.pt` model will be automatically downloaded by ultralytics the first time it runs.
- If your machine is low on resources, use `yolov8n.pt` (default) which is light and fast.
