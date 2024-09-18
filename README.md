# VoicemeeterMicIndicator
**A Python script which displays the status of a Voicemeeter input in the system tray.** 
<hr>
This script shows the current mute state of a Voicemeeter input on your taskbar using a system tray icon. The state is monitored and updated in real-time by interacting with the Voicemeeter API through the 

![Python Voicemeeter API](https://github.com/onyx-and-iris/voicemeeter-api-python).

<hr>

**Function**:

The Python script registers a listener event for a keypress (in my case, F24 mutes the input using Voicemeeter's Macro Buttons), and uses the API to confirm as such, before updating the icon on the system tray.  
This script uses the following libraries:

- `voicemeeterlib`
- `pystray`
- `Pillow`
- `keyboard`

<hr>

**Customization**:

- **Icons**: You can replace the icons for the mute/unmute states (must be 64x64 PNG images).
- **Input & Hotkey**: You can change the monitored input and customize the key being watched for toggling mute.

<hr>

**Usage**:

Install required libraries:
```
pip install voicemeeterlib pystray pillow keyboard
```
Ensure Voicemeeter is running.  
Run `MicIndicator.py`.

**Optional Usage**:

If you desire, you can package the script into an exe (for running in background or on startup):

```
pyinstaller --onefile --windowed --add-data "muted.png;." --add-data "unmuted.png;." --icon "icon.ico" MicIndicator.py
```
<hr>

![button](https://github.com/user-attachments/assets/abbb95c7-6b71-4ffc-afa0-edf6cb2337a0)

<hr>

**Eventual Idea**:

At some point, I'll go through and rewrite this a little bit to be just a simple taskbar indicator for toggle macros. I feel like having visuals for these things is a very helpful indicator to have. If there's a demand for it, let me know and I'll do it.
