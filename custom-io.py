import sounddevice as sd
import numpy as np
import soundfile as sf

# Define the duration of the recording in seconds
DURATION = 5
# Define the sampling rate
FS = 44100
# Define the devices
DEVICES = ["Line 1 (Virtual Audio Cable)", "Line 2 (Virtual Audio Cable)", "Line 3 (Virtual Audio Cable)"]

def record_from_device(device_name):
    device_info = sd.query_devices()
    device_id = None
    for i, device in enumerate(device_info):
        if device['name'] == device_name:
            device_id = i
            break

    if device_id is None:
        raise ValueError(f"No device found with name: {device_name}")

    print(f"Recording from {device_name} for {DURATION} seconds")
    recording = sd.rec(int(DURATION * FS), samplerate=FS, channels=1, device=device_id)
    sd.wait()  # Wait for the recording to finish
    print(f"Recording from {device_name} finished")

    # Save recording to a file
    sf.write(f'{device_name.replace(" ", "_")}_recording.wav', recording, FS)

for device in DEVICES:
    record_from_device(device)

# Recordings are saved as WAV files in the current working directory.
