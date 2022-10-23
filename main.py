import PySimpleGUI as sg
from layouts import login, create_account, main_menu, bg_left, bg_right
from functions import update_selection

sg.theme("Reddit")

global_size = (400, 150)

layout = [[
    sg.Column(bg_left, key='col-bg_left', pad=(0,0)),
    sg.Column(login, s=global_size, key='col-login'),
    sg.Column(create_account, s=global_size, key='col-logup', visible=False),
    sg.Column(main_menu, s=global_size, key='col-main', visible=False),
    sg.Column(bg_right, key='col-bg_right', pad=(0,0)),
]]

window = sg.Window("Login", layout, finalize=True, margins=(0, 0))
# window.maximize()

update_selection(window, 'password', 'Password')
update_selection(window, 'login', 'Login')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel": break

    if event == "proceed_login":
        window['col-login'].update(visible=False)
        
        window['col-bg_right'].update(visible=False)
        window['col-main'].update(visible=True)
        window['col-bg_right'].update(visible=True)

    if event == "create_account":
        window['col-login'].update(visible=False)
        
        window['col-bg_right'].update(visible=False)
        window['col-logup'].update(visible=True)
        window['col-bg_right'].update(visible=True)

    if "back_to_login" in event:
        window['col-main'].update(visible=False)
        
        window['col-bg_right'].update(visible=False)
        window['col-login'].update(visible=True)
        window['col-logup'].update(visible=False)
        window['col-bg_right'].update(visible=True)

window.close()
