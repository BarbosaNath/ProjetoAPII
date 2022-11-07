import PySimpleGUI as sg
import debug_layouts as layouts

sg.theme("Reddit")

global_size = (400, 150)

layout = [[
    sg.Column(layouts.show, key="col-show", pad=(0,0), visible=False),
    sg.Column(layouts.main, key="col-main", pad=(0,0))
]]

window = sg.Window("Programa Foda", layout, finalize=True, margins=(0, 0))
# window.maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "cancel": break

    if event == "back":
        window['col-show'].update(visible=False)
        window['col-main'].update(visible=True)
        
    if event == "show_db":
        window['col-show'].update(visible=True)
        window['col-main'].update(visible=False)

    if event == "update":
        layouts.update_show()

window.close()