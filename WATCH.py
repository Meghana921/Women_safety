import time
import os
import numpy
import numpy as np
import sys
import cv2
import os
from PIL import Image
##import atttachem
import telepot
##from twilio.rest import Client
##account_sid = "AC3ea11538ed6d9edcf289d818731ee80d"
##auth_token = "db75bdb5a21fd3df079eafda1131392a"
##
##client = Client(account_sid, auth_token)
from tkinter import *
import tkinter as tk
Window=tk.Tk()
Window.title("New Window")
Window.geometry("500x500")
Window.configure(background="grey")
lbl=tk.Label(Window,text="WOMEN SAFETY SYSTEM",width=40,height=3,fg="red",bg="black",font=("times",15,"bold"))
lbl.place(x=100,y=100)
cap = cv2.VideoCapture(0)

  
def Next():
       sample=0;
       error=0
       while(cap.isOpened()):
       #while(True):
          
           ret, img = cap.read()
           if ret:
               error=1
               gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
               cv2.imshow('frame',img)
               cv2.imwrite('frame.png',img)
               cv2.waitKey(1)
               sample=sample+1
           if (sample == 50):
                sample =0;
                break

       cap.release()
       if error ==0:
          print('Camera is interrupted\nPlease execute the script again')
          cv2.destroyAllWindows()
       if error ==1:
         print('image is caputured')

##       client.api.account.messages.create(
##          to="+91-8549990955",
##          from_="+19096393455" ,  #+1 210-762-4855"
##          body='Emergency at http://www.google.com/maps/?q={},{}'.format('13.0379','77.6190'))

       bot = telepot.Bot('5686805071:AAFYQBcP9csEGLtdCN-rlCVjb3H3fPi52rM')
       bot.sendMessage('1214514766', str('Emergency at http://www.google.com/maps/?q={},{}'.format('13.0379','77.6190')))
       bot.sendPhoto('1214514766', photo=open('frame.png', 'rb'))
##       atttachem.sendMail( ["mngowda1096@gmail.com"],
##               "PERSON VICTIM IMAGE",
##               "this is the body text of the email",
##               ["frame.png"] )

##       print('email send........')

      ###########################################
      ##print(text)
       cv2.destroyAllWindows()
       print('Completed')
            
button=tk.Button(Window,text="EMERGENCY BUTTON",command=Next,activebackground="Black",fg="white",bg="Red",width=20,height=2,font=("times",15,"bold"))
button.place(x=200,y=400)
Window.mainloop()
