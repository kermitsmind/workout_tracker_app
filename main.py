#### importing libraries
import database_operations


#### get root password from file
passwordFile = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
rootPassword = passwordFile.readline()[:-1]


def main():
    #### create database
    # database_operations.createDatabase(host="localhost", user="root", password=rootPassword)

    #### populate database with appropriate tables
    database_operations.createDatabaseTables(
        host="localhost",
        user="root",
        password=rootPassword,
        database="WorkoutTrackerDB",
    )


if __name__ == "__main__":
    main()
