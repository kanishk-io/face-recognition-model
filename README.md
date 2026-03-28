# Face Recognition System

A real-time face recognition desktop application built with Python. Uses a webcam feed to detect and identify faces against a database of known individuals — displaying live bounding boxes and recognized names in a GUI window.

**Repo:** [github.com/kanishk-io/face-recognition-model](https://github.com/kanishk-io/face-recognition-model)

---

## What It Does

- Opens your webcam in real time
- Detects all faces in each frame
- Compares them against a folder of known person images
- Draws a bounding box and name label on each recognized face
- Shows two live lists — faces currently in frame and all faces recognized in the session

---

## Features

- Real-time face detection and recognition via webcam
- Loads known faces from a local `persons/` folder automatically
- Horizontally flipped feed (mirror mode) for natural interaction
- Live **In Frame Faces** panel — updates every frame
- Cumulative **All Recognized Faces** panel — persists across the session
- Unknown faces labeled as `Unknown`
- Clean Tkinter GUI with Stop button

---

## Tech Stack

| | |
|---|---|
| Language | Python 3 |
| Face Recognition | `face_recognition` (dlib-based) |
| Computer Vision | OpenCV (`cv2`) |
| GUI | Tkinter + PIL |
| Image Processing | Pillow |

---

## Project Structure

```
face-recognition-model/
├── project4.py        # Main application
├── persons/           # Folder of known face images
│   ├── john.jpg
│   ├── jane.png
│   └── ...
└── README.md
```

> Image filename = person's ID/name shown on screen.
> Example: `kanishk.jpg` → displays `kanishk` when recognized.

---

## How to Run

```bash
git clone https://github.com/kanishk-io/face-recognition-model.git
cd face-recognition-model

# Install dependencies
pip install face_recognition opencv-python pillow

# Add known face images to the persons/ folder
# Filename = the name you want displayed (e.g. kanishk.jpg)

# Run
python project4.py
```

> **Note:** `face_recognition` requires `dlib` which may need CMake and a C++ compiler on Windows. On Linux/Mac it installs cleanly.

---

## How It Works

```
Webcam Frame
    ↓
face_recognition.face_locations()   → finds all face bounding boxes
    ↓
face_recognition.face_encodings()   → converts each face to a 128-d vector
    ↓
face_recognition.compare_faces()    → compares against known encodings
    ↓
Match found → draw box + name label
No match    → label as "Unknown"
    ↓
Display in Tkinter GUI
```

---

## Project Context

Built as part of an Artificial Intelligence / Computer Vision course to demonstrate real-time image processing, facial encoding, vector comparison, and desktop GUI integration in Python.

---

## License

MIT
