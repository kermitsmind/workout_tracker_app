#### importing libraries
import database_operations


#### get root and superUser password from file
passwordFile = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
rootPassword = passwordFile.readline()[:-1]
superUserPassword = "super_user_password"
adminUserPassword = "admin_user_password"


def main():

    # #### open connenction as super user
    connection = database_operations.openConnectionToDB(
        host="localhost",
        user="super_user",
        password=superUserPassword,
        database="WorkoutTrackerDB",
    )

    # mycursor = connection.cursor()

    # mycursor.execute("select * from personal_information")
    # for x in mycursor:
    #     print(x)

    # ### add sample user
    # database_operations.createUser(firstName="Adam", lastName="Smith", birthDate="1998-03-12", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_1_password", rootPassword=rootPassword)
    # database_operations.createUser(firstName="John", lastName="Wynn", birthDate="1997-09-11", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_2_password", rootPassword=rootPassword)

    # database_operations.closeConnectionToDB(connection=connection)

    ### open connenction as user
    connection = database_operations.openConnectionToDB(
        host="localhost",
        user="user_1",
        password="user_1_password",
        database="WorkoutTrackerDB",
    )

    mycursor = connection.cursor()

    # mycursor.execute("select * from personal_information")
    # for x in mycursor:
    #     print(x)

    #### add sample record to running
    database_operations.addRecordToRunningTable(
        connection=connection,
        cursor=mycursor,
        person_id=1,
        date="2022-01-19",
        type="interval",
        total_time=1278,
        total_distance=9786,
        terrain="indoor",
    )

    database_operations.closeConnectionToDB(connection=connection)


if __name__ == "__main__":
    main()
