import mysql.connector



mydb = mysql.connector.connect(
	host="localhost",
	user="sha2user",
	passwd="Boot!camp2021!",
	)
	
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE adoption")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)