import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '19Erkinbek98',
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("All Done!")