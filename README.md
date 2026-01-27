# README for video_ascii_cmd.py

## Description

This repository is not add for my portifolio, but is funny

`video_ascii_cmd.py` is a Python script that converts video files into ASCII art and plays them directly in the terminal/command prompt. It uses OpenCV to process video frames, converts each frame to grayscale, and maps pixel intensities to ASCII characters for a retro, text-based video playback experience.

### Features
- Select video files via a file dialog (supports MP4, AVI, MOV, MKV, WMV).
- Adjustable ASCII character set and scaling for customization.
- Real-time playback with optional FPS limiting.
- Contrast adjustment for better visibility.
- Works in Windows Command Prompt (uses `cls` for screen clearing).

## Installation

### Prerequisites
- Python 3.x
- Windows OS (optimized for CMD; may work on other systems with adjustments)

### Dependencies
Install the required Python packages:

```bash
pip install opencv-python
```

Note: `tkinter` is included with Python standard library, so no additional installation is needed.

## Usage

1. Run the script:
   ```bash
   python video_ascii_cmd.py
   ```

2. A file dialog will open. Select a video file.

3. The video will start playing as ASCII art in the terminal. Press Ctrl+C to stop.

### Configuration
You can modify the following constants at the top of the script for customization:
- `ASCII_CHARS`: String of characters used for ASCII mapping (from darkest to lightest).
- `ESCALA`: Vertical scaling factor to correct aspect ratio in CMD.
- `LARGURA_CMD`: Width of the ASCII output (affects quality and performance).
- `FPS_LIMIT`: Set to `True` to limit playback to original video FPS; `False` for faster playback.
- `CONTRASTE`: Contrast multiplier for frame brightness.

## Notes
- Playback speed may vary based on terminal size and system performance.
- For best results, maximize the Command Prompt window.
- The script clears the screen frequently, so it's designed for terminal use only.