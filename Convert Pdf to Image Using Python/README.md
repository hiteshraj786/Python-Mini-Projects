# Convert PDF to Image Using Python 📄➡️🖼️

This mini-project demonstrates how to convert a multi-page PDF document into individual image files (JPEGs) using the `pdf2image` library and Poppler in Python.

## 🚀 Features
- Reads an input PDF file (`FOT.pdf`).
- Converts every page of the PDF into a separate JPEG image.
- Automatically numbers and saves the output images (e.g., `new1.jpg`, `new2.jpg`, etc.).

## 🛠️ Prerequisites
You need the `pdf2image` library and the Poppler binaries installed on your system.

1. **Install Python Library:**
   ```bash
   pip install pdf2image
   ```

2. **Poppler Setup:**
   - This project includes a local copy of Poppler (`poppler-24.08.0`). 
   - The script sets the `poppler_path` directly to the local directory. If you move this project to another location, make sure to update the `poppler_path` argument in `main.py` so it points to the correct absolute path of the `poppler\Library\bin` folder.

## 💻 How to Run
1. Place your target PDF file in the same directory (or update the filename in `main.py`).
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will iterate through the pages of the PDF and save each one as a `.jpg` image in the current directory.

## 📂 Code Overview
The code leverages the `convert_from_path` function from `pdf2image` to parse the PDF, returning a list of image objects which are then iterated over and saved using the standard PIL `.save()` method.
