import PySimpleGUI as sg
from layouts import login, create_account, main_menu, bg_left, bg_right
from debug import Log
import database.database as db
from functions import swap_columns
# from database.database import add_to_db


sg.theme("Reddit")
# Debug(sg.theme("DarkGrey2")) # Exemplo de Debug()

global_size = (400, 150)

layout = [[
    sg.Column(bg_left, key='col-bg_left', pad=(0, 0)),
    sg.Column(login, s=global_size, key='col-login'),
    sg.Column(create_account, s=global_size, key='col-logup', visible=False),
    sg.Column(main_menu, s=global_size, key='col-main', visible=False),
    sg.Column(bg_right, key='col-bg_right', pad=(0, 0)),
]]

window = sg.Window("Programa Foda", layout, finalize=True, margins=(0, 0))
# window.maximize()

while True:
    event, values = window.read()

    Log(event, values) # Exemplo de Log()

    if event == sg.WIN_CLOSED or event == "Cancelar": break

    elif event == "proceed_login": 
        swap_columns(window, "col-login", "col-main", "col-bg_right")

    elif event == "create_account":
        swap_columns(window, "col-login", "col-logup", "col-bg_right")

    elif "back_to_login" in event:
        swap_columns(window, "col-main" , "col-login", "col-bg_right")
        swap_columns(window, "col-logup", "col-login", "col-bg_right")

    elif event == "Criar conta":
        sg.popup("Conta Criada")

        swap_columns(window, "col-logup" , "col-login", "col-bg_right")

        db.add_to_db("database/test.db", "usuario", {
          "name": values['create_user'],
          "email": values['create_email'],
          "password": values['create_password']
        })

        Log("Teste: ",values['create_user'], values['create_email'], values['create_password'])

    elif callable(event):
        event(window)

window.close()
