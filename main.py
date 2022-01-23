#### importing libraries
import database_operations
import gui
import PySimpleGUI as sg

#### get root and superUser password from file
passwordFile = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
rootPassword = passwordFile.readline()[:-1]
superUserPassword = "super_user_password"
adminUserPassword = "admin_user_password"


def main():

    # #### open connenction as super user
    # connection = database_operations.openConnectionToDB(
    #     host="localhost",
    #     user="super_user",
    #     password=superUserPassword,
    #     database="WorkoutTrackerDB",
    # )

    # mycursor = connection.cursor(prepared=True)

    # mycursor.execute("select * from personal_information")
    # for x in mycursor:
    #     print(x)

    # ### add sample user
    # database_operations.createUser(firstName="Adam", lastName="Smith", birthDate="1998-03-12", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_1_password", rootPassword=rootPassword)
    # database_operations.createUser(firstName="John", lastName="Wynn", birthDate="1997-09-11", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_2_password", rootPassword=rootPassword)

    # database_operations.closeConnectionToDB(connection=connection)

    ### open connenction as user
    # connection = database_operations.openConnectionToDB(
    #     host="localhost",
    #     user="user_1",
    #     password="user_1_password",
    #     database="WorkoutTrackerDB",
    # )

    # mycursor = connection.cursor(prepared=True)

    # mycursor.execute("select * from running where person_id = 1 and terrain = 'indoor';")
    # for x in mycursor:
    #     print(x)

    #### add sample record to running
    # database_operations.addRecordToRunningTable(
    #     connection=connection,
    #     cursor=mycursor,
    #     person_id=2,
    #     date="2021-12-14",
    #     type="interval",
    #     total_time=1789,
    #     total_distance=1786,
    #     terrain="outdoor",
    # )

    #### add sample record to diet
    # database_operations.addRecordToDietTable(
    #     connection=connection,
    #     cursor=mycursor,
    #     person_id=2,
    #     name="2000_calories",
    #     start_date="2021-12-13",
    #     stop_date="2022-11-14",
    #     calories=2000,
    # )

    # database_operations.showRecordsFromTableMatchingQuery(cursor=mycursor, person_id=1, table="running", column="terrain", criterion="indoor")
    
    # database_operations.closeConnectionToDB(connection=connection)
    # global username, password
    # gui.loginUserWindow()

    username = ''
    password = ''
    
    # login window + trying to connect to DB + if connection successful then retrieve lobin/password to variables
    sg.theme("LightBlue2")
    layout = [[sg.Text("Log In", size =(15, 1), font=40)],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-username-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-password-', password_char='*', font=16)],
            [sg.Button('Ok'),sg.Button('Cancel')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                connection = database_operations.openConnectionToDB(
                    host="localhost",
                    user=values['-username-'],
                    password=values['-password-'],
                    database="WorkoutTrackerDB",
                )
                if connection == "ERROR":
                    sg.popup("Invalid credentials. Try again")
                else:
                    username = values['-username-']
                    password = values['-password-']
                    # sg.popup("Welcome!")
                    gui.progress_bar()
                    gui.registerUserWindow()
                    break

    window.close()

if __name__ == "__main__":
    main()
