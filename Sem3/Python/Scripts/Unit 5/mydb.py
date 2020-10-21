import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root" , passwd = "2812" )
cursor=mydb.cursor()
# cursor.execute("create database datacamp")
cursor.execute("use datacamp")
# cursor.execute("create table users (id int(11) not null AUTO_INCREMENT PRIMARY KEY,name varchar(255),user_name varchar(255))")
# cursor.execute("desc users")
# print(cursor.fetchall())


# query="insert into users(name,user_name) VALUES (%s,%s)"
# values=("h","hh")
# cursor.execute(query,values)
query1="select * from users"
cursor.execute(query1)
records=cursor.fetchall()
for a in records:
	print(a)
# mydb.commit()