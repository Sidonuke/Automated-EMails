from smtplib import SMTP #Email orders
import mysql.connector #Helpful to connect to the DB
import datetime #Current date for email

sequel = mysql.connector.connect(user='USERNAME', password='PASSWORD', host='SQLADDRESS', database='DATABASENAME') #SQL Info
cursor = sequel.cursor()
query = ('SELECT Time, Name, Flight, Reason, Done FROM Unlocks ') #Only the needed SQL Fields
cursor.execute(query)

date = datetime.datetime.now() #Date in SUBJECT line below.

body = list() #Our body for email
for (Time, Name, Flight, Reason, Done) in cursor:
    body.append('At {}, {} called to unlock {}, due to {} This was completed at {}.'.format(
    Time, Name, Flight, Reason, Done)) #Add each list item depending on values in SQL DB
if not body:
    body.append('No unlocks were needed for ' + date.strftime('%m, %d, %Y')) #If no data in the tables above then inserts this as the email body.

body = '\n'.join(body) #New line for each row in the table Unlocks
body = (str(body).replace('[','').replace(']','')) #Pesky brackets would not go away!

smtp = SMTP()
smtp.connect('EMAILSERVER', SMTPPORT) #Our Email Server
smtp.login('USERNAME', 'EMAILPASS') #Email Credentials.
FROM = 'YOU@EMAIL.com'
TO = ['USER@EMAIL.COM', 'USER1@EMAIL.COM', 'USER2@EMAIL.COM'] # must be a list (seperated by a comma)
SUBJECT = 'Flight unlocks for' + ' ' + date.strftime('%m, %d, %Y')
TEXT = ('Good Evening All,'+'\n'+'\n' + body)#Formatting and indenting
message = '''\
From: %s
To: %s
Subject: %s
%s
''' % (FROM, ', '.join(TO), SUBJECT, TEXT)
smtp.sendmail(FROM, TO, message)

smtp.quit()
cursor.close()
sequel.close()
