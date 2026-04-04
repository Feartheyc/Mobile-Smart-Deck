# Tokyo Night Remote Deck 🎮

A custom, glassmorphism-styled local web dashboard to control your PC from your phone. Built with Python, Flask, and Socket.IO.

## Features
* **Live PC Stats:** Monitor CPU, RAM, and GPU.
* **Media Controls:** Live cover art fetching, play/pause, and a working seek bar.
* **App Launchers:** Quick launch Discord, Brave, Steam, Terminal, etc.
* **Discord Integration:** Global hotkeys for Mute, Deafen, and Screen Share.
* **Audio Switcher:** Instantly toggle between headphones and speakers.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install flask flask-socketio psutil requests winsdk pyautogui`
3. Download [NirCmd](https://www.nirsoft.net/utils/nircmd.html) and place `nircmd.exe` in the project folder (required for audio switching).
4. **Important:** Open `app.py` and update the application file paths to match your Windows username.
5. Run the server: `python app.py`
6. Open your phone's browser and go to your PC's IP address on port 5000 (e.g., `http://192.168.1.15:5000`).

## License
MIT License
