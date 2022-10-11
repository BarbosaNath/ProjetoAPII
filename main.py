import PySimpleGUI as sg
from layouts import login, create_account, main_menu
from functions import update_selection

sg.theme("Reddit")

layout = [[
    sg.Column(login, key='col-login'),
    sg.Column(create_account, key='col-logup', visible=False),
    sg.Column(main_menu, key='col-main', visible=False)]]

window = sg.Window("Login", layout, finalize=True)
window.maximize()

update_selection(window, 'password', 'Password')
update_selection(window, 'login', 'Login')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel": break

    if event == "proceed_login": 
        window['col-login'].update(visible=False)
        window['col-main'].update(visible=True)
            
    if event == "create_account":
        window['col-login'].update(visible=False)
        window['col-logup'].update(visible=True)
        
    if "back_to_login" in event:
        window['col-main' ].update(visible=False)
        window['col-login'].update(visible=True)
        window['col-logup'].update(visible=False)

window.close()
