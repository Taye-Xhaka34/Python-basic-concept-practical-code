import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Tanga2008@",
    database="python"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Student")
results = mycursor.fetchone()
for i in mycursor:
    print(i)
