# Tokyo Night Smart Deck 🎮

A custom, glassmorphism-styled local web dashboard to control your PC from your phone. Built with Python, Flask, and Socket.IO.

## Features
* **Live PC Stats:** Monitor CPU, RAM, and GPU.
* **Media Controls:** Live cover art fetching, play/pause, and a working seek bar.
* **App Launchers:** Quick launch Discord, Brave, Steam, Terminal, etc.
* **Discord Integration:** Global hotkeys for Mute, Deafen, and Screen Share.
* **Audio Switcher:** Instantly toggle between headphones and speakers.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Download [NirCmd](https://www.nirsoft.net/utils/nircmd.html) and place `nircmd.exe` in the project folder (required for audio switching).
4. **Important:** Open `app.py` and update the application file paths to match your Windows username.
5. Run the server: `python app.py`
6. Open your phone's browser and go to your PC's IP address on port 5000 (e.g., `http://192.168.1.15:5000`).

## ⚙️ Run Automatically in Background (Windows)
To make the deck run silently on startup without leaving a black terminal window open on your taskbar:

1. Create a new file in your project folder named `start_deck.vbs`.
2. Paste the following code into it and **update the directory path**:
3. Make a shortcut to this file and place it `shell:startup` folder
   ```vbscript
   Set objShell = CreateObject("Wscript.Shell")
   ' Update this to the exact path where you cloned the repository
   objShell.CurrentDirectory = "C:\Users\YOUR_USERNAME\Remote-deck"
   ' Runs Python windowless
   objShell.Run "pythonw.exe app.py", 0, False

Images:
<img width="1600" height="720" alt="image" src="https://github.com/user-attachments/assets/74872a8a-a00b-41c2-906f-a3cfc0465e95" />

<img width="1600" height="1201" alt="image" src="https://github.com/user-attachments/assets/9d1cac4a-2ae4-44ef-ae6d-34e7b3050911" />

## 🚀 Planned Features for later!!
This project is actively growing! Here are some features planned for future updates. If you want to contribute, feel free to fork the repo and tackle one of these:

* **Master Volume Slider:** A draggable UI slider on the dashboard to control the PC's main volume, not just swap devices.
* **OBS Studio Integration:** Dedicated hotkeys to switch scenes, toggle mic/cam, and start/stop recording in OBS.
* **Discord Remote Control** Dedicated hotkeys to mute, unmute, turn camera on/off, share your screen and push to talk
* **PC Power Controls:** A secure sub-menu to remotely Sleep, Restart, or Shut Down the PC.
* **Custom Theme Engine:** Allow users to easily swap from the default *Tokyo Night* theme to other popular palettes (Dracula, Nord, Catppuccin) via a CSS toggle.
* **Settings Page (UI):** A web interface to let users add new app buttons or change Discord hotkeys without having to edit the `app.py` code directly.

## License
MIT License
