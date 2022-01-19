#### importing libraries
import database_operations


#### get root password from file
passwordFile = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
rootPassword = passwordFile.readline()[:-1]
superUserPassword="super_user_password"


def main():
    #### create database
    # database_operations.createDatabase(host="localhost", user="super_user", password=superUserPassword)
    # database_operations.restoreDatabaseBackup(backupName="db_backup.sql")

    ## populate database with appropriate tables
    # database_operations.createDatabaseTables(
    #     host="localhost",
    #     user="super_user",
    #     database="WorkoutTrackerDB",
    #     password=superUserPassword
    # )

    #### set access levels in the database
    # connection = database_operations.openConnectionToDB(    
    #     host="localhost",
    #     user="super_user",
    #     password=superUserPassword,
    #     database="WorkoutTrackerDB",
    # )

    # mycursor = connection.cursor()
    # admin_user = '''
    # create user 'super_user'@'localhost' identified by 'super_user_password';
    # revoke all privileges, grant option from 'super_user'@'localhost';
    # grant all privileges on WorkoutTrackerDB.* to 'super_user'@'localhost'; -- remember about .* after db name
    # grant process on WorkoutTrackerDB.* to super_user@localhost;
    # '''
    # mycursor.execute("drop database WorkoutTrackerDB")

    # mycursor.execute("show grants for 'super_user'@'localhost'")
    # for x in mycursor:
    #     print(x)

    # database_operations.createDatabaseBackup(backupName="db_backup.sql")

if __name__ == "__main__":
    main()
