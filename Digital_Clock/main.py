
from tkinter import *
import datetime
from PIL import Image, ImageTk
import os
import sys

# ======= Image Path Handling for PyInstaller EXE =======
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
img_path = os.path.join(BASE_DIR, 'background.jpg')
# run this command in cmd ---> pyinstaller --onefile --noconsole --add-data "background.jpg;." main.py


# ======= Time + Date Update Function =======
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_AMPM.config(text=am)

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    lab_date.config(text=date)
    lab_Month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200, date_time)

# ======= Tkinter Window =======
clock = Tk()
clock.title("       **** Digital Clock ****")
clock.geometry("1000x500")

# ======= Load and Set Background Image =======
bg_image = Image.open(img_path)
bg_image = bg_image.resize((1000, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(clock, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ======= Time Labels =======
lab_hr = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="#011C26", fg="yellow")
lab_hr.place(x=120, y=50, height=110, width=100)

lab_hr_txt = Label(clock, text="Hour", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_hr_txt.place(x=120, y=190, height=40, width=100)

lab_min = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="#011C26", fg="yellow")
lab_min.place(x=340, y=50, height=110, width=100)

lab_min_txt = Label(clock, text="Min", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_min_txt.place(x=340, y=190, height=40, width=100)

lab_sec = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="#011C26", fg="yellow")
lab_sec.place(x=560, y=50, height=110, width=100)

lab_sec_txt = Label(clock, text="Sec", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_sec_txt.place(x=560, y=190, height=40, width=100)

lab_AMPM = Label(clock, text="00", font=("Time New Roman", 50, "bold"), bg="#011C26", fg="yellow")
lab_AMPM.place(x=780, y=50, height=110, width=100)

lab_AMPM_txt = Label(clock, text="AM/PM", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_AMPM_txt.place(x=780, y=190, height=40, width=100)

# ======= Date Labels =======
lab_date = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="#011C26", fg="yellow")
lab_date.place(x=120, y=270, height=110, width=100)

lab_date_txt = Label(clock, text="Date", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_date_txt.place(x=120, y=410, height=40, width=100)

lab_Month = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="#011C26", fg="yellow")
lab_Month.place(x=340, y=270, height=110, width=100)

lab_Month_txt = Label(clock, text="Month", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_Month_txt.place(x=340, y=410, height=40, width=100)

lab_year = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="#011C26", fg="yellow")
lab_year.place(x=560, y=270, height=110, width=100)

lab_year_txt = Label(clock, text="Year", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_year_txt.place(x=560, y=410, height=40, width=100)

lab_day = Label(clock, text="00", font=("Time New Roman", 40, "bold"), bg="#011C26", fg="yellow")
lab_day.place(x=780, y=270, height=110, width=100)

lab_day_txt = Label(clock, text="Day", font=("Time New Roman", 20, "bold"), bg="#011C26", fg="yellow")
lab_day_txt.place(x=780, y=410, height=40, width=100)

# Start Clock Update
date_time()

# Start GUI
clock.mainloop()
