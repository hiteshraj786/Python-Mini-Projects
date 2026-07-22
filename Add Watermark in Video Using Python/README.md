# Add Watermark in Video Using Python 🎥💧

This mini-project demonstrates how to easily add a text watermark to a video using the powerful `moviepy` library in Python. It overlays a customized text clip onto an existing video and exports the result.

## 🚀 Features
- Reads an input video file (`lord.mp4`).
- Generates a customizable text watermark (e.g., "Hare Krishna") with specific font size and color.
- Positions the watermark at the center of the video for the entire duration.
- Renders and saves the composited output video (`test.mp4`).

## 🛠️ Prerequisites
To run this project, you need to install the `moviepy` library and `ImageMagick`.

1. **Install Python Library:**
   ```bash
   pip install moviepy
   ```

2. **Install ImageMagick:**
   - Download and install [ImageMagick](https://imagemagick.org/script/download.php) for Windows.
   - Note: The script explicitly sets the `IMAGEMAGICK_BINARY` path (e.g., `C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe`). Make sure to update this path according to your installation directory.

## 💻 How to Run
1. Place your input video file in the same directory and name it `lord.mp4` (or update the filename in `main.py`).
2. Run the script:
   ```bash
   python main.py
   ```
3. Once the processing is complete, the watermarked video will be saved as `test.mp4` in the project directory.

## 📂 Code Overview
The code uses `VideoFileClip` to load the video, `TextClip` to create the watermark text, and `CompositeVideoClip` to merge the two layers.
