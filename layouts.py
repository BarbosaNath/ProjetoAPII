import PySimpleGUI as sg
from functions import resize

sg.theme("Reddit")

#screen_size = win().winfo_screenwidth(), win().winfo_screenHeight() 


bg_left  = [[sg.Image(resize('res/bglphb', .1),pad=(0,0))]]
bg_right = [[sg.Image(resize('res/bgrphb', .1),pad=(0,0))]]


# ---------------------------------------------------------------------------------------
login = [[sg.Text("Login:", size=(10, 1)),sg.InputText('Login', key='login')],
         [sg.Text("Password:", size=(10, 1)),sg.InputText('Password', key='password', password_char='•')],
         [sg.Button("Login", key='proceed_login', border_width=0, size=(7, 1)),sg.Button("Cancel", border_width=0, size=(7, 1)),sg.Button("Dont have an account?",key='create_account',border_width=0,button_color=('DodgerBlue3', 'white'))]]

# ---------------------------------------------------------------------------------------
create_account = [[sg.Text("Login:", size=(15, 1)),sg.InputText('Login', key='login')], 
                  [sg.Text("Email:", size=(15, 1)),  sg.InputText('Email', key='email')],
                  [sg.Text("Password:", size=(15, 1)),sg.InputText('Password',key='password',password_char='•')],
                  [sg.Text("Repeat Password:", size=(15, 1)),sg.InputText('Password',key='repeat_password',password_char='•')],
                  [sg.Button("Create Account", border_width=0),sg.Button("Cancel",key='back_to_login-A',border_width=0)]]

# ---------------------------------------------------------------------------------------
main_menu = [[sg.Button("Log out",key='back_to_login-B')],
            [sg.FileBrowse()]]
