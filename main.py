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
                try:
                    window_register = sg.Window("Sign Up", gui.register_layout)
                    while True:
                        event_register, values_register = window_register.read()
                        if (
                            event_register == "Cancel"
                            or event_register == sg.WIN_CLOSED
                        ):
                            break
                        else:
                            if event_register == "Submit":
                                first_name = values_register["-register_first_name-"]
                                last_name = values_register["-register_last_name-"]
                                birth_date = values_register["-register_birth_date-"]
                                phone_number = values_register[
                                    "-register_phone_number-"
                                ]
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
                                else:
                                    message = "Your username: " + userName
                                    sg.popup(message)
                                    gui.progress_bar_register()
                                    break
                    window_register.close()
                except:
                    pass
    window_login.close()

    #### user is logged
    global column
    global criterion
    global person_id
    if isUserLogged == "USER_LOGGED":
        column, criterion = "", ""
        mycursor = connection.cursor(prepared=True)

        if username == "super_user":
            window = sg.Window("Super user account", gui.super_user_layout)
        elif username == "admin_user":
            window = sg.Window("Admin user account", gui.admin_user_layout)
        elif username.find("super") == -1 and username.find("admin") == -1:
            window = sg.Window("User account", gui.user_layout)
            person_id = int(username[5:])

        while True:
            event, values = window.read()
            if event in (None, "Exit") or event == sg.WIN_CLOSED:
                break
            elif event in (None, "About"):
                sg.popup("Help", "page", keep_on_top=True)
            else:
                if username == "super_user":
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

                if event == "Select user":
                    person_id = values["-userID-"]

                if event == "Show running records":
                    try:
                        records = database_operations.showRecordsFromTableMatchingQuery(
                            cursor=mycursor,
                            person_id=person_id,
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
                    except:
                        pass

                if event == "Add running record":
                    try:
                        database_operations.addRecordToRunningTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            date=values["-column_running_add_date-"],
                            type=values["-column_running_add_type-"],
                            total_time=values["-column_running_add_time-"],
                            total_distance=values["-column_running_add_distance-"],
                            terrain=values["-column_running_add_terrain-"],
                        )
                    except:
                        pass

                if event == "Delete running record":
                    try:
                        database_operations.deleteRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="running",
                            recordId=values["-column_running_delete_runningId-"],
                        )
                    except:
                        pass

                if event == "Modify running record":
                    try:
                        database_operations.modifyRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="running",
                            column=values["-column_running_modify_column-"],
                            value=values["-column_running_modify_value-"],
                            recordId=values["-column_running_modify_runningId-"],
                        )
                    except:
                        pass

                if event == "Show diet records":
                    try:
                        records = database_operations.showRecordsFromTableMatchingQuery(
                            cursor=mycursor,
                            person_id=person_id,
                            table="diet",
                            column=values["-column_diet_show-"],
                            criterion=values["-criterion_diet_show-"],
                        )
                        # print = window.FindElement("_OP_1_").update
                        window.find_element("_OP_2_").update("")
                        for x in records:
                            window.find_element("_OP_2_").update(
                                ("{}\n".format(x)), append=True
                            )
                            print(x)
                            # time.sleep(1)
                    except:
                        pass

                if event == "Add diet record":
                    try:
                        database_operations.addRecordToDietTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            name=values["-column_diet_add_name-"],
                            start_date=values["-column_diet_add_start_date-"],
                            stop_date=values["-column_diet_add_stop_date-"],
                            calories=values["-column_diet_add_calories-"],
                        )
                    except:
                        pass

                if event == "Delete diet record":
                    try:
                        database_operations.deleteRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="diet",
                            recordId=values["-column_diet_delete_dietId-"],
                        )
                    except:
                        pass

                if event == "Modify diet record":
                    try:
                        database_operations.modifyRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="diet",
                            column=values["-column_diet_modify_column-"],
                            value=values["-column_diet_modify_value-"],
                            recordId=values["-column_diet_modify_dietId-"],
                        )
                    except:
                        pass

                if event == "Show weight lifting records":
                    try:
                        records = database_operations.showRecordsFromTableMatchingQuery(
                            cursor=mycursor,
                            person_id=person_id,
                            table="weight_lifting",
                            column=values["-column_weight_lifting_show-"],
                            criterion=values["-criterion_weight_lifting_show-"],
                        )
                        # print = window.FindElement("_OP_1_").update
                        window.find_element("_OP_3_").update("")
                        for x in records:
                            window.find_element("_OP_3_").update(
                                ("{}\n".format(x)), append=True
                            )
                            print(x)
                            # time.sleep(1)
                    except:
                        pass

                if event == "Add weight lifting record":
                    try:
                        database_operations.addRecordToWeightLiftingTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            date=values["-column_weight_lifting_add_date-"],
                            type=values["-column_weight_lifting_add_type-"],
                            no_series=values["-column_weight_lifting_add_no_series-"],
                            repeats_per_series=values[
                                "-column_weight_lifting_add_repeats_per_series-"
                            ],
                            weight=values["-column_weight_lifting_add_weight-"],
                        )
                    except:
                        pass

                if event == "Delete weight lifting record":
                    try:
                        database_operations.deleteRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="weight_lifting",
                            recordId=values[
                                "-column_weight_lifting_delete_weight_liftingId-"
                            ],
                        )
                    except:
                        pass

                if event == "Modify weight lifting record":
                    try:
                        database_operations.modifyRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="weight_lifting",
                            column=values["-column_weight_lifting_modify_column-"],
                            value=values["-column_weight_lifting_modify_value-"],
                            recordId=values[
                                "-column_weight_lifting_modify_weight_liftingId-"
                            ],
                        )
                    except:
                        pass

                if event == "Show swimming records":
                    try:
                        records = database_operations.showRecordsFromTableMatchingQuery(
                            cursor=mycursor,
                            person_id=person_id,
                            table="swimming",
                            column=values["-column_swimming_show-"],
                            criterion=values["-criterion_swimming_show-"],
                        )
                        # print = window.FindElement("_OP_1_").update
                        window.find_element("_OP_4_").update("")
                        for x in records:
                            window.find_element("_OP_4_").update(
                                ("{}\n".format(x)), append=True
                            )
                            print(x)
                            # time.sleep(1)
                    except:
                        pass

                if event == "Add swimming record":
                    try:
                        database_operations.addRecordToSwimmingTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            date=values["-column_swimming_add_date-"],
                            type=values["-column_swimming_add_type-"],
                            total_time=values["-column_swimming_add_time-"],
                            total_distance=values["-column_swimming_add_distance-"],
                            water=values["-column_swimming_add_water-"],
                        )
                    except:
                        pass

                if event == "Delete swimming record":
                    try:
                        database_operations.deleteRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="swimming",
                            recordId=values["-column_swimming_delete_swimmingId-"],
                        )
                    except:
                        pass

                if event == "Modify swimming record":
                    try:
                        database_operations.modifyRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="swimming",
                            column=values["-column_swimming_modify_column-"],
                            value=values["-column_swimming_modify_value-"],
                            recordId=values["-column_swimming_modify_swimmingId-"],
                        )
                    except:
                        pass

                if event == "Show rest records":
                    try:
                        records = database_operations.showRecordsFromTableMatchingQuery(
                            cursor=mycursor,
                            person_id=person_id,
                            table="rest",
                            column=values["-column_rest_show-"],
                            criterion=values["-criterion_rest_show-"],
                        )
                        # print = window.FindElement("_OP_1_").update
                        window.find_element("_OP_5_").update("")
                        for x in records:
                            window.find_element("_OP_5_").update(
                                ("{}\n".format(x)), append=True
                            )
                            print(x)
                            # time.sleep(1)
                    except:
                        pass

                if event == "Add rest record":
                    try:
                        database_operations.addRecordToRestTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            date=values["-column_rest_add_date-"],
                            night_sleep_hours=values[
                                "-column_rest_add_night_sleep_hours-"
                            ],
                            relax_hours=values["-column_rest_add_relax_hours-"],
                        )
                    except:
                        pass

                if event == "Delete rest record":
                    try:
                        database_operations.deleteRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="rest",
                            recordId=values["-column_rest_delete_restId-"],
                        )
                    except:
                        pass

                if event == "Modify rest record":
                    try:
                        database_operations.modifyRecordFromAnyTable(
                            connection=connection,
                            cursor=mycursor,
                            person_id=person_id,
                            table="rest",
                            column=values["-column_rest_modify_column-"],
                            value=values["-column_rest_modify_value-"],
                            recordId=values["-column_rest_modify_restId-"],
                        )
                    except:
                        pass

        window.close()

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
                backupName = values["-backup_name_emergency-"]
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
