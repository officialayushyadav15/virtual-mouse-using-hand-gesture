
# 🖱️ Virtual Mouse Using Hand Gestures with MediaPipe and OpenCV

This project implements a **virtual mouse controller** using your hand gestures, powered by **MediaPipe**, **OpenCV**, **PyAutoGUI**, and **Pynput**. The system captures real-time webcam video to detect and analyze hand landmarks to perform actions such as moving the mouse, left click, right click, double click, and taking a screenshot — all using intuitive gestures.

---

## 🛠️ Libraries Used

| Library       | Purpose |
|---------------|---------|
| `opencv-python` | Capture and display webcam video; render hand landmark overlay |
| `mediapipe`     | Real-time hand detection and tracking |
| `pyautogui`     | Programmatically control mouse pointer and perform actions |
| `pynput`        | For simulating mouse click actions |
| `numpy`         | Mathematical calculations for angle and distance |
| `random`        | To generate random label for screenshot files |

---

## 📷 How it Works

- **MediaPipe** detects **21 hand landmarks** in real-time.
- Gestures are recognized based on:
  - **Angle between joints**
  - **Distance between landmarks**
- These gestures are then mapped to mouse functions such as:
  - **Move cursor**
  - **Left click**
  - **Right click**
  - **Double click**
  - **Take screenshot**

---

---

## 🧠 Gesture Detection Explanation

Hand gesture detection in this project relies on two main techniques:
1. Tracking **21 key landmarks** using MediaPipe's hand tracking solution.
2. Computing **angles and distances** between key points to identify specific gestures.



### 🖐️ MediaPipe Hand Landmarks

The image below shows all 21 landmarks that MediaPipe detects in a hand. Each landmark corresponds to a specific joint or fingertip:

- Each finger has four key points (MCP, PIP, DIP, TIP).
- The **wrist** is landmark `0`, and **index finger tip** is `8`, which is crucial for cursor movement.

![MediaPipe Landmarks](mediapipehandgesture.jpeg)


### 📐 Angle Detection with `get_angle()`

To detect gestures like clicks, we need to check how fingers bend or straighten. This is done using angles between three consecutive landmarks.

For instance, if we take three points A, B, and C:
- The function `get_angle(a, b, c)` calculates the angle at point **B**.
- This is done by subtracting the angle between line AB and the x-axis from the angle between line BC and the x-axis.

This is useful for identifying gestures like pinching, tapping, or holding.

#### 📊 Example Illustration:

![Angle Detection Logic](fun_get_angle.jpg)

- **Angle 1** is the angle between vector **AB** and the x-axis.
- **Angle 2** is the angle between vector **BC** and the x-axis.
- The required angle used in gesture recognition is `Angle 1 - Angle 2`.

This mechanism allows the program to recognize the degree of bend in fingers like the index or thumb, which is used to infer clicks, movement, or screenshot gestures.



- MediaPipe provides precise hand tracking via its 21-point model.
- Angles are used to detect finger gestures:
  - Small angles between joints suggest bent fingers (used for clicks).
  - Larger distances between certain fingers can imply gestures like open hand (used for mouse movement or screenshots).

These combined techniques enable the hands to act like a virtual mouse, enabling contactless control.


---

## ✋ Gesture-to-Action Mapping

### 🖋️ Finger Position for Each Gesture

Below is a table showing how each finger behaves for the various actions. The cells contain the status of each finger (`Open` or `Close`) for the respective gesture:

| **Functionality**     | **Thumb** | **Index** | **Middle** | **Ring** | **Pinky** |
|-----------------------|-----------|-----------|------------|----------|-----------|
| **Move Mouse**        | Close      | Open      | Open       | Close    | Close     |
| **Left Click**        | Open      | Close      | Open      | Close    | Close     |
| **Right Click**       | Open      | Open     | Close       | Close    | Close     |
| **Double Click**      | Open      | Close      | Close       | Close     | Close      |
| **Screenshot**        | Open      | Open      | Close      | Close    | Open      |

### 📷 Gesture-to-Action Illustration

Here’s a clear visual representation of the gestures and finger movements for each action:

- **Move Mouse:**  
  - First two fingers straight, others curled.
  
- **Left Click:**  
  - Index finger up + thumb away + others curled.

- **Right Click:**  
  - Middle finger up + thumb away + others curled.
  
- **Double Click:**  
  - All fingers curled, index finger up + thumb away.

- **Screenshot:**  
  - Middle and ring fingers curled, others open.
---

## 🧪 Setup Instructions

### 🔧 1. Create and Activate Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate     # For Windows
# source myenv/bin/activate   # For macOS/Linux
````

### 📦 2. Install Requirements

```bash
pip install -r requirements.txt
```

### Requirements (`requirements.txt`)

```
opencv-python
mediapipe==0.10.0
pyautogui
pynput
numpy
```

> **Note:** Use **Python 3.10** for full compatibility with MediaPipe.

---

## ▶️ Run the Project

```bash
python virtual_mouse.py
```

Press `q` to quit the webcam window.

---

## 📹 Demo Video

[![Watch the video](https://img.youtube.com/vi/VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID_HERE)

---

## 📁 File Structure

```
virtual-mouse-gesture/
│
├── virtual_mouse.py              # Main application logic
├── util.py                       # Helper functions: angle & distance
├── fun_get_angle.jpg             # Image illustrating angle detection
├── mediapipehandgesture.jpeg     # MediaPipe hand landmark diagram
├── gesture_to_action_map.jpg     # Custom image mapping gestures to actions
├── requirements.txt              # All dependencies
└── README.md                     # You're reading it!
```

---

## 🧠 Concepts Highlighted

* **Computer Vision** with OpenCV
* **Hand Pose Estimation** with MediaPipe
* **Euclidean Distance** and **Angle Calculation**
* **Gesture Recognition**
* **System Automation**

---

## 💬 CLI Commands Reference

| Command                           | Purpose                        |
| --------------------------------- | ------------------------------ |
| `python -m venv myenv`            | Create virtual environment     |
| `myenv\Scripts\activate`          | Activate environment (Windows) |
| `pip install -r requirements.txt` | Install dependencies           |
| `python virtual_mouse.py`         | Run the project                |
| Press `q`                         | Quit webcam viewer             |

---



## 🔗 References

- 📘 [MediaPipe Hand Landmarker (Google AI)](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- 📘 [OpenCV Python (PyPI)](https://pypi.org/project/opencv-python/)
- 📘 [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)
- 📘 [Pynput Mouse Control](https://pynput.readthedocs.io/en/latest/mouse.html)
- 📘 [Python 3.10 Official Release](https://www.python.org/downloads/release/python-3100/)
- 📘 [NumPy (PyPI)](https://pypi.org/project/numpy/)

---



## 🙋‍♂️ About Me

I'm Ayush Yadav, a passionate developer with an interest in computer vision, automation, and innovative tech solutions.  
Always exploring new technologies and building things that matter.

### Let’s connect:

- 📧 **Email:** [officialayushyadav15@gmail.com](mailto:officialayushyadav15@gmail.com)
- 💼 **GitHub:** [@officialayushyadav15](https://github.com/officialayushyadav15)
- 🔗 **LinkedIn:** [Ayush Yadav](https://www.linkedin.com/in/ayush-yadav-408924230/)

---

## 🤝 Contributions

Feel free to open issues or submit pull requests. Any improvements or gesture additions are welcome!

---


### 🚀 Happy Coding and Gesture-Controlling! 👋
