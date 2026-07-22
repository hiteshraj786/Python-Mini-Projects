import tkinter as tk
from PIL import Image , ImageTk
import random 

window = tk.Tk()

window.geometry("1200x1000")
window.title("Dice Roll")


dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image = image1)
label2 = tk.Label(window, image = image2)

label1.image = image1 
label2.image = image2 

label1.place(x=  0 , y = 100, width=500,height=500 )
label2.place(x=  700 , y = 100, width=500,height=500)

def dice_roll():
    image1  = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1
    image2  = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2


button = tk.Button(window,text="ROLL",bg="green",fg="white",command=dice_roll,font=("Time 20 bold",30))
button.place(x=450 , y =700 , width = 300, height = 100  )

window.mainloop()


#  sample 

# def roll_dice():
#     a = random.randint(1,6) 
#     label = tk.Label(window , text = a ).pack()

# button = tk.Button(window ,text= "click" , command = roll_dice ) 
# button.pack()
