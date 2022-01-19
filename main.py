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

    #### open coccenction
    connection = database_operations.openConnectionToDB(
        host="localhost",
        user="super_user",
        password=superUserPassword,
        database="WorkoutTrackerDB",
    )

    # database_operations.createAdminUser(password=rootPassword)

    mycursor = connection.cursor()

    mycursor.execute("show grants for 'super_user'@'localhost'")
    for x in mycursor:
        print(x)


if __name__ == "__main__":
    main()
