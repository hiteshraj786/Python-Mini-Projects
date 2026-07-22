from plyer import notification
import time 

if __name__ == '__main__':
    while True:
        notification.notify(title="*** Take Rest ***",message="Rest is vital for better mental health, increased concentration"
        " and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism",app_icon ="C:/Python Course/Python_Project/Desktop Notifier/rest.ico",timeout=5)

        time.sleep(10)



# if this file run in background so write this command in command promet-->
#  pythonw main.py