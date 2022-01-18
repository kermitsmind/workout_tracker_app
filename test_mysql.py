import mysql.connector as mysql
import getpass
 
try:
    password = getpass.getpass()
except Exception as error:
    print('ERROR', error)

mydb = mysql.connect(
    host="localhost",
    user="root",
    password=password
)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE myTESTdatabasePYTHON")