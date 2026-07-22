# Desktop Notifier Using Python 🔔💻

This mini-project demonstrates how to create a simple desktop notification system using the `plyer` library in Python. It periodically sends reminders to the user (e.g., to take a rest for mental health).

## 🚀 Features
- Uses `plyer.notification` to trigger native OS desktop notifications.
- Displays a custom title, message, and icon (`rest.ico`).
- Runs continuously in a loop, triggering notifications at a set interval.

## 🛠️ Prerequisites
You will need to install the `plyer` library.

1. **Install Python Library:**
   ```bash
   pip install plyer
   ```

2. **Icon Configuration:**
   - The script uses an absolute path for the application icon (`rest.ico`). You might need to update the `app_icon` path in `main.py` if you move the project.

## 💻 How to Run
1. Open a terminal in the project directory.
2. Run the script normally:
   ```bash
   python main.py
   ```
3. The script will sleep for a specified time (e.g., 10 seconds) and then pop up a Windows notification reminding you to take a rest.

### 🕵️‍♂️ Run in Background
To run this file in the background (so the terminal window doesn't stay open), run the following command in the Command Prompt or PowerShell:
```bash
pythonw main.py
```
*(To stop it, you will have to find the pythonw.exe process in your Task Manager and end it).*

## 📂 Code Overview
The code uses an infinite `while True:` loop paired with `time.sleep()` to trigger `notification.notify()` at regular intervals.
