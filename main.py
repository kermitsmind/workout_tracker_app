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

    #### open connenction as super user
    # connection = database_operations.openConnectionToDB(
    #     host="localhost",
    #     user="super_user",
    #     password=superUserPassword,
    #     database="WorkoutTrackerDB",
    # )

    # mycursor = connection.cursor()

    # mycursor.execute("select * from personal_information")
    # for x in mycursor:
    #     print(x)

    #### add sample user
    # database_operations.createUser(firstName="Adam", lastName="Smith", birthDate="1998-03-12", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_1_password", rootPassword=rootPassword)

    #### open connenction as user
    connection = database_operations.openConnectionToDB(
        host="localhost",
        user="user_1",
        password="user_1_password",
        database="WorkoutTrackerDB",
    )

    mycursor = connection.cursor()

    mycursor.execute("select * from personal_information")
    for x in mycursor:
        print(x)


if __name__ == "__main__":
    main()
