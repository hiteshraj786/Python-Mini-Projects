# Automate WhatsApp Message Using Python 📱🤖

This mini-project demonstrates how to automate sending WhatsApp messages using the `pywhatkit` library in Python. It schedules a message to be sent to a specific phone number at a given time.

## 🚀 Features
- Uses `pywhatkit` to interface with WhatsApp Web.
- Automatically opens the browser, types the specified message, and sends it at the scheduled time.

## 🛠️ Prerequisites
To run this script, you need to install the `pywhatkit` library.

1. **Install Python Library:**
   ```bash
   pip install pywhatkit
   ```

2. **WhatsApp Web Setup:**
   - Make sure you are logged into [WhatsApp Web](https://web.whatsapp.com/) on your default browser before running the script, as it relies on the browser to send the message.

## 💻 How to Run
1. Open `main.py` and modify the phone number, message, and the scheduled time (hours and minutes in 24-hour format).
2. Run the script:
   ```bash
   python main.py
   ```
3. A new browser tab will open automatically just before the scheduled time, and the message will be dispatched.

## 📂 Code Overview
The `main.py` file uses `pywhatkit.sendwhatmsg(phone_no, message, time_hour, time_minute)` to automate the message dispatch.
