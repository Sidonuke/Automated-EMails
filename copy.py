import mysql.connector #Helpful to connect to the DB

cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD', host='HOSTNAME', database='DATABASE') #SQL Info
cursor = cnx.cursor(buffered=True) 

cursor.execute ("INSERT INTO UnlocksDB SELECT * FROM Unlocks") #Copies into the "storage" Database from the Daily Database
cnx.commit()

cursor.execute ("TRUNCATE TABLE Unlocks") # Empties the daily table so that we can begin a new day. (NOTE. The reason I didn't drop was because the field names are fine, just needed Data gone.
cursor.close()
cnx.close()
