import mysql.contector 

dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'Rohith@1510'
)


cursorObject = database.cursor()

cursorbject.execute("CREATE DATABASE elderco")

print("All Done!")

