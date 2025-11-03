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


---

## ⚙️ Installation & Quickstart

### 1️⃣ Clone Repository
```bash
git clone https://github.com/apdaniswara-sys/OJD_ObjectDetection.git
cd OJD_ObjectDetection

    2️⃣ Create Virtual Environment
python -m venv env_obj_dtc
# Windows PowerShell
.\env_obj_dtc\Scripts\Activate.ps1
# or cmd
env_obj_dtc\Scripts\activate.bat

    3️⃣ Install Dependencies
pip install -r requirements.txt

    4️⃣ Run Detection Demo
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
Camera Feed ───▶ YOLOv8 Detection ───▶ Annotated Frame
                             │
                             ▼
                     Side Panel Summary


🖼️ Demo Output (Preview)
Below is a preview of what you’ll see when running the detection script:

<p align="center"> <img src="demo_preview.jpg" width="600" alt="OJD_ObjectDetection demo preview"/> </p>

✅ Detected objects are highlighted with bounding boxes.
✅ The right-side panel shows color-coded class counts (e.g., "person: 2", "bottle: 1").
✅ The interface is clean, with easy-to-read modern design.

📦 Example Output (Console Log)
[INFO] Model: yolov8n.pt
[INFO] Camera started (640x480)
[DETECT] Frame 34: person=2, bottle=1, chair=1
[DETECT] Frame 35: person=2, bottle=1, chair=1

🧠 Requirements
| Package       | Version |
| ------------- | ------- |
| Python        | ≥ 3.9   |
| ultralytics   | latest  |
| opencv-python | ≥ 4.8   |
| numpy         | ≥ 1.24  |

Install automatically with:
pip install -r requirements.txt

🧰 Troubleshooting
| Issue                                                | Cause                 | Fix                                                    |
| ---------------------------------------------------- | --------------------- | ------------------------------------------------------ |
| `ModuleNotFoundError: No module named 'ultralytics'` | Package not installed | Run `pip install ultralytics`                          |
| Camera not opening                                   | Wrong camera index    | Edit `cv2.VideoCapture(0)` in `camera_object_count.py` |
| Slow performance                                     | Weak GPU / CPU        | Lower camera resolution to 480×360 or use `yolov8n.pt` |

🧑‍💻 Author

Developed by apdaniswara-sys
📬 GitHub Profile

🪪 License
This project is licensed under the MIT License — free for commercial and educational use.

❤️ Example Preview (Real Output)
demo_preview.jpg
