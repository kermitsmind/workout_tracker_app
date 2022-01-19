#### importing libraries
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import os


#### open connection with given credentials and return the connection object
def openConnectionToDB(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
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


def createDatabase(host, user, password):
    #### connect to the database
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    #### create cursor for further usage
    mycursor = connection.cursor()

    #### create database
    mycursor.execute("CREATE DATABASE WorkoutTrackerDB")


def createDatabaseTables(host, user, password, database):
    #### connect to the database
    connection = openConnectionToDB(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    #### create cursor for further usage
    mycursor = connection.cursor()

    #### select DB
    mycursor.execute("use WorkoutTrackerDB")

    ### create tables
    table_1 = """CREATE TABLE personal_information (
        person_id int auto_increment primary key,
        first_name varchar(90),
        last_name varchar(90),
        birth_date date,
        phone_number int default null,
        nationality varchar(90),
        registration_date date
    )"""
    mycursor.execute(table_1)

    table_2 = """CREATE TABLE diet (
        diet_id int auto_increment primary key,
        person_id int,
        name varchar(90),
        start_date date,
        stop_date date,
        calories int default null,
        foreign key (person_id) references personal_information(person_id)
    )"""
    table_2_cst = "ALTER TABLE diet MODIFY person_id int NOT NULL"
    mycursor.execute(table_2)
    mycursor.execute(table_2_cst)

    table_3 = """CREATE TABLE running (
        running_id int auto_increment primary key,
        person_id int,
        date date,
        type varchar(90),
        total_time int default null,
        total_distance int default null,
        terrain varchar(90),
        foreign key (person_id) references personal_information(person_id)
    )"""
    table_3_cst = "ALTER TABLE running MODIFY person_id int NOT NULL"
    mycursor.execute(table_3)
    mycursor.execute(table_3_cst)

    table_4 = """CREATE TABLE swimming (
        swimming_id int auto_increment primary key,
        person_id int,
        date date,
        type varchar(90),
        total_time int default null,
        total_distance int default null,
        water varchar(90),
        foreign key (person_id) references personal_information(person_id)
    )"""
    table_4_cst = "ALTER TABLE swimming MODIFY person_id int NOT NULL"
    mycursor.execute(table_4)
    mycursor.execute(table_4_cst)

    table_5 = """CREATE TABLE weight_lifting (
        weight_lifting_id int auto_increment primary key,
        person_id int,
        date date,
        type varchar(90),
        no_series int default null,
        repeats_per_series int default null,
        weight int default null,
        foreign key (person_id) references personal_information(person_id)
    )"""
    table_5_cst = "ALTER TABLE weight_lifting MODIFY person_id int NOT NULL"
    mycursor.execute(table_5)
    mycursor.execute(table_5_cst)

    table_6 = """CREATE TABLE rest (
        rest_id int auto_increment primary key,
        person_id int,
        date date,
        night_sleep_hours int default null,
        relax_hours int default null,
        foreign key (person_id) references personal_information(person_id)
    )"""
    table_6_cst = "ALTER TABLE rest MODIFY person_id int NOT NULL"
    mycursor.execute(table_6)
    mycursor.execute(table_6_cst)


def createDatabaseBackup(backupName):
    command = (
        "/usr/local/mysql-8.0.27-macos11-arm64/bin/mysqldump --user=super_user -p WorkoutTrackerDB > "
        + str(backupName)
    )
    print(command)
    os.system(command)


def restoreDatabaseBackup(backupName):
    command = (
        "/usr/local/mysql-8.0.27-macos11-arm64/bin/mysql --host=localhost --user=super_user --port=3306 -p WorkoutTrackerDB < "
        + str(backupName)
    )
    os.system(command)


def createSuperUser(password, user="root"):
    connection = openConnectionToDB(
        host="localhost",
        user=user,
        password=password,
        database="WorkoutTrackerDB",
    )
    mycursor = connection.cursor()
    super_user = """
    create user 'super_user'@'localhost' identified by 'super_user_password';
    revoke all privileges, grant option from 'super_user'@'localhost';
    grant all privileges on WorkoutTrackerDB.* to 'super_user'@'localhost'; -- remember about .* after db name
    -- grant process on WorkoutTrackerDB.* to super_user@localhost; -- do in mysql from terminal logged with sudo
    """
    mycursor.execute(super_user)


def createAdminUser(password, user="root"):
    connection = openConnectionToDB(
        host="localhost",
        user=user,
        password=password,
        database="WorkoutTrackerDB",
    )
    mycursor = connection.cursor()
    admin_user = """
    create user 'admin_user'@'localhost' identified by 'admin_user_password';
    revoke all privileges, grant option from 'admin_user'@'localhost';
    grant select on WorkoutTrackerDB.* to 'admin_user'@'localhost';
    grant alter on WorkoutTrackerDB.* to 'admin_user'@'localhost';
    """
    mycursor.execute(admin_user)
