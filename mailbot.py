# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:28:54 2022

@author: SATHYA
"""

import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('your gmail id','gmail App password')
SUBJECT=input("subject for the mail: ")
TEXT=open("content.txt","r+")
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT.read())
print("Typing and sending the mail !!")
server.sendmail('from mail','to mail',message)
TEXT.close()
print("Mail sent successfully :)")