import mysql.connector
import dbconnect
cur, con = dbconnect.get_connection() 

sql = "DELETE FROM tbllanguage WHERE language_name = 'Spanish'"

cur.execute(sql)

con.commit()

print(cur.rowcount, "record(s) deleted")
