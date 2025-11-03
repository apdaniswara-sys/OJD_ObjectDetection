# 🧠 OJD_ObjectDetection
**Real-Time Object Identification & Counting (YOLOv8 + OpenCV)**  

A lightweight, modern object detection demo built using **Ultralytics YOLOv8** and **OpenCV**, designed for real-time object identification and counting.  
This project includes a clean UI with a right-side panel displaying **class-wise object counts** using color-coded boxes — ideal for quick prototyping or real-time monitoring dashboards.

---

## 🚀 Features
✅ Real-time object detection from webcam (YOLOv8n model by default)  
✅ Right-side dashboard panel showing object class & total count  
✅ Automatically downloads model weights on first run  
✅ Lightweight: optimized for 640×480 capture resolution  
✅ Modular: `main.py` launcher and structured `src/` folder  
✅ Fully open-source and easy to customize  

---

## 🗂️ Project Structure
OJD_ObjectDetection/
│
├── main.py
├── requirements.txt
├── .gitignore
│
├── src/
│ ├── camera_object_count.py # main detection + counting script
│ ├── utils/
│ │ └── draw_utils.py # helper for drawing side panel
│
├── assets/
│ └── demo_preview.jpg # example output image
│
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Quickstart

### 1️⃣ Clone Repository
```bash
git clone https://github.com/apdaniswara-sys/OJD_ObjectDetection.git
cd OJD_ObjectDetection
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv env_obj_dtc
# Windows PowerShell
.\env_obj_dtc\Scripts\Activate.ps1
# or cmd
env_obj_dtc\Scripts\activate.bat
If PowerShell blocks execution, allow temporarily:

powershell
Copy code
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run Detection Demo
bash
Copy code
python src/camera_object_count.py
Press q to quit the camera window.

🧩 How It Works
YOLOv8 (Ultralytics) detects objects in each video frame.

OpenCV renders bounding boxes and class labels on the frame.

A side panel dynamically displays:

Unique object classes detected.

Count of each detected object.

Colored badges for clarity and style.

Example flow:

mathematica
Copy code
Camera Feed ───▶ YOLOv8 Detection ───▶ Annotated Frame
                             │
                             ▼
                     Side Panel Summary

🖼️ Demo Output (Preview)
Below is a preview of what you’ll see when running the detection script:

<p align="center"> <img src="image_result.png" width="600" alt="OJD_ObjectDetection demo preview"/> </p>
✅ Detected objects are highlighted with bounding boxes.
✅ The right-side panel shows color-coded class counts (e.g., "person: 2", "bottle: 1").
✅ The interface is clean, with easy-to-read modern design.

📦 Example Output (Console Log)
When running, the console will also show real-time detection info:

csharp
Copy code
[INFO] Model: yolov8n.pt
[INFO] Camera started (640x480)
[DETECT] Frame 34: person=2, cellphone=1, chair=1

🧠 Requirements
Package	Version
Python	≥ 3.9
ultralytics	latest
opencv-python	≥ 4.8
numpy	≥ 1.24

Install automatically with:

bash
Copy code
pip install -r requirements.txt

🧰 Troubleshooting
Issue	Cause	Fix
ModuleNotFoundError: No module named 'ultralytics'	Package not installed	Run pip install ultralytics
Camera not opening	Wrong camera index	Edit cv2.VideoCapture(0) in camera_object_count.py
Slow performance	Weak GPU / CPU	Lower camera resolution to 480×360 or use yolov8n.pt

📸 Example Customization
You can easily switch to another YOLOv8 model:

python
Copy code
model = YOLO('yolov8s.pt')
Or adjust frame size:

python
Copy code
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

📍 Future Improvements
 Add FPS counter overlay

 Add CSV logger for object counts

 Optional save-to-video output

 Web-based streaming dashboard

🧑‍💻 Author
Developed by apdaniswara-sys
📬 GitHub Profile

🪪 License
This project is licensed under the MIT License — free for commercial and educational use.

❤️ Example Preview (Real Output)
If you want to embed a real screenshot later, place it in:

bash
image_result.png
