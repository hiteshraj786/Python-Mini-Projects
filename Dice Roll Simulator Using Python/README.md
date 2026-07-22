# Dice Roll Simulator Using Python 🎲🐍

This mini-project is a simple Graphical User Interface (GUI) application that simulates rolling two six-sided dice simultaneously. It is built using the `tkinter` and `Pillow` libraries.

## 🚀 Features
- Interactive GUI application with a large "ROLL" button.
- Displays two randomly generated dice faces side-by-side using real images (`dice1.png` to `dice6.png`).
- Instantly updates the dice images on every roll without reloading the application window.

## 🛠️ Prerequisites
You will need to install the Pillow library to handle image processing within Tkinter.

1. **Install Pillow:**
   ```bash
   pip install Pillow
   ```

*(Tkinter usually comes pre-installed with standard Python distributions).*

## 💻 How to Run
1. Make sure all the dice images (`dice1.png` through `dice6.png`) are in the same directory as the script.
2. Run the script:
   ```bash
   python main.py
   ```
3. A large window will appear showing two dice. Click the green **ROLL** button to randomly roll both dice again!

## 📂 Code Overview
The code initializes a `tk.Tk()` window. The `random.choice(dice)` function selects random PNGs, which are then converted to Tkinter-compatible images via `ImageTk.PhotoImage`. The images are packed into `Label` widgets and updated whenever the ROLL button triggers the `dice_roll()` callback function.
