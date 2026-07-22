from skpy import Skype
import os.path

slogin = Skype("hiteshpuhorit@gmail.com","P@ssw0rd")
contact = slogin.contacts["live:.cid.2405d0ce58c715aa"]
contact.chat.sendMsg("welcome to Wscube Tech . ")
for i in contact:
    print(i)

group = slogin.chats.create(["live:.cid.2405d0ce58c715aa",])


with open("file_path","rb") as f:
    contact.chat.sendFile(f,"name.png",image=True)
    