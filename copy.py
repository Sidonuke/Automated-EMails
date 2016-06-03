import mysql.connector #Helpful to connect to the DB

cnx = mysql.connector.connect(user='sidonukenet2', password='Sidonukeg5', host='mysql.sidonuke.net', database='sidonuke_net_2') #SQL Info
cursor = cnx.cursor(buffered=True)

cursor.execute ("INSERT INTO UnlocksDB SELECT * FROM Unlocks")
cnx.commit()

cursor.execute ("TRUNCATE TABLE Unlocks")
cursor.close()
cnx.close()
