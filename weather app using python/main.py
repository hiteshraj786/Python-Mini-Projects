from tkinter import*
from tkinter import ttk
import requests



def data_get():
    city=city_name.get()
    api_key = "8e2691b45bbe40b74564dd92e1f71eaa"

  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    response = requests.get(url)
    data = response.json() 

    W_label1.config(text=data["weather"][0]["main"])


    WD_label1.config(text=data["weather"][0]["description"])

    temp_label1.config(text=str(data["main"]["temp"]) + " °C")

    
    per_label1.config(text=str(data["main"]["pressure"])+" mb")





win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x560")

name_label = Label(win,text="Accurate Weather App",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)




list_name = [ "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra","Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal", "Mumbai","Delhi","Bangalore","Chennai", "Kolkata", "Hyderabad", "Ahmedabad", "Pune", "Surat", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane","Bhopal","Visakhapatnam","Pimpri-Chinchwad","Patna","Vadodara"
]


city_name = StringVar()
com = ttk.Combobox(win,text="Accurate Weather App",font=("Time New Roman",20,"bold"),values=list_name,textvariable=city_name)
com.place(x=50,y=120,height=50,width=400)





W_label = Label(win,text="Weather Climate",font=("Time New Roman",20))
W_label.place(x=25,y=250,height=50,width=210)

W_label1 = Label(win,text="",font=("Time New Roman",20))
W_label1.place(x=250,y=250,height=50,width=210)



WD_label = Label(win,text="Weather Description",font=("Time New Roman",17))
WD_label.place(x=25,y=320,height=50,width=210)

WD_label1 = Label(win,text="",font=("Time New Roman",17))
WD_label1.place(x=250,y=320,height=50,width=210)



temp_label = Label(win,text="Temperature",font=("Time New Roman",20))
temp_label.place(x=25,y=390,height=50,width=210)

temp_label1 = Label(win,text="",font=("Time New Roman",20))
temp_label1.place(x=250,y=390,height=50,width=210)



per_label = Label(win,text="Pressure",font=("Time New Roman",20))
per_label.place(x=25,y=460,height=50,width=210)

per_label1 = Label(win,text="",font=("Time New Roman",20))
per_label1.place(x=250,y=460,height=50,width=210)






done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=data_get)
done_button.place(x=200,y=190,height=40,width=100)


win.mainloop()