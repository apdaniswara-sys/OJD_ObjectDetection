# 🧰 Developer Setup Guide — OJD_ObjectDetection

This document provides a quick setup guide for developers working on **OJD_ObjectDetection**, ensuring consistent environment configuration and smooth development experience.

---

## 🧩 1️⃣ Project Overview
OJD_ObjectDetection is a real-time object detection system using **YOLOv8 (Ultralytics)** and **OpenCV**, designed to detect and count objects via webcam input.

---

## ⚙️ 2️⃣ Environment Setup

### 🪄 Create and Activate Virtual Environment

**Windows PowerShell**
```bash
python -m venv env_obj_dtc
.\env_obj_dtc\Scripts\Activate.ps1
```

**Command Prompt (cmd)**
```bash
env_obj_dtc\Scriptsctivate.bat
```

After activation, your prompt should look like:
```
(env_obj_dtc) PS C:\Users\muizz\Documents\OJD_Training\OJD_ObjectDetection>
```

---

## 📦 3️⃣ Install Dependencies
Inside the activated environment:
```bash
pip install -r requirements.txt
```

You can verify installation:
```bash
pip show ultralytics
```

If the package shows a valid location under `env_obj_dtc\Lib\site-packages`, the setup is correct.

---

## 🧠 4️⃣ VS Code Configuration

To ensure VS Code runs scripts **inside the venv**:

1. Open the **Command Palette (Ctrl+Shift+P)**
2. Choose **Python: Select Interpreter**
3. Select the interpreter path:
   ```
   .\env_obj_dtc\Scripts\python.exe
   ```

To persist settings automatically, add or update this file:
`.vscode/settings.json`
```json
{
    "python.defaultInterpreterPath": "env_obj_dtc\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true,
    "python.envFile": "${workspaceFolder}/.env"
}
```

---

## ▶️ 5️⃣ Running the Detection Script
To start real-time detection:
```bash
python src/camera_object_count.py
```
Press **Q** to close the OpenCV window.

---

## 🧹 6️⃣ Common Fixes

| Issue | Cause | Solution |
|-------|--------|-----------|
| `ModuleNotFoundError: No module named 'ultralytics'` | Running from global Python | Activate venv or use correct interpreter |
| `Execution policy error` | PowerShell blocks script | Run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` |
| `Camera not opening` | Device busy / wrong ID | Try `cv2.VideoCapture(1)` or restart camera app |

---

## 🧾 7️⃣ Version Control Tips
Always commit with a timestamped message:
```bash
git commit -m "Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git push origin main
```

---

## 👥 8️⃣ Developer Notes
- Keep dependencies updated:
  ```bash
  pip install --upgrade ultralytics opencv-python
  ```
- Store all assets (preview images, model weights) under `/assets/`
- Avoid committing large `.pt` models (>100MB) directly to GitHub — use Git LFS if needed.

---

Happy coding! 🧑‍💻
**Maintainer:** `apdaniswara-sys`
**Project:** `OJD_ObjectDetection`
