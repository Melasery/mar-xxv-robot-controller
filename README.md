# 🤖 MAR-XXV Robot Controller (Web-Based)

**MAR-XXV** is a **FastAPI-powered robot controller** designed for **real-time navigation** via a **web interface**. It supports:
- 🎥 **Live Streaming** (from Raspberry Pi Camera)
- 🎮 **Gamepad & Keyboard Control**
- 🗣 **Text-to-Speech (TTS)**
- 📡 **WebSocket Communication**



## **📌 Features**
- ✅ **Live Video Streaming** - View real-time footage from the robot.
- ✅ **Gamepad & Keyboard Support** - Control via buttons or a game controller.
- ✅ **Web-Based Control Panel** - Mobile-friendly UI with touch support.
- ✅ **Text-to-Speech (TTS)** - Type messages for the robot to speak.
- ✅ **WebSockets Communication** - Low-latency control signals.
- ✅ **Raspberry Pi Compatible** - Designed for embedded systems.



## **⚙️ Installation & Setup (For Raspberry Pi)**
### **1️⃣ Prerequisites**
Ensure your Raspberry Pi has:
- **Raspberry Pi OS (32-bit or 64-bit)**
- **Python 3.7+**
- **FastAPI for the web server**
- **WebSockets support**
- **RPi.GPIO (for motor control)**
- **OpenCV (for live video streaming)**

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/Melasery/mar-xxv-robot.git
cd mar-xxv-robot
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Web Server**
```bash
./run.sh
```
The server starts at `http://localhost:8000`.
If running on a Raspberry Pi, replace `localhost` with its IP address.

### **5️⃣ Access the Web Interface**
Open a browser and go to:
```cpp
http://<raspberry-pi-ip>:8000
```



## **🕹️ Usage Instructions**
### **Web Controls**
- Use the arrow keys or buttons to move the robot.
- Click "Text to Speech" to enter text and make the robot speak.
- The video feed streams live from the robot’s camera.

### **Gamepad Support**
- **PS4/Xbox Controller Compatible**
  - ⬆️ D-Pad Up → Move Forward
  - ⬇️ D-Pad Down → Move Backward
  - ⬅️ D-Pad Left → Turn Left
  - ➡️ D-Pad Right → Turn Right
  - X / A → Stop Movement

🎮 Ensure the controller is connected before launching the web interface.



## **📂 Project Structure**
```bash
/mar-xxv-robot
│── /static/                  # Static assets (CSS, JavaScript)
│    ├── style.css            # Stylesheet for UI
│    ├── script.js            # JavaScript for controls & WebSocket communication
│── /templates/               # HTML templates for rendering with FastAPI
│    ├── control_panel.html   # Main UI for robot control
│── /src/                     # Backend Python scripts
│    ├── server.py            # FastAPI WebSocket server & API routes
│    ├── motor_control.py     # GPIO motor control logic
│    ├── video_stream.py      # Camera streaming logic
│    ├── text_to_speech.py    # TTS function using gTTS & pygame
│── README.md                 # Main documentation
│── .gitignore                # Ignore unnecessary files
│── requirements.txt          # Python dependencies
│── run.sh                    # Shell script to start the server
```



## **🚀 Future Enhancements**
- 🎤 **Voice Control** - Enable control using voice commands.
- 🧠 **AI Object Detection** - Implement OpenCV for obstacle detection.
- 📡 **Cloud-Based Control** - Access via an online dashboard.
- 🎭 **Facial Recognition** - Identify users with AI.



## **📝 License & Credits**
This project is licensed under the **MIT License**.

Developed by: **Marouan El-Asery**
