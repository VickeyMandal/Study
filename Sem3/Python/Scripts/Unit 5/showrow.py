	try:
		connection=mysql.connector.connect(host="localhost",database="iplb",user="root",password="2812")
		s="select * from cricketers"
		cursor.connection.cursor()
		cursor.execyte(s)
		records=cursor.fetchall()
		print("Total rows in table: ",cursor.rowcount)
		print("each info")
		for row in records:
			print("id = ",row[0])
			print("names = ",row[1])
			
