#### importing libraries
import database_operations
import gui
import PySimpleGUI as sg
import time

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

    username = ""
    password = ""
    global connection
    isUserLogged = "USER_NOT_LOGGED"

    # login window + trying to connect to DB + if connection successful then retrieve lobin/password to variables
    sg.theme("LightBlue2")
    login_layout = [
        [sg.Text("Log In", size=(15, 1), font=40)],
        [
            sg.Text("Username", size=(15, 1), font=16),
            sg.InputText(key="-username-", font=16),
        ],
        [
            sg.Text("Password", size=(15, 1), font=16),
            sg.InputText(key="-password-", password_char="*", font=16),
        ],
        [sg.Button("Login"), sg.Button("Cancel"), sg.Button("Register")],
    ]

    register_layout = [[sg.Text("Sign Up", size =(15, 1), font=40, justification='c')],
             [sg.Text("First name", size =(15, 1),font=16), sg.InputText(key='-register_first_name-', font=16)],
             [sg.Text("Last name", size =(15, 1),font=16), sg.InputText(key='-register_last_name-', font=16)],
             [sg.Text("Birth date", size =(15, 1),font=16), sg.InputText(key='-register_birth_date-', font=16)],
             [sg.Text("Phone number", size =(15, 1),font=16), sg.InputText(key='-register_phone_number-', font=16)],
             [sg.Text("Nationality", size =(15, 1),font=16), sg.InputText(key='-register_nationality-', font=16)],
             [sg.Text("Registration date", size =(15, 1),font=16), sg.InputText(key='-register_registration_date-', font=16)],
             [sg.Text("Password", size =(15, 1), font=16), sg.InputText(key='-register_password-', font=16, password_char='*')],
             [sg.Button("Submit"), sg.Button("Cancel")]]

    window_login = sg.Window("Log In", login_layout)

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
                    sg.popup("Invalid credentials. Try again")
                else:
                    username = values_login["-username-"]
                    password = values_login["-password-"]
                    # sg.popup("Welcome!")
                    gui.progress_bar_login()
                    isUserLogged = "USER_LOGGED"
                    break

            if event_login == "Register":
                window_register = sg.Window("Sign Up", register_layout)
                while True:
                    event_register,values_register = window_register.read()
                    if event_register == 'Cancel' or event_register == sg.WIN_CLOSED:
                        break
                    else:
                        if event_register == "Submit":
                            first_name = values_register['-register_first_name-']
                            last_name = values_register['-register_last_name-']
                            birth_date = values_register['-register_birth_date-']
                            phone_number = values_register['-register_phone_number-']
                            nationality = values_register['-register_nationality-']
                            registration_date = values_register['-register_registration_date-']
                            user_password = values_register['-register_password-']
                            
                            userName = database_operations.createUser(firstName=first_name, lastName=last_name, birthDate=birth_date, 
                            phoneNumber=phone_number, nationality=nationality, registrationDate=registration_date, 
                            userPassword=user_password, rootPassword=rootPassword)
                            
                            message = "Your username: " + userName
                            sg.popup(message)
                            gui.progress_bar_register()
                            break
                window_register.close()
    window_login.close()

    #### user is logged
    if (
        isUserLogged == "USER_LOGGED"
        and username.find("admin") == -1
        and username.find("super") == -1
    ):
        global column
        global criterion
        column, criterion = "", ""
        mycursor = connection.cursor(prepared=True)

        layout_running_main = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")]
        ]

        layout_running_show = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [sg.Button("Show running records")],
            [
                sg.Text("Column", size=(8, 1), font=16),
                sg.InputText(key="-column_running_show-", size=(10, 1), font=16),
                sg.Text("Criterion", size=(8, 1), font=16),
                sg.InputText(key="-criterion_running_show-", size=(10, 1), font=16),
            ],
            [sg.Text("What you print will display below:")],
            [sg.Multiline("", size=(100, 10), key="_OP_1_", do_not_clear=True)],
        ]

        layout_running_add = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [
                sg.Text("Date", size=(8, 1), font=16),
                sg.InputText(key="-column_running_add_date-", size=(10, 1), font=16),
                sg.Text("Type", size=(8, 1), font=16),
                sg.InputText(key="-column_running_add_type-", size=(10, 1), font=16),
                sg.Text("Time", size=(8, 1), font=16),
                sg.InputText(key="-column_running_add_time-", size=(10, 1), font=16),
                sg.Text("Distance", size=(8, 1), font=16),
                sg.InputText(
                    key="-column_running_add_distance-", size=(10, 1), font=16
                ),
                sg.Text("Terrain", size=(8, 1), font=16),
                sg.InputText(key="-column_running_add_terrain-", size=(10, 1), font=16),
            ],
            [sg.Button("Add running record")],
        ]

        layout_running_delete = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [
                sg.Text("Running ID", size=(8, 1), font=16),
                sg.InputText(
                    key="-column_running_delete_runningId-", size=(10, 1), font=16
                ),
            ],
            [sg.Button("Delete running record")],
        ]

        layout_running_modify = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [
                sg.Text("Running ID", size=(8, 1), font=16),
                sg.InputText(
                    key="-column_running_modify_runningId-", size=(10, 1), font=16
                ),
                sg.Text("Column", size=(8, 1), font=16),
                sg.InputText(
                    key="-column_running_modify_column-", size=(10, 1), font=16
                ),
                sg.Text("Value", size=(8, 1), font=16),
                sg.InputText(
                    key="-column_running_modify_value-", size=(10, 1), font=16
                ),
            ],
            [sg.Button("Modify running record")],
        ]

        diet_show = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [sg.Button("Show diet records")],
            [sg.Text("What you print will display below:")],
            [sg.Multiline("", size=(100, 10), key="_OP_2_", do_not_clear=True)],
        ]

        menu_def = [["Application", ["Exit"]], ["Help", ["About"]]]
        layout = [
            [sg.MenubarCustom(menu_def, key="-MENU-", font="Courier 15", tearoff=True)],
            [
                sg.Text(
                    "App title",
                    size=(100, 1),
                    justification="center",
                    font=("Helvetica", 16),
                    relief=sg.RELIEF_RIDGE,
                    k="-TEXT HEADING-",
                    enable_events=True,
                )
            ],
        ]
        layout += [
            [
                sg.TabGroup(
                    [
                        [
                            sg.Tab("RUNNING", layout_running_main),
                            sg.Tab("show", layout_running_show),
                            sg.Tab("add", layout_running_add),
                            sg.Tab("delete", layout_running_delete),
                            sg.Tab("modify", layout_running_modify),
                            sg.Tab("Diet - show", diet_show),
                        ]
                    ],
                    key="-TAB GROUP-",
                    expand_x=True,
                    expand_y=True,
                ),
            ]
        ]

        window = sg.Window("User account", layout)
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


if __name__ == "__main__":
    main()


# ref:
# https://stackoverflow.com/questions/64398194/pysimplegui-login-authenticator
