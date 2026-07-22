# Digital Clock Using Python (Tkinter) 🕰️🐍

This mini-project is a beautiful, fully functional Digital Clock built with Python's `tkinter` library. It displays the current time (Hour, Minute, Second, AM/PM) and date (Day, Month, Year) on top of a custom background image. 

It is also configured to be easily compiled into a standalone Windows executable (`.exe`) via PyInstaller!

## 🚀 Features
- **Real-Time Clock:** Displays accurate local time and date, updating every 1000ms.
- **Custom UI:** Uses a customized background image (`background.jpg`) for a more aesthetic look.
- **PyInstaller Ready:** Includes the logic (`_MEIPASS`) required to locate external assets (like images) when bundled into a single `.exe` file.

## 🛠️ Prerequisites
You need the Pillow library for image processing. If you wish to build an `.exe`, you will also need PyInstaller.

1. **Install Dependencies:**
   ```bash
   pip install pillow pyinstaller
   ```

## 💻 How to Run
1. Make sure `background.jpg` is in the same directory as `main.py`.
2. Run the script directly via Python:
   ```bash
   python main.py
   ```

### 📦 Build as an Executable (.exe)
To compile this script into a standalone `.exe` without a console window (and pack the background image inside), run:
```bash
pyinstaller --onefile --noconsole --add-data "background.jpg;." main.py
```
After the build finishes, you'll find `main.exe` in the `dist` folder.

## 📂 Code Overview
The code uses `tkinter.Label` to create text placeholders for hours, minutes, date, etc. The `date_time()` function fetches the current time using the `datetime` module and updates the Labels using `.config(text=...)`. The function recursively calls itself using `window.after(1000, date_time)` to keep the clock ticking continuously.
