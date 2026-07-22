# Create Split Screen Video Using Python 🎞️🔲

This mini-project demonstrates how to merge multiple video clips into a single split-screen layout using the `moviepy` library in Python.

## 🚀 Features
- Reads multiple input video files (up to 4 in this example).
- Extracts a specific subclip (e.g., the first 5 seconds) from each video.
- Arranges the videos into a 2x2 grid (split-screen).
- Renders and exports the combined layout into a new video file (`test.mp4`).

## 🛠️ Prerequisites
You need the `moviepy` library to process and manipulate the video files.

1. **Install Python Library:**
   ```bash
   pip install moviepy
   ```

## 💻 How to Run
1. Ensure you have 4 video files (`black.mp4`, `live.mp4`, `lord.mp4`, `tech.mp4`) in the same directory, or update the filenames in `main.py` to point to your own videos.
2. Run the script:
   ```bash
   python main.py
   ```
3. Wait for the rendering process to finish. The output split-screen video will be saved as `test.mp4`.

## 📂 Code Overview
The code uses `VideoFileClip` to load each video and `.subclip(0, 5)` to extract a 5-second segment. Then, `clips_array` is used to arrange the clips into a 2D array format (a 2x2 grid), which is then written to a new file.
