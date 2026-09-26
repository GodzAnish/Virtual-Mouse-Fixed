# Complete Installation Guide - Virtual Mouse

## Table of Contents
1. [First Time Setup](#first-time-setup)
2. [Running the Program](#running-the-program)
3. [Troubleshooting](#troubleshooting)
4. [Performance Tips](#performance-tips)

---

## First Time Setup

### Step 1: Extract and Open Project

1. Extract the `Virtual-Mouse-Fixed` folder to your Desktop
2. Open **Visual Studio Code**
3. Click **File** → **Open Folder**
4. Navigate to and select the `Virtual-Mouse-Fixed` folder
5. Click **Select Folder**

### Step 2: Install Recommended Extensions

When VS Code opens, you should see a popup asking to install recommended extensions. Click **Install All**. This installs:
- Python (by Microsoft)
- Pylance (by Microsoft)
- Jupyter (by Microsoft)

If you don't see the popup:
1. Press `Ctrl+Shift+X` to open Extensions
2. Search for "Python" and install the Microsoft one
3. Search for "Pylance" and install it

### Step 3: Open Terminal

Press `` Ctrl+` `` (backtick) or click **View** → **Terminal**

### Step 4: Create Virtual Environment

In the terminal, type:
```bash
python -m venv venv
```

Wait for it to complete (takes 30-60 seconds).

### Step 5: Activate Virtual Environment

**For Command Prompt (Recommended):**
```bash
venv\Scripts\activate
```

**For PowerShell:**
```bash
venv\Scripts\Activate.ps1
```

**If you get a PowerShell error:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

**You MUST see `(venv)` at the start of your terminal line!**

✅ Correct:
```
(venv) C:\Users\Asus\Desktop\Virtual-Mouse-Fixed>
```

❌ Wrong:
```
C:\Users\Asus\Desktop\Virtual-Mouse-Fixed>
```

### Step 6: Install Dependencies

Choose **ONE** option:

#### Option A: MediaPipe Version (Original)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- opencv-python (camera and image processing)
- mediapipe (hand tracking)
- pyautogui (mouse control)
- pynput (mouse buttons)
- numpy (calculations)
- protobuf (MediaPipe dependency)

#### Option B: cvzone Version (More Reliable)

```bash
pip install --upgrade pip
pip install -r requirements_cvzone.txt
```

This installs:
- opencv-python
- cvzone (simplified hand tracking)
- pyautogui
- pynput
- numpy

**Recommendation**: Try Option A first. If you get "no attribute 'solutions'" error, use Option B instead.

### Step 7: Verify Installation

**For MediaPipe:**
```bash
python -c "import mediapipe as mp; print('MediaPipe:', mp.__version__); print('Has solutions:', hasattr(mp, 'solutions'))"
```

Should show:
```
MediaPipe: 0.10.33
Has solutions: True
```

**For cvzone:**
```bash
python -c "from cvzone.HandTrackingModule import HandDetector; print('cvzone works!')"
```

Should show:
```
cvzone works!
```

---

## Running the Program

### Method 1: From Terminal (Recommended)

**MediaPipe version:**
```bash
python Virtual_Mouse.py
```

**cvzone version:**
```bash
python Virtual_Mouse_cvzone.py
```

### Method 2: Using F5 (Debug Mode)

1. Open `Virtual_Mouse.py` (or `Virtual_Mouse_cvzone.py`)
2. Press `F5`
3. If asked, select "Python File"

### Method 3: Right-Click Run

1. Right-click in the Python file
2. Select "Run Python File in Terminal"

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'cv2'"

**Cause**: Virtual environment not activated or packages not installed.

**Fix**:
```bash
# Make sure venv is activated (you should see (venv) in terminal)
venv\Scripts\activate

# Reinstall packages
pip install -r requirements.txt
```

### Issue: "AttributeError: module 'mediapipe' has no attribute 'solutions'"

**Cause**: MediaPipe installation is corrupted or wrong version.

**Fix Option 1 - Reinstall MediaPipe:**
```bash
pip uninstall mediapipe protobuf -y
pip cache purge
pip install protobuf==3.20.3
pip install mediapipe==0.10.33 --no-cache-dir --force-reinstall
```

**Fix Option 2 - Switch to cvzone:**
```bash
pip uninstall mediapipe -y
pip install -r requirements_cvzone.txt
python Virtual_Mouse_cvzone.py
```

### Issue: "Webcam not detected" or Black Screen

**Fix**:
1. Close all other apps using the webcam (Zoom, Teams, Camera app)
2. Check if Windows Camera app works
3. Restart your computer
4. Try a different USB port (if using external webcam)
5. Grant camera permissions in Windows Settings

### Issue: PowerShell Script Execution Error

**Error message:**
```
running scripts is disabled on this system
```

**Fix**:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Type `Y` and press Enter when asked.

### Issue: Import Errors After Installation

**Fix**:
1. Make sure you're using the correct Python interpreter:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose the one that shows `.\venv\Scripts\python.exe`

2. Reinstall packages:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: Program Freezes or Lags

**Fix**:
- Close other heavy applications
- Improve lighting in your room
- Move closer to webcam (2-3 feet away)
- Use a plain background
- Lower your screen resolution temporarily

### Issue: Gestures Not Recognized

**Fix**:
- Make sure your hand is well-lit
- Keep hand in center of camera view
- Make clear, distinct finger movements
- Make sure only ONE hand is visible
- Adjust `min_detection_confidence` in code (lower = more sensitive)

---

## Performance Tips

### For Better Accuracy:
1. **Lighting**: Use good lighting, face a window or lamp
2. **Background**: Plain, contrasting background works best
3. **Distance**: 2-3 feet from camera is optimal
4. **Hand position**: Keep hand centered in frame
5. **One hand**: System tracks only one hand

### For Better Speed:
1. Close unnecessary applications
2. Use wired webcam instead of wireless
3. Lower webcam resolution if possible
4. Close other browser tabs/apps

### Gesture Tips:
- Make **slow, deliberate** movements
- Hold gestures for 0.5 seconds
- Return to neutral position between gestures
- Keep fingers clearly separated

---

## Switching Between Versions

### Currently using MediaPipe, want to try cvzone:
```bash
pip install -r requirements_cvzone.txt
python Virtual_Mouse_cvzone.py
```

### Currently using cvzone, want to try MediaPipe:
```bash
pip install -r requirements.txt
python Virtual_Mouse.py
```

Both can coexist - just run the appropriate file!

---

## Uninstalling

To completely remove:
1. Close VS Code
2. Delete the `Virtual-Mouse-Fixed` folder
3. That's it! (virtual environment is self-contained)

---

## Getting Help

If you're still having issues:

1. **Check Python version:**
   ```bash
   python --version
   ```
   Should be 3.8-3.11

2. **List installed packages:**
   ```bash
   pip list
   ```

3. **Check if venv is activated:**
   Look for `(venv)` at start of terminal prompt

4. **Try the other version:**
   If MediaPipe fails, try cvzone and vice versa

---

## Quick Reference Commands

```bash
# Activate venv
venv\Scripts\activate

# Install MediaPipe version
pip install -r requirements.txt

# Install cvzone version
pip install -r requirements_cvzone.txt

# Run MediaPipe version
python Virtual_Mouse.py

# Run cvzone version
python Virtual_Mouse_cvzone.py

# Check what's installed
pip list

# Reinstall everything
pip install -r requirements.txt --force-reinstall
```

---

**Last Updated**: September 26, 2026  
**Tested On**: Windows 11, Python 3.10.12, VS Code
