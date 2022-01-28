import PySimpleGUI as sg


username = ""
password = ""
# PROGRESS BAR
def progress_bar_register():
    sg.theme("LightBlue2")
    layout = [
        [sg.Text("Creating your account...")],
        [sg.ProgressBar(100, orientation="h", size=(20, 20), key="progbar")],
        [sg.Cancel()],
    ]

    window = sg.Window("Working...", layout)
    for i in range(100):
        event, values = window.read(timeout=1)
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        window["progbar"].update_bar(i + 1)
    window.close()


def progress_bar_login():
    sg.theme("LightBlue2")
    layout = [
        [sg.Text("Logging into your account...")],
        [sg.ProgressBar(40, orientation="h", size=(20, 20), key="progbar")],
        [sg.Cancel()],
    ]

    window = sg.Window("Working...", layout)
    for i in range(40):
        event, values = window.read(timeout=1)
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        window["progbar"].update_bar(i + 1)
    window.close()


def registerUserWindow():
    global username, password
    sg.theme("LightBlue2")
    layout = [
        [sg.Text("Sign Up", size=(15, 1), font=40, justification="c")],
        [
            sg.Text("E-mail", size=(15, 1), font=16),
            sg.InputText(key="-email-", font=16),
        ],
        [
            sg.Text("Re-enter E-mail", size=(15, 1), font=16),
            sg.InputText(key="-remail-", font=16),
        ],
        [
            sg.Text("Create Username", size=(15, 1), font=16),
            sg.InputText(key="-username-", font=16),
        ],
        [
            sg.Text("Create Password", size=(15, 1), font=16),
            sg.InputText(key="-password-", font=16, password_char="*"),
        ],
        [sg.Button("Submit"), sg.Button("Cancel")],
    ]

    window = sg.Window("Sign Up", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                password = values["-password-"]
                username = values["-username-"]
                if values["-email-"] != values["-remail-"]:
                    sg.popup_error("Error", font=16)
                    continue
                elif values["-email-"] == values["-remail-"]:
                    progress_bar()
                    break
    window.close()


# registerUserWindow()


def loginUserWindow():
    global username, password
    sg.theme("LightBlue2")
    layout = [
        [sg.Text("Log In", size=(15, 1), font=40)],
        [
            sg.Text("Username", size=(15, 1), font=16),
            sg.InputText(key="-usrnm-", font=16),
        ],
        [
            sg.Text("Password", size=(15, 1), font=16),
            sg.InputText(key="-pwd-", password_char="*", font=16),
        ],
        [sg.Button("Ok"), sg.Button("Cancel")],
    ]

    window = sg.Window("Log In", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                if values["-usrnm-"] == username and values["-pwd-"] == password:
                    sg.popup("Welcome!")
                    break
                elif values["-usrnm-"] != username or values["-pwd-"] != password:
                    sg.popup("Invalid loginUserWindow. Try again")

    window.close()


# loginUserWindow()

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
    [
        sg.Button("Login"),
        sg.Button("Cancel"),
        sg.Button("Register"),
        sg.Button("Emergency login"),
    ],
]

register_layout = [
    [sg.Text("Sign Up", size=(15, 1), font=40, justification="c")],
    [
        sg.Text("First name", size=(15, 1), font=16),
        sg.InputText(key="-register_first_name-", font=16),
    ],
    [
        sg.Text("Last name", size=(15, 1), font=16),
        sg.InputText(key="-register_last_name-", font=16),
    ],
    [
        sg.Text("Birth date", size=(15, 1), font=16),
        sg.InputText(key="-register_birth_date-", font=16),
    ],
    [
        sg.Text("Phone number", size=(15, 1), font=16),
        sg.InputText(key="-register_phone_number-", font=16),
    ],
    [
        sg.Text("Nationality", size=(15, 1), font=16),
        sg.InputText(key="-register_nationality-", font=16),
    ],
    [
        sg.Text("Registration date", size=(15, 1), font=16),
        sg.InputText(key="-register_registration_date-", font=16),
    ],
    [
        sg.Text("Password", size=(15, 1), font=16),
        sg.InputText(key="-register_password-", font=16, password_char="*"),
    ],
    [sg.Button("Submit"), sg.Button("Cancel")],
]

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
        sg.InputText(key="-column_running_add_distance-", size=(10, 1), font=16),
        sg.Text("Terrain", size=(8, 1), font=16),
        sg.InputText(key="-column_running_add_terrain-", size=(10, 1), font=16),
    ],
    [sg.Button("Add running record")],
]

layout_running_delete = [
    [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
    [
        sg.Text("Running ID", size=(8, 1), font=16),
        sg.InputText(key="-column_running_delete_runningId-", size=(10, 1), font=16),
    ],
    [sg.Button("Delete running record")],
]

layout_running_modify = [
    [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
    [
        sg.Text("Running ID", size=(8, 1), font=16),
        sg.InputText(key="-column_running_modify_runningId-", size=(10, 1), font=16),
        sg.Text("Column", size=(8, 1), font=16),
        sg.InputText(key="-column_running_modify_column-", size=(10, 1), font=16),
        sg.Text("Value", size=(8, 1), font=16),
        sg.InputText(key="-column_running_modify_value-", size=(10, 1), font=16),
    ],
    [sg.Button("Modify running record")],
]

diet_show = [
    [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
    [sg.Button("Show diet records")],
    [sg.Text("What you print will display below:")],
    [sg.Multiline("", size=(100, 10), key="_OP_2_", do_not_clear=True)],
]

backup = [
    [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
    [
        sg.Text("Backup name", size=(8, 1), font=16),
        sg.InputText(key="-backup_name-", size=(10, 1), font=16),
    ],
    [sg.Button("Make backup")],
]

restore = [
    [sg.Text("Some info string", size=(15, 1), font=40, justification="c")],
    [
        sg.Text("Backup name", size=(8, 1), font=16),
        sg.InputText(key="-backup_name-", size=(10, 1), font=16),
    ],
    [sg.Button("Restore backup")],
]

menu_def = [["Application", ["Exit"]], ["Help", ["About"]]]
user_layout = [
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
user_layout += [
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

super_user_layout_normal = [
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
super_user_layout_normal += [
    [
        sg.TabGroup(
            [
                [
                    # sg.Tab("RUNNING", layout_running_main),
                    # sg.Tab("show", layout_running_show),
                    # sg.Tab("add", layout_running_add),
                    # sg.Tab("delete", layout_running_delete),
                    # sg.Tab("modify", layout_running_modify),
                    sg.Tab("BACKUP", backup),
                ]
            ],
            key="-TAB GROUP-",
            expand_x=True,
            expand_y=True,
        ),
    ]
]

super_user_layout_emergency = [
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
super_user_layout_emergency += [
    [
        sg.TabGroup(
            [
                [
                    # sg.Tab("RUNNING", layout_running_main),
                    # sg.Tab("show", layout_running_show),
                    # sg.Tab("add", layout_running_add),
                    # sg.Tab("delete", layout_running_delete),
                    # sg.Tab("modify", layout_running_modify),
                    sg.Tab("BACKUP", restore),
                ]
            ],
            key="-TAB GROUP-",
            expand_x=True,
            expand_y=True,
        ),
    ]
]
