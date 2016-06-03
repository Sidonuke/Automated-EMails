#!/usr/bin/python
from smtplib import SMTP #Email orders
import mysql.connector #Helpful to connect to the DB
import datetime #Current date for email
import json #Used below simply for indenting ;)

cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD', host='HOSTNAME', database='DATABASE') #SQL Info
cursor = cnx.cursor()

query = ("SELECT Time, Name, Flight, Reason, Done FROM Unlocks ") #Only the needed SQL Fields

cursor.execute(query)

squares = list() #Don't ask why it's named squares.
for (Time, Name, Flight, Reason, Done) in cursor:
    squares.append("At {}, {} called to unlock {} due to {}, This was completed at {}".format(
    Time, Name, Flight, Reason, Done)) #Add each list item depending on values in SQL DB

date = datetime.datetime.now() #Date in SUBJECT line below.

smtp = SMTP()
smtp.connect('HOSTNAME', SMTPPORT) #Our Email Server
smtp.login('USER@EMAIL.COM', 'PASSWORD') #Email Credentials. 

FROM = 'WHO IS SENDING THE EMAIL (USER@EMAIL.COM)'

TO = ["RECEIVER (BOSS@EMAIL.COM)"] # must be a list

SUBJECT = "Flight unlocks for" + " " + date.strftime("%m, %d, %Y")

TEXT = ('Good Evening All,'+'\n'+'\n' + json.dumps(squares, indent = 0)) #Formatting and indenting

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

smtp.sendmail(FROM, TO, message)
smtp.quit()
cursor.close()
cnx.close()
