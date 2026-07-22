import smtplib as s 
 
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()

ob.login('hiteshpuhorit@gmail.com','zbhapvtlfiqgauxy')
subject = "test java"
body =  "I love java"
messege = "subject:{}\n\n{}".format(subject,body)
listadd = ['bharatpurohit274@gmail.com',]
ob.sendmail('hiteshpuhorit@gmail.com',listadd,messege)
print("send mail")
ob.quit()
