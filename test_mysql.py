#### importing libraries
from matplotlib.pyplot import table
import database_operations
import gui
import PySimpleGUI as sg
import time

connection = database_operations.openConnectionToDB(
                    host="localhost",
                    user="user_1",
                    password="user_1_password",
                    database="WorkoutTrackerDB"
                )

mycursor = connection.cursor(prepared=True)
database_operations.showRecordsFromTableMatchingQuery(cursor=mycursor, person_id=1, table="running", 
column="terrain", criterion="indoor")

database_operations.modifyRecordFromAnyTable(connection=connection, cursor=mycursor, person_id=1, table="running", 
recordId=3, column="type", value="interval")

# mycursor.execute("update running set `type` = \"sprint\" where person_id = 1 and running_id = 3;")
print("------")

database_operations.showRecordsFromTableMatchingQuery(cursor=mycursor, person_id=1, table="running", 
column="terrain", criterion="indoor")