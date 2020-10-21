import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
mycursor=mydb.cursor()
mycursor.execute("create database iplb")

mycursor.execute("use iplb")
mycursor.execute("create table cricketers ()")

mysqlstuff=("insert into cricketers (team,,name,matches,run) VALUES ('RCB','Virat Kohli',13,567)")
mycursor.execute(mysqlstuff)
mydb.commit()
# print(mycursor.rowcount, "rows inserted")
# record2=('csk','suresh raina',23,667)
# mycursor.execute(sqlstuff,record2)
# mydb.commit()
# print(mycursor.rowcount, "rows inserted")
# sql="insert into cricketres(team,name,matches,run)VALUES (%s,%s,%s,%s)"
# val=[('mi','Rohit sharma',45,7548),
# 	('csk','M S dhoni',566,7654)]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount, "rows inserted")
