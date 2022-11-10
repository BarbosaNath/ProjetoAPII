import PySimpleGUI as sg
import debug_layouts as layouts

sg.theme("Reddit")

global_size = (400, 150)

layout = [[
    sg.Column(layouts.update_show("col-show"), key="col-show", pad=(0,0), visible=False),
    sg.Column(layouts.generate_main(), s=(300,300), key="col-main", pad=(0,0))
]]

window = sg.Window("programa", layout, finalize=False, margins=(0, 0))
# window.maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "cancel": break

    if callable(event):
        event(window)
    elif event == "update":
        window.close()
        layout = [[
            sg.Column(layouts.update_show("col-show"), key="col-show", pad=(0,0)),
            sg.Column(layouts.generate_main(), s=(300,300), key="col-main", pad=(0,0), visible=False)
        ]]
        window = sg.Window("programa", layout, finalize=False, margins=(0,0))

window.close()
