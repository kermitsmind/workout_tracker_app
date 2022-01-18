#### importing libraries
from __future__ import print_function
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

    mycursor.execute("use WorkoutTrackerDB")

    #### create database
    # mycursor.execute("CREATE DATABASE WorkoutTrackerDB")
    
    #### create tables
    # table_1 = '''CREATE TABLE personal_information (
    #     person_id int auto_increment primary key,
    #     first_name varchar(90),
    #     last_name varchar(90),
    #     birth_date date,
    #     phone_number int default null,
    #     nationality varchar(90),
    #     registration_date date
    # )'''
    # mycursor.execute(table_1)

    # table_2 = '''CREATE TABLE diet (
    #     diet_id int auto_increment primary key,
    #     person_id int,
    #     name varchar(90),
    #     start_date date,
    #     stop_date date,
    #     calories int default null,
    #     foreign key (person_id) references personal_information(person_id)
    # )'''
    # table_2_cst = "ALTER TABLE diet MODIFY person_id int NOT NULL"
    # mycursor.execute(table_2)
    # mycursor.execute(table_2_cst)

    # table_3 = '''CREATE TABLE running (
    #     running_id int auto_increment primary key,
    #     person_id int,
    #     date date,
    #     type varchar(90),
    #     total_time int default null,
    #     total_distance int default null,
    #     terrain varchar(90),
    #     foreign key (person_id) references personal_information(person_id)
    # )'''
    # table_3_cst = "ALTER TABLE running MODIFY person_id int NOT NULL"
    # mycursor.execute(table_3)
    # mycursor.execute(table_3_cst)
    
    # table_4= '''CREATE TABLE swimming (
    #     swimming_id int auto_increment primary key,
    #     person_id int,
    #     date date,
    #     type varchar(90),
    #     total_time int default null,
    #     total_distance int default null,
    #     water varchar(90),
    #     foreign key (person_id) references personal_information(person_id)
    # )'''
    # table_4_cst = "ALTER TABLE swimming MODIFY person_id int NOT NULL"
    # mycursor.execute(table_4)
    # mycursor.execute(table_4_cst)

    # table_5= '''CREATE TABLE weight_lifting (
    #     weight_lifting_id int auto_increment primary key,
    #     person_id int,
    #     date date,
    #     type varchar(90),
    #     no_series int default null,
    #     repeats_per_series int default null,
    #     weight int default null,
    #     foreign key (person_id) references personal_information(person_id)
    # )'''
    # table_5_cst = "ALTER TABLE weight_lifting MODIFY person_id int NOT NULL"
    # mycursor.execute(table_5)
    # mycursor.execute(table_5_cst)

    # table_6= '''CREATE TABLE rest (
    #     rest_id int auto_increment primary key,
    #     person_id int,
    #     date date,
    #     night_sleep_hours int default null,
    #     relax_hours int default null,
    #     foreign key (person_id) references personal_information(person_id)
    # )'''
    # table_6_cst = "ALTER TABLE rest MODIFY person_id int NOT NULL"
    # mycursor.execute(table_6)
    # mycursor.execute(table_6_cst)




if __name__ == "__main__":
    main()

#### references
# https://dev.mysql.com/doc/