#### importing libraries
from fileinput import hook_compressed
import database_operations
import gui
import PySimpleGUI as sg
import time

#### get root and superUser password from file
passwordFile_1 = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
passwordFile_2 = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectSuperuserPassword"
)
rootPassword = passwordFile_1.readline()[:-1]
superUserPassword = passwordFile_2.readline()[:-1]


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
    global username
    global password
    username = ""
    password = ""
    global connection
    isUserLogged = "USER_NOT_LOGGED"
    global emergency_login
    emergency_login = "NO"

    # login window + trying to connect to DB + if connection successful then retrieve lobin/password to variables
    window_login = sg.Window("Log In", gui.login_layout)

    #### log in
    while True:
        event_login, values_login = window_login.read()
        if event_login == "Cancel" or event_login == sg.WIN_CLOSED:
            break
        else:
            if event_login == "Login":
                connection = database_operations.openConnectionToDB(
                    host="localhost",
                    user=values_login["-username-"],
                    password=values_login["-password-"],
                    database="WorkoutTrackerDB",
                )
                if connection == "ERROR":
                    sg.popup("Error occured. Try again")
                else:
                    username = values_login["-username-"]
                    password = values_login["-password-"]
                    # sg.popup("Welcome!")
                    gui.progress_bar_login()
                    isUserLogged = "USER_LOGGED"
                    break
            if event_login == "Emergency login":
                emergency_login = "YES"
                username = values_login["-username-"]
                password = values_login["-password-"]
                if username == "super_user" and password == superUserPassword:
                    break
                else:
                    sg.popup("Error occured. Try again")

            if event_login == "Register":
                window_register = sg.Window("Sign Up", gui.register_layout)
                while True:
                    event_register, values_register = window_register.read()
                    if event_register == "Cancel" or event_register == sg.WIN_CLOSED:
                        break
                    else:
                        if event_register == "Submit":
                            first_name = values_register["-register_first_name-"]
                            last_name = values_register["-register_last_name-"]
                            birth_date = values_register["-register_birth_date-"]
                            phone_number = values_register["-register_phone_number-"]
                            nationality = values_register["-register_nationality-"]
                            registration_date = values_register[
                                "-register_registration_date-"
                            ]
                            user_password = values_register["-register_password-"]

                            userName = database_operations.createUser(
                                firstName=first_name,
                                lastName=last_name,
                                birthDate=birth_date,
                                phoneNumber=phone_number,
                                nationality=nationality,
                                registrationDate=registration_date,
                                userPassword=user_password,
                                rootPassword=rootPassword,
                            )

                            if userName == "ERROR":
                                sg.popup("Error occured. Try again")
                                break

                            message = "Your username: " + userName
                            sg.popup(message)
                            gui.progress_bar_register()
                            break
                window_register.close()
    window_login.close()

    #### user is logged
    global column
    global criterion
    if (
        isUserLogged == "USER_LOGGED"
        and username.find("admin") == -1
        and username.find("super") == -1
    ):
        column, criterion = "", ""
        mycursor = connection.cursor(prepared=True)

        window = sg.Window("User account", gui.user_layout)
        while True:
            event, values = window.read()
            if event in (None, "Exit") or event == sg.WIN_CLOSED:
                break
            elif event in (None, "About"):
                sg.popup("Help", "page", keep_on_top=True)
            else:
                if event == "Show running records":
                    records = database_operations.showRecordsFromTableMatchingQuery(
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        table="running",
                        column=values["-column_running_show-"],
                        criterion=values["-criterion_running_show-"],
                    )
                    # print = window.FindElement("_OP_1_").update
                    window.find_element("_OP_1_").update("")
                    for x in records:
                        window.find_element("_OP_1_").update(
                            ("{}\n".format(x)), append=True
                        )
                        print(x)
                        # time.sleep(1)
                    pass

                if event == "Add running record":
                    database_operations.addRecordToRunningTable(
                        connection=connection,
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        date=values["-column_running_add_date-"],
                        type=values["-column_running_add_type-"],
                        total_time=values["-column_running_add_time-"],
                        total_distance=values["-column_running_add_distance-"],
                        terrain=values["-column_running_add_terrain-"],
                    )

                if event == "Delete running record":
                    database_operations.deleteRecordFromAnyTable(
                        connection=connection,
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        table="running",
                        recordId=values["-column_running_delete_runningId-"],
                    )

                if event == "Modify running record":
                    database_operations.modifyRecordFromAnyTable(
                        connection=connection,
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        table="running",
                        column=values["-column_running_modify_column-"],
                        value=values["-column_running_modify_value-"],
                        recordId=values["-column_running_modify_runningId-"],
                    )
                    print(
                        "column: ",
                        values["-column_running_modify_column-"],
                        "value: ",
                        values["-column_running_modify_value-"],
                        "runningId: ",
                        values["-column_running_modify_runningId-"],
                    )

                if event == "Show diet records":
                    records = database_operations.showRecordsFromTableMatchingQuery(
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        table="diet",
                        column="name",
                        criterion="2000_calories",
                    )
                    # print = window.FindElement("_OP_1_").update
                    window.find_element("_OP_1_").update("")
                    for x in records:
                        window.find_element("_OP_2_").update(
                            ("{}\n".format(x)), append=True
                        )
                        print(x)
                        # time.sleep(1)
                    pass
        window.close()

    if isUserLogged == "USER_LOGGED" and username.find("super") == 0:
        column, criterion = "", ""
        mycursor = connection.cursor(prepared=True)

        window = sg.Window("Super user account", gui.super_user_layout_normal)
        while True:
            event, values = window.read()
            if event in (None, "Exit") or event == sg.WIN_CLOSED:
                break
            elif event in (None, "About"):
                sg.popup("Help", "page", keep_on_top=True)
            else:
                backupName = values["-backup_name-"]
                if event == "Make backup":
                    if backupName == "":
                        database_operations.createDatabaseBackup(
                            mysqldumpPassword=password
                        )
                    else:
                        database_operations.createDatabaseBackup(
                            mysqldumpPassword=password, backupName=backupName
                        )

    if (
        emergency_login == "YES"
        and username == "super_user"
        and password == superUserPassword
    ):
        window = sg.Window("Super user account", gui.super_user_layout_emergency)
        while True:
            event, values = window.read()
            if event in (None, "Exit") or event == sg.WIN_CLOSED:
                break
            elif event in (None, "About"):
                sg.popup("Help", "page", keep_on_top=True)
            else:
                backupName = values["-backup_name-"]
                if event == "Restore backup":
                    database_operations.createDatabase(
                        host="localhost", user=username, password=password
                    )
                    database_operations.restoreDatabaseBackup(
                        mysqldumpPassword=password, backupName=backupName
                    )
        window.close()


if __name__ == "__main__":
    main()


# ref:
# https://stackoverflow.com/questions/64398194/pysimplegui-login-authenticator
