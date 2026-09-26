# Virtual Mouse Using Hand Gestures - FIXED VERSION 🎮

This is the complete, working version of the Virtual Mouse project with all fixes applied.

---

## 📦 What's Included

- ✅ **Virtual_Mouse.py** - Main program (uses MediaPipe)
- ✅ **Virtual_Mouse_cvzone.py** - Alternative version (uses cvzone - more reliable)
- ✅ **util.py** - Helper functions
- ✅ **requirements.txt** - Dependencies for MediaPipe version
- ✅ **requirements_cvzone.txt** - Dependencies for cvzone version
- ✅ **README.md** - This file
- ✅ **INSTALLATION_GUIDE.md** - Detailed setup instructions
- ✅ **VS Code configuration** - Pre-configured settings

---

## 🚀 Quick Start (3 Steps)

### Step 1: Open in VS Code
1. Extract this folder to your Desktop
2. Open VS Code
3. File → Open Folder → Select this folder

### Step 2: Setup Environment
Open VS Code terminal (`` Ctrl+` ``) and run:

```bash
# Create virtual environment
python -m venv venv

# Activate it (Command Prompt)
venv\Scripts\activate

# OR (PowerShell - if you get an error, see INSTALLATION_GUIDE.md)
venv\Scripts\Activate.ps1
```

### Step 3: Install & Run

**Choose ONE option:**

#### Option A: Use MediaPipe (Original)
```bash
pip install -r requirements.txt
python Virtual_Mouse.py
```

#### Option B: Use cvzone (More Reliable)
```bash
pip install -r requirements_cvzone.txt
python Virtual_Mouse_cvzone.py
```

---

## 🎯 Gestures

Once running:
- **Move cursor**: Move your index finger
- **Left Click**: Bend index finger (keep others extended)
- **Right Click**: Bend middle finger (keep others extended)
- **Double Click**: Bend both index & middle fingers (far apart)
- **Screenshot**: Bend both index & middle fingers (close together)
- **Quit**: Press 'q' on keyboard

---

## ⚠️ If You Get Errors

### MediaPipe Error: "module has no attribute 'solutions'"
Switch to the cvzone version:
```bash
pip uninstall mediapipe -y
pip install -r requirements_cvzone.txt
python Virtual_Mouse_cvzone.py
```

### PowerShell Execution Policy Error
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Webcam Not Working
- Close other apps using the webcam (Zoom, Teams, etc.)
- Check Windows Camera app works
- Grant camera permissions if prompted

---

## 📁 File Descriptions

| File | Purpose |
|------|---------|
| `Virtual_Mouse.py` | Main program using MediaPipe |
| `Virtual_Mouse_cvzone.py` | Alternative using cvzone library |
| `util.py` | Angle and distance calculation functions |
| `requirements.txt` | Python packages for MediaPipe version |
| `requirements_cvzone.txt` | Python packages for cvzone version |
| `.vscode/` | VS Code configuration (auto-setup) |

---

## 💡 Which Version Should I Use?

**Use MediaPipe if:**
- You want the original version
- You're comfortable fixing installation issues

**Use cvzone if:**
- MediaPipe keeps giving errors
- You want simpler, more reliable code
- You're new to computer vision

Both versions work identically - they just use different hand tracking libraries!

---

## 🛠️ System Requirements

- **Python**: 3.8 - 3.11 (you have 3.10.12 ✓)
- **OS**: Windows 10/11
- **Webcam**: Any USB or built-in camera
- **RAM**: 4GB minimum

---

## 📖 Need More Help?

See **INSTALLATION_GUIDE.md** for:
- Detailed troubleshooting
- Step-by-step installation
- Common errors and solutions
- Tips for best performance

---

## 🎉 That's It!

Your virtual mouse should be working now. Enjoy hands-free computing!

**Created: September 26, 2026**
**Fixed and optimized for Python 3.10 + Windows 11**
