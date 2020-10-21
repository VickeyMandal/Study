import mysql.connector
from mysql.connector import Error
try:
	connection=mysql.connector.connect(host="localhost",database="iplb",user="root",password="2812")
	if connection.is_connected():
		db_info=connection.get_server_info()
		print("Connected to mysql server version: ",db_info)
		cursor=connection.cursor()
		cursor.execute("select database()")
		record=cursor.fetchone()
		print("you are connected to database",record)
except Error as e:
	print("error while connecting to mysql",e)
finally:
	if(connection.is_connected()):
		cursor.close()
		connection.close()
		print("mysql connection is closed")

def insertintotable(id, name,price,purchase_date):
	try:
		connection=mysql.connector.connect(host="localhost",database="iplb",user="root",password="2812")
		cursor=connection.cursor()
		query="insert int tablename (id, name,price,purchase_date) values (%s,%S,%s,%s)"
		r=(id,name,price,purchase,purchase_date)
		cursor.execute(q,r)
		connection.commit()
	except mysql.connector.Error as error:
		print("failed to insert")
	finally:
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			print("connection is closed")


insertintotable(2,"msi,556,'2020-06-12'")


