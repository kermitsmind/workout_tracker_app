#### importing libraries
import mysql.connector
from mysql.connector import errorcode
import getpass


#### get root password from file
passwordFile = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
rootPassword = passwordFile.readline()[:-1]

#### get password from terminal prompt
def getPassword():
    try:
        rootPassword = getpass.getpass()
    except Exception as error:
        print("ERROR", error)
    return rootPassword


#### open connection with given credentials and return the connection object
def openConnectionToDB(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password=rootPassword
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return connection


#### close given connection
def closeConnectionToDB(connection):
    try:
        connection.close()
    except:
        print("Encountered error while closing the connection")


def main():
    ####
    connection = openConnectionToDB(
        host="localhost",
        user="root",
        password=rootPassword,
        database="WorkoutTrackerDB",
    )
    #### create cursor for further usage
    mycursor = connection.cursor()

    # #### create database
    # mycursor.execute("CREATE DATABASE WorkoutTrackerDB")
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)


if __name__ == "__main__":
    main()
