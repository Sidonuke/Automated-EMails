import mysql.connector #Helpful to connect to the DB

cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD', host='SQL SERVER', database='DATABASE') #SQL Info
cursor = cnx.cursor(buffered=True)

cursor.execute ("INSERT INTO UnlocksDB SELECT * FROM Unlocks")
cnx.commit()

cursor.execute ("TRUNCATE TABLE Unlocks")
cursor.close()
cnx.close()
