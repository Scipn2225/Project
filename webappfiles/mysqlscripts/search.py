import mysql.connector
import dbconnect
cur, con = dbconnect.get_connection() 
sql = "SELECT * FROM tblbook WHERE title = 'The Book Thief'"
cur.execute(sql)
myresult = cur.fetchall()
for x in myresult:
    print(x)