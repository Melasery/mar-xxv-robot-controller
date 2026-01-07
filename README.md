# MAR-XXV Robot Controller: Closed-Loop AI Navigation

**Computer Vision | Embedded Systems | Robotics**

This project delivers a responsive, AI-driven control system for the MAR-XXV mobile robot platform. It integrates onboard computer vision for object detection with a low-latency web interface for teleoperation and telemetry streaming.

## System Architecture

- **Brain**: Raspberry Pi 4 running a multi-threaded Python control service.
- **Vision**: OpenCV-based pipeline for real-time lane tracking and object recognition (Haar Cascades/YOLO).
- **Control Interface**: FastAPI backend serving a React-based dashboard for live video feed (WebSocket) and joystick control.
- **Actuation**: Arduino slave controller handling PWM motor drive and encoder feedback via serial communication.

## Key Capabilities

- **Autonomous Navigation**: Lane following and obstacle avoidance logic.
- **Live Streaming**: Low-latency MJPEG stream over local network.
- **Remote Control**: Tablet-friendly web interface for manual override.

## Repository Structure

- `/server`: FastAPI backend and video processing services.
- `/client`: React frontend for control dashboard.
- `/firmware`: Arduino sketches for motor control.

---
*Part of the Computational Textiles portfolio.*
