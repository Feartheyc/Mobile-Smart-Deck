from flask import Flask, render_template
from flask_socketio import SocketIO
import psutil
import requests
import time
import threading
import subprocess
import asyncio
import base64
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager
import winsdk.windows.storage.streams as streams
import pyautogui

# --- CONFIGURATION ---
is_on_dac = False
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# --- WINDOWS MEDIA FETCHING ---
async def get_media_info():
    try:
        manager = await GlobalSystemMediaTransportControlsSessionManager.request_async()
        session = manager.get_current_session()
        
        if not session:
            return {"art": None, "pos": 0, "dur": 0}
            
        # Get Timeline (Progress)
        timeline = session.get_timeline_properties()
        pos = timeline.position.total_seconds() if timeline else 0
        dur = timeline.end_time.total_seconds() if timeline else 0
        
        # Get Cover Art
        info = await session.try_get_media_properties_async()
        b64_image = None
        
        if info and info.thumbnail:
            stream = await info.thumbnail.open_read_async()
            reader = streams.DataReader(stream)
            await reader.load_async(stream.size)
            buffer = reader.read_buffer(reader.unconsumed_buffer_length)
            b64_image = f"data:image/jpeg;base64,{base64.b64encode(bytes(buffer)).decode('utf-8')}"
            
        return {"art": b64_image, "pos": pos, "dur": dur}
    except Exception:
        return {"art": None, "pos": 0, "dur": 0}

# --- BACKGROUND DATA LOOP ---
def background_data_fetch():
    while True:
        # 1. PC Stats
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        
        # 2. Weather (Mumbai)
        weather_api = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
        try:
            w_data = requests.get(weather_api).json()
            temp = w_data['current_weather']['temperature']
        except:
            temp = "--"

        # 3. Media Info
        try:
            media_info = asyncio.run(get_media_info())
            cover_art_url = media_info["art"] if media_info["art"] else ""
            track_pos = media_info["pos"]
            track_dur = media_info["dur"]
        except:
            cover_art_url = ""
            track_pos, track_dur = 0, 0

        # Send to Phone
        socketio.emit('update_ui', {
            'cpu': cpu, 
            'ram': ram, 
            'temp': temp,
            'cover_art': cover_art_url,
            'track_pos': track_pos,
            'track_dur': track_dur
        })
        time.sleep(2)

# --- COMMAND HANDLER ---
@socketio.on('button_pressed')
def handle_button(action):
    global is_on_dac
    print(f"Action Received: {action}")
    
    # Page 1: App Launchers
    if action == 'launch_discord':
        #UPDATE THIS PATH to your local Discord installation
        subprocess.Popen(r"")
    elif action == 'launch_brave':
        #UPDATE THIS PATH to your local Brave or any browser's installation
        subprocess.Popen(r"")
    elif action == 'launch_whatsapp':
        subprocess.Popen(["cmd", "/c", "start", "https://web.whatsapp.com"], shell=True)
    elif action == 'launch_explorer':
        subprocess.Popen(["explorer.exe"])
    elif action == 'launch_terminal':
        subprocess.Popen(["cmd", "/c", "start", "pwsh.exe"], shell=True)
    elif action == 'launch_steam':
        subprocess.Popen(["cmd", "/c", "start", "steam://open/main"], shell=True)

    # Audio Switcher (Fixed Toggle)
    elif action == 'switch_audio':
        if is_on_dac:
            subprocess.Popen(["nircmd.exe", "setdefaultsounddevice", "ZEB Speakers"])
            print("Switched to Speakers")
        else:
            subprocess.Popen(["nircmd.exe", "setdefaultsounddevice", "Razer Headphones"])
            print("Switched to DAC")
        is_on_dac = not is_on_dac

    # Media Controls
    elif action == 'media_play':
        pyautogui.press('playpause')
    elif action == 'media_next':
        pyautogui.press('nexttrack')
    elif action == 'media_prev':
        pyautogui.press('prevtrack')

    # Page 2: Discord Hotkeys (Using F15-F18 to avoid browser conflicts)
    elif action == 'discord_mute':
        pyautogui.press('f15')
    elif action == 'discord_deafen':
        pyautogui.press('f16')
    elif action == 'discord_screen':
        pyautogui.press('f17')
    elif action == 'discord_ptt':
        pyautogui.press('f18')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=background_data_fetch, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)