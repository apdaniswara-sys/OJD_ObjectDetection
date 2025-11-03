# 🧠 OJD_ObjectDetection
**Real-Time Object Identification & Counting (YOLOv8 + OpenCV)**  

A lightweight, modern object detection demo built using **Ultralytics YOLOv8** and **OpenCV**, designed for real-time object identification and counting.  
This project includes a clean UI with a right-side panel displaying **class-wise object counts** using color-coded boxes — ideal for quick prototyping or real-time monitoring dashboards.

---

## 🚀 Features
✅ Real-time object detection from webcam (YOLOv8n model by default)  
✅ Right-side dashboard panel showing object class & total count  
✅ Lightweight: optimized for 640×480 capture resolution  


---

## 🗂️ Project Structure
```bash
OJD_ObjectDetection/
│
├── src/
│ ├── camera_object_count.py # main detection + counting script
│ ├── utils/
│ │ └── draw_utils.py # helper for drawing side panel
│
├── .gitignore
├── requirements.txt
├── demo_preview.jpg # example output image
├── README.md
└── yolov8n.pt
```

---

## ⚙️ Installation & Quickstart  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/apdaniswara-sys/OJD_ObjectDetection.git
cd OJD_ObjectDetection
```

---

### 2️⃣ Create Virtual Environment  
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

---

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Detection Demo  
```bash
python src/camera_object_count.py
```
Press **q** to quit the camera window.

---

### 🖼️ Example Preview  
Below is a sample of how the real-time detection dashboard looks (with object boxes and side counter):

![Demo Preview](demo_preview.jpg)

---

### 🗂️ Files Overview  
| File | Description |
|------|--------------|
| `src/camera_object_count.py` | Main real-time detection + counting script |
| `src/utils/draw_utils.py` | Helper for drawing the side panel |
| `main.py` | Simple entry point for launching the app |
| `demo_preview.jpg` | Example screenshot of detection UI |
| `requirements.txt` | Dependencies for running the project |
| `.gitignore` | Ignore list (env, caches, etc.) |

---

### ⚙️ Notes  
- The model `yolov8n.pt` will auto-download on first run.  
- To stop camera stream, press `q`.  
- For better performance, ensure your Python version ≥ 3.10.

---

⭐ **Tip:** Don’t forget to give this repo a star if you find it useful!  
