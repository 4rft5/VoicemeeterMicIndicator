import voicemeeterlib
import pystray
from PIL import Image
import threading
import time
import keyboard
import sys
import os

#define state of mic
mode = "Muted"

#get the current mic mute state
def get_microphone_mute_state(vm):
    #replace 'strip-0' with the correct strip for your microphone
    return vm.strip[0].mute

def resource_path(relative_path):
    """Get absolute path to resource, works for development and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

images = {
    "Muted": Image.open(resource_path('muted.png')),
    "Unmuted": Image.open(resource_path('unmuted.png'))
}

#lock thread
lock = threading.Lock()

def update_icon(icon, vm):
    global mode
    #get current mute state for icon
    current_state = get_microphone_mute_state(vm)
    #update state and icon
    mode = "Muted" if current_state else "Unmuted"
    icon.icon = images[mode]
    icon.title = mode

def toggle_mode(icon, item):
    with lock:
        #toggle mic state
        with voicemeeterlib.api("banana") as vm:
            current_state = get_microphone_mute_state(vm)
            vm.strip[0].mute = not current_state
            update_icon(icon, vm)  #update icon

def on_quit(icon, item):
    icon.visible = False
    icon.stop()
    sys.exit()

def setup_icon():
    icon = pystray.Icon("test_icon")
    with voicemeeterlib.api("banana") as vm:
        update_icon(icon, vm)  #set initial icon
    icon.menu = pystray.Menu(
        pystray.MenuItem("Toggle Mode", toggle_mode),
        pystray.MenuItem("Quit", on_quit)
    )
    return icon

def monitor_hotkey():
    last_time = 0
    debounce_time = 0.5
    while True:
        if keyboard.is_pressed('f24'):
            current_time = time.time()
            if current_time - last_time > debounce_time:
                toggle_mode(icon, None)
                last_time = current_time
        time.sleep(0.01)

if __name__ == "__main__":
    icon = setup_icon()

    #monitor for hotkey
    hotkey_thread = threading.Thread(target=monitor_hotkey, daemon=True)
    hotkey_thread.start()

    icon.run()
