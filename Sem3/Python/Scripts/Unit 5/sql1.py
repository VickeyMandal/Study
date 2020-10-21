import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )

if conn:
	print("succ")
else:
	print("fail")