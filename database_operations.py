#### importing libraries
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import os
import sys
import subprocess


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
        return "ERROR"
    else:
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
    mycursor = connection.cursor(prepared=True)

    #### create database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS WorkoutTrackerDB")


def createDatabaseTables(host, user, password, database):
    #### connect to the database
    connection = openConnectionToDB(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    #### create cursor for further usage
    mycursor = connection.cursor(prepared=True)

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


def createDatabaseBackup(mysqldumpPassword, backupName="workout_tracker_backup"):
    command = (
        "/usr/local/mysql-8.0.27-macos11-arm64/bin/mysqldump --user=super_user -p"
        + mysqldumpPassword
        + " WorkoutTrackerDB > "
        + str(backupName)
        + ".sql"
    )
    print(command)
    os.system(command)


def restoreDatabaseBackup(mysqldumpPassword, backupName):
    command = (
        "/usr/local/mysql-8.0.27-macos11-arm64/bin/mysql --host=localhost --user=super_user --port=3306 -p"
        + mysqldumpPassword
        + " WorkoutTrackerDB < "
        + str(backupName)
        + ".sql"
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


def createUser(
    firstName,
    lastName,
    birthDate,
    phoneNumber,
    nationality,
    registrationDate,
    userPassword,
    rootPassword,
    user="root",
):
    connection = openConnectionToDB(
        host="localhost",
        user=user,
        password=rootPassword,
        database="WorkoutTrackerDB",
    )

    if connection == "ERROR":
        return "ERROR"

    mycursor = connection.cursor()

    addUserToTable = "insert into personal_information (first_name, last_name, birth_date, phone_number, nationality, registration_date) values ("
    addUserToTable += '"' + firstName + '", '
    addUserToTable += '"' + lastName + '", '
    addUserToTable += '"' + birthDate + '", '
    addUserToTable += str(phoneNumber) + ", "
    addUserToTable += '"' + nationality + '", '
    addUserToTable += '"' + registrationDate + '");'

    mycursor.execute(addUserToTable)
    connection.commit()

    getUserId = "select person_id from personal_information pi where "
    getUserId += 'pi.first_name="' + firstName + '" and '
    getUserId += 'pi.last_name="' + lastName + '" and '
    getUserId += 'pi.birth_date="' + birthDate + '" and '
    getUserId += "pi.phone_number=" + str(phoneNumber) + " and "
    getUserId += 'pi.nationality="' + nationality + '" and '
    getUserId += 'pi.registration_date="' + registrationDate + '";'

    userId = 0
    mycursor.execute(getUserId)
    for x in mycursor:
        userId = x[0]

    user_1 = (
        "create user 'user_"
        + str(userId)
        + "'@'localhost' identified by '"
        + userPassword
        + "';"
    )
    user_2 = (
        "revoke all privileges, grant option from 'user_"
        + str(userId)
        + "'@'localhost';"
    )
    user_3 = (
        "grant all privileges on WorkoutTrackerDB.* to 'user_"
        + str(userId)
        + "'@'localhost';"
    )
    user_4 = (
        "grant alter on WorkoutTrackerDB.* to 'user_" + str(userId) + "'@'localhost';"
    )

    mycursor.execute(user_1)
    mycursor.execute(user_2)
    mycursor.execute(user_3)
    mycursor.execute(user_4)

    userName = "user_" + str(userId)

    return userName


def addRecordToRunningTable(
    connection, cursor, person_id, date, type, total_time, total_distance, terrain
):
    sqlQueryForm = "insert into running (person_id, date, type, total_time, total_distance, terrain) values (%s, %s, %s, %s, %s, %s)"
    sqlQueryData = (
        str(person_id),
        date,
        type,
        str(total_time),
        str(total_distance),
        terrain,
    )

    try:
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()


def addRecordToDietTable(
    connection, cursor, person_id, name, start_date, stop_date, calories
):
    sqlQueryForm = "insert into diet (person_id, name, start_date, stop_date, calories) values (%s, %s, %s, %s, %s)"
    sqlQueryData = (str(person_id), name, start_date, stop_date, str(calories))

    try:
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()


def addRecordToSwimmingTable(
    connection, cursor, person_id, date, type, total_time, total_distance, water
):
    sqlQueryForm = "insert into swimming (person_id, date, type, total_time, total_distance, water) values (%s, %s, %s, %s, %s, %s)"
    sqlQueryData = (
        str(person_id),
        date,
        type,
        str(total_time),
        str(total_distance),
        water,
    )

    try:
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()


def addRecordToWeightLiftingTable(
    connection, cursor, person_id, date, type, no_series, repeats_per_series, weight
):
    sqlQueryForm = "insert into weight_lifting (person_id, date, type, no_series, repeats_per_series, weight) values (%s, %s, %s, %s, %s, %s)"
    sqlQueryData = (
        str(person_id),
        date,
        type,
        str(no_series),
        str(repeats_per_series),
        str(weight),
    )

    try:
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()


def addRecordToRestTable(
    connection, cursor, person_id, date, night_sleep_hours, relax_hours
):
    sqlQueryForm = "insert into rest (person_id, date, night_sleep_hours, relax_hours) values (%s, %s, %s, %s)"
    sqlQueryData = (str(person_id), date, str(night_sleep_hours), str(relax_hours))

    try:
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()


def showRecordsFromTableMatchingQuery(cursor, person_id, table, column, criterion):
    if column == "" and criterion == "":
        try:
            sqlQueryForm = "select * from " + table + " where person_id = %s;"
            sqlQueryData = str(person_id)
            cursor.execute(sqlQueryForm, sqlQueryData)
            records = []
            for x in cursor:
                records.append(x)
                print(x)
            return records
        except:
            print("An error while querying occured")
            pass
            return []
    else:
        try:
            sqlQueryForm = (
                "select * from "
                + table
                + " where person_id = %s and "
                + column
                + " = %s;"
            )
            sqlQueryData = (str(person_id), criterion)
            cursor.execute(sqlQueryForm, sqlQueryData)
            records = []
            for x in cursor:
                records.append(x)
                print(x)
            return records
        except:
            print("An error while querying occured")
            pass
            return []


def deleteRecordFromAnyTable(connection, cursor, person_id, table, recordId):
    sqlQueryForm = (
        "delete from " + table + " where person_id = %s and " + table + "_id = %s;"
    )
    sqlQueryData = (person_id, recordId)

    try:
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()


def modifyRecordFromAnyTable(
    connection, cursor, person_id, table, recordId, column, value
):
    sqlQueryForm = (
        "update "
        + table
        + " set `"
        + column
        + '` = "'
        + value
        + '" where person_id = %s and '
        + table
        + "_id = %s;"
    )
    sqlQueryData = (person_id, recordId)

    try:
        print(sqlQueryForm)
        connection.autocommit = False
        cursor.execute(sqlQueryForm, sqlQueryData)
        connection.commit()
    except:
        connection.rollback()
        print("ERROR: ", sys.exc_info()[0])
