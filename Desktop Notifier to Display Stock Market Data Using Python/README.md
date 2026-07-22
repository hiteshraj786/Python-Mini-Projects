# Desktop Notifier for Stock Market Data 📈🔔

This mini-project demonstrates how to fetch live stock market data using the `yfinance` library and display it as a desktop notification using the `plyer` library in Python.

## 🚀 Features
- Fetches real-time stock data (Current Price, Day Low, Day High) for a specific ticker (e.g., MSFT) from Yahoo Finance.
- Displays this data as a native Windows desktop notification.
- Refreshes and triggers the notification periodically on an infinite loop.

## 🛠️ Prerequisites
You'll need `yfinance` to grab the stock data and `plyer` for the notifications.

1. **Install Python Libraries:**
   ```bash
   pip install yfinance plyer
   ```

## 💻 How to Run
1. Open a terminal in the project directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. A Windows notification displaying Microsoft's (MSFT) current stock details will pop up.
4. The loop will sleep for 20 seconds and then display another notification.

### 🕵️‍♂️ Run in Background
To run this application silently in the background (so the terminal window doesn't stay open), run the following command:
```bash
pythonw main.py
```
*(To stop it, locate the `pythonw.exe` process in Task Manager and end it).*

## 📂 Code Overview
The script initializes a `yf.Ticker` object to grab `.info` data. It then enters a `while True:` loop, formatting a notification message with current market stats, and waits `20` seconds before the next update using `time.sleep()`.
