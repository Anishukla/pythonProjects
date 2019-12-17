"""
@author: anishukla
"""
#Using this code we can write a common mail for multiple users using gmail.

import smtplib

host = "smtp.gmail.com"
port = 587
print("Enter your Mail id")
username = input()

print("Enter your Password")
password = input()
from_email = username
to_list = []
print("Enter the number of people you want to send your mail: ")
num = int(input())

for i in range(num):
    if i==0:
        print("Enter 1st Email Id")
    else:
        print("Enter {} more E-mail address".format(num-i))
    to_mail = input()
    to_list.append(to_mail)

email_con = smtplib.SMTP(host, port)

email_con.ehlo()
email_con.starttls()
email_con.login(username, password)
print("Write your common message for above email holders.")
msg = input()
email_con.sendmail(from_email, to_list, msg)

 
#Execute last line after completion
#email_con.quit()
