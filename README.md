# ✊ Hand Gesture Scroll Control — Python + OpenCV

A hands-free scroll controller using Python, OpenCV, and MediaPipe. This tool allows you to scroll up or down using **fist gestures**, making it ideal for scenarios like reading while eating, multitasking, or accessibility use.

---

## 🚀 What It Does

- ✋ **Open hands** → Idle mode (no scroll)
- ✊ **Left hand fist** → Scroll **up**
- ✊ **Right hand fist** → Scroll **down**
- ❌ **Cross both hands** → Exit the program

> The system is designed for **daily use** and comfort — no arm movement required, just simple hand positions.

---

## 🧠 How It Works

1. Captures webcam feed using OpenCV
2. Detects hand landmarks using **MediaPipe**
3. Identifies:
   - Open hands → Idle mode
   - Fist gesture + hand side → Triggers scroll
   - Cross gesture (X) → Safely exits the script
4. Sends scroll commands via **PyAutoGUI**

---

## 🛠 Tech Stack

- Python 3.8+
- OpenCV
- MediaPipe
- PyAutoGUI
- Numpy

---

## 🖥️ Installation & Run

```bash
git clone https://github.com/yourusername/hand-scroll-control.git
cd hand-scroll-control
pip install -r requirements.txt
python hand_scroll.py
