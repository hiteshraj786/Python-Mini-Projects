# from tkinter import *
# import datetime
# from PIL import Image, ImageTk


# # print(datetime.datetime.now())

# def date_time():
#     time = datetime.datetime.now()
#     hr = time.strftime('%I')
#     mi = time.strftime('%M')
#     sec = time.strftime('%S')
#     am = time.strftime('%p')
#     lab_hr.config(text=hr)
#     lab_min.config(text=mi)
#     lab_sec.config(text=sec)
#     lab_AMPM.config(text=am)



#     date = time.strftime('%d')
#     month = time.strftime('%m')
#     year = time.strftime('%y')
#     day = time.strftime('%a')
#     lab_date.config(text=date)
#     lab_Month.config(text=month)
#     lab_year.config(text=year)
#     lab_day.config(text=day)

#     lab_hr.after(200,date_time)


# clock = Tk()

# clock.title("       **** Digital Clock ****")
# clock.geometry("1000x500")
# # clock.config(bg="yellow")

# #  Load background image
# bg_image = Image.open("background.jpg")  # Use the correct path if saved in another folder
# bg_image = bg_image.resize((1000, 500), Image.Resampling.LANCZOS)


# bg_photo = ImageTk.PhotoImage(bg_image)
# # Add this line to show background image
# bg_label = Label(clock, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Use bg of clock or bg_label to match background color
# bg_color = clock["bg"]

# #  **** Time *****
# lab_hr = Label(clock,text ="00",font=("Time New Roman",60,"bold"),bg="#011C26",fg="yellow")
# lab_hr.place(x=120,y=50,height=110,width=100)

# lab_hr_txt = Label(clock,text ="Hour",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow")
# lab_hr_txt.place(x=120,y=190,height=40,width=100)

# lab_min = Label(clock,text ="00",font=("Time New Roman",60,"bold"),bg="#011C26",fg="yellow")
# lab_min.place(x=340,y=50,height=110,width=100)

# lab_min_txt = Label(clock,text ="Min",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow")
# lab_min_txt.place(x=340,y=190,height=40,width=100)

# lab_sec = Label(clock,text ="00",font=("Time New Roman",60,"bold"),bg="#011C26",fg="yellow")
# lab_sec.place(x=560,y=50,height=110,width=100)

# lab_sec_txt = Label(clock,text ="Sec",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow")
# lab_sec_txt.place(x=560,y=190,height=40,width=100)



# lab_AMPM = Label(clock,text ="00",font=("Time New Roman",50,"bold"),bg="#011C26",fg="yellow")
# lab_AMPM.place(x=780,y=50,height=110,width=100)

# lab_AMPM_txt = Label(clock,text ="AM/PM",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow")
# lab_AMPM_txt.place(x=780,y=190,height=40,width=100)







# #   ****** Date ******

# lab_date = Label(clock,text ="00",font=("Time New Roman",60,"bold"),bg="#011C26",fg="yellow",bd=0, highlightthickness=0)
# lab_date.place(x=120,y=270,height=110,width=100)

# lab_date_txt = Label(clock,text ="Date",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_date_txt.place(x=120,y=410,height=40,width=100)



# lab_Month = Label(clock,text ="00",font=("Time New Roman",60,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_Month.place(x=340,y=270,height=110,width=100)

# lab_Month_txt = Label(clock,text ="Month",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_Month_txt.place(x=340,y=410,height=40,width=100)



# lab_year = Label(clock,text ="00",font=("Time New Roman",60,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_year.place(x=560,y=270,height=110,width=100)

# lab_year_txt = Label(clock,text ="Year",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_year_txt.place(x=560,y=410,height=40,width=100)



# lab_day = Label(clock,text ="00",font=("Time New Roman",40,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_day.place(x=780,y=270,height=110,width=100)

# lab_day_txt = Label(clock,text ="Day",font=("Time New Roman",20,"bold"),bg="#011C26",fg="yellow", bd=0, highlightthickness=0)
# lab_day_txt.place(x=780,y=410,height=40,width=100)



# date_time()

# clock.mainloop()




# from tkinter import *
# from PIL import Image, ImageTk
# import datetime

# def update_time():
#     now = datetime.datetime.now()

#     hr = now.strftime('%I')
#     mi = now.strftime('%M')
#     sec = now.strftime('%S')
#     am = now.strftime('%p')
#     date = now.strftime('%d')
#     month = now.strftime('%m')
#     year = now.strftime('%y')
#     day = now.strftime('%a')

#     canvas.itemconfig(hr_text, text=hr)
#     canvas.itemconfig(min_text, text=mi)
#     canvas.itemconfig(sec_text, text=sec)
#     canvas.itemconfig(am_text, text=am)

#     canvas.itemconfig(date_text, text=date)
#     canvas.itemconfig(month_text, text=month)
#     canvas.itemconfig(year_text, text=year)
#     canvas.itemconfig(day_text, text=day)

#     clock.after(1000, update_time)

# clock = Tk()
# clock.title("**** Transparent Digital Clock ****")
# clock.geometry("1000x500")

# # Load background image
# bg_image = Image.open("background.jpg")  # make sure path is correct
# bg_image = bg_image.resize((1000, 500), Image.Resampling.LANCZOS)
# bg_photo = ImageTk.PhotoImage(bg_image)

# canvas = Canvas(clock, width=1000, height=500)
# canvas.pack(fill="both", expand=True)
# canvas.create_image(0, 0, image=bg_photo, anchor=NW)

# # 🟡 Transparent Time Text
# hr_text = canvas.create_text(170, 100, text="00", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(170, 180, text="Hour", fill="yellow", font=("Times New Roman", 20, "bold"))

# min_text = canvas.create_text(390, 100, text="00", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(390, 180, text="Min", fill="yellow", font=("Times New Roman", 20, "bold"))

# sec_text = canvas.create_text(610, 100, text="00", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(610, 180, text="Sec", fill="yellow", font=("Times New Roman", 20, "bold"))

# am_text = canvas.create_text(830, 100, text="AM", fill="yellow", font=("Times New Roman", 50, "bold"))
# canvas.create_text(830, 180, text="AM/PM", fill="yellow", font=("Times New Roman", 20, "bold"))

# # 🔴 Transparent Date Text
# date_text = canvas.create_text(170, 300, text="00", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(170, 380, text="Date", fill="yellow", font=("Times New Roman", 20, "bold"))

# month_text = canvas.create_text(390, 300, text="00", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(390, 380, text="Month", fill="yellow", font=("Times New Roman", 20, "bold"))

# year_text = canvas.create_text(610, 300, text="00", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(610, 380, text="Year", fill="yellow", font=("Times New Roman", 20, "bold"))

# day_text = canvas.create_text(830, 300, text="Mon", fill="yellow", font=("Times New Roman", 60, "bold"))
# canvas.create_text(830, 380, text="Day", fill="yellow", font=("Times New Roman", 20, "bold"))

# update_time()
# clock.mainloop()



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
