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
        [sg.Button("Ok"), sg.Button("Cancel")],
    ]

    window_login = sg.Window("Log In", login_layout)

    while True:
        event, values = window_login.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                connection = database_operations.openConnectionToDB(
                    host="localhost",
                    user=values["-username-"],
                    password=values["-password-"],
                    database="WorkoutTrackerDB",
                )
                if connection == "ERROR":
                    sg.popup("Invalid credentials. Try again")
                else:
                    username = values["-username-"]
                    password = values["-password-"]
                    # sg.popup("Welcome!")
                    gui.progress_bar()
                    isUserLogged = "USER_LOGGED"
                    break

    window_login.close()

    if (
        isUserLogged == "USER_LOGGED"
        and username.find("admin") == -1
        and username.find("super") == -1
    ):
        global column
        global criterion
        column, criterion = "", ""
        mycursor = connection.cursor(prepared=True)
        layout_1 = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [sg.Button("Running records")],
            [sg.Text("Column", size=(8, 1), font=16), sg.InputText(key="-column_1-", font=16), sg.Text("Criterion", size=(7, 1), font=16), sg.InputText(key="-criterion_1-", font=16)],
            [sg.Text("What you print will display below:")],
            # [sg.Output(size=(50, 10), key="-OUTPUT_1-")],
            [sg.Multiline('', size=(100,10),key="_OP_1_", do_not_clear=True)]
        ]
        layout_2 = [
            [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
            [sg.Button("Diet records")],
            [sg.Text("What you print will display below:")],
            # [sg.Output(size=(50, 10), key="-OUTPUT-")],
            [sg.Multiline('', size=(100,10),key="_OP_2_", do_not_clear=True)]
        ]

        menu_def = [['Application', ['Exit']],
                ['Help', ['About']] ]
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
                            sg.Tab("Running", layout_1),
                            sg.Tab("Diet", layout_2),
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
            if event in (None, 'Exit') or event == sg.WIN_CLOSED:
                break
            elif event in (None, 'About'):
                sg.popup('Help',
                     'page', keep_on_top=True)
            else:
                if event == "Running records":
                    records = database_operations.showRecordsFromTableMatchingQuery(
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        table="running",
                        column=values["-column_1-"],
                        criterion=values["-criterion_1-"],
                    )
                    # print = window.FindElement("_OP_1_").update
                    window.find_element( "_OP_1_" ).update("")
                    for x in records:
                        window.find_element( "_OP_1_" ).update(("{}\n".format(x)),append=True)
                        print(x)
                        # time.sleep(1)
                    pass
                if event == "Diet records":
                    records = database_operations.showRecordsFromTableMatchingQuery(
                        cursor=mycursor,
                        person_id=int(username[5:]),
                        table="diet",
                        column="name",
                        criterion="2000_calories",
                    )
                    # print = window.FindElement("_OP_1_").update
                    window.find_element( "_OP_1_" ).update("")
                    for x in records:
                        window.find_element( "_OP_2_" ).update(("{}\n".format(x)),append=True)
                        print(x)
                        # time.sleep(1)
                    pass
        window.close()


if __name__ == "__main__":
    main()


# ref:
# https://stackoverflow.com/questions/64398194/pysimplegui-login-authenticator
