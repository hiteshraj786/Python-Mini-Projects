from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown /1")













st  = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st,text="Restart",font=("Time New Roamn",25,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roamn",25,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)


s_button = Button(st,text="ShutDown",font=("Time New Roamn",25,"bold"),relief=RAISED,cursor="plus",command=shutdown)
s_button.place(x=150,y=280,height=50,width=200)



lg_button = Button(st,text="Log-Out",font=("Time New Roamn",25,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=390,height=50,width=200)




st.mainloop()