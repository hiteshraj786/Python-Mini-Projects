# Import pyautogui for taking screenshot
import pyautogui 

# Import all necessary classes/functions from tkinter
from tkinter import *


# Function to take a screenshot and save it to user-specified path
def take_ss():
    # Get folder path from the entry box
    add_data = entry.get()

    # Prepare full file path for saving screenshot as test12.png
    path = add_data + "\\test12.png"

    # Print the path in console for debugging
    print(path)

     # Take screenshot using pyautogui
    ss = pyautogui.screenshot()
    # Save the screenshot to the specified path   # Save the screenshot to the specified path
    ss.save(path)

# Create main GUI window
win = Tk()
win.title("Screenshot Taker")  # Title of the window
win.geometry("600x600")       # Set window size (width x height)
win.config(bg="yellow")       # Set background color of the window
win.resizable(False,False)    # Disable window resizing (fixed size)

# Create an Entry widget for the user to input path where screenshot will be saved
entry = Entry(win, font=("Time New Roman", 20, "bold"))
entry.place(x=20, y=10, height=100, width=560)  # Position and size of Entry box

# Create a Button to trigger screenshot function
button = Button(win,text = "Done",font = ("Time New Roman",40,"bold"),relief=RAISED,cursor="plus",command=take_ss)
button.place(x=150,y=225,height=150,width=300)


# Run the main GUI loop (keeps window open and responsive)
win.mainloop()