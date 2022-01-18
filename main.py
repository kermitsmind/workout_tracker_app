#### importing libraries
import mysql.connector as mysql
import getpass
 

#### get root password from file
passwordFile = open("/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword")
rootPassword = passwordFile.readline()[:-1]


#### get root password from terminal prompt
# try:
#     rootPassword = getpass.getpass()
# except Exception as error:
#     print('ERROR', error)


#### connect to database with given credentials
mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = rootPassword
)

#### create cursor for further usage
mycursor = mydb.cursor()

#### create database
mycursor.execute("CREATE DATABASE WorkoutTrackerDB")
mycursor.execute("SHOW DATABASES")