# AI Voice Assistant (Python)

Voice assistant capable of continuous voice recognition, real-time Wikipedia searches, system telemetry commands, and cross-platform browser synthesis.

## Features
- **Dual Execution Modes**:
  1. **Flask Voice Studio**: Browser-based speech synthesis & recognition (works out of the box on Windows, macOS, Linux).
  2. **Desktop Voice Assistant**: CLI execution via `pyttsx3` and `speech_recognition`.
- **Command Categories**: Time/Date, Wikipedia knowledge extraction, system metrics, jokes, and web navigation.

## Quick Start
```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000` to interact with your Voice Assistant.
