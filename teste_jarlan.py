import image_manipulation as img
from PySimpleGUI import Window, Button, Text, Column, VerticalSeparator
import PySimpleGUI as sg
from PIL import Image
import tags

sg.LOOK_AND_FEEL_TABLE['FotoShopping'] = {
                                        'BACKGROUND': '#f6fcff',
                                        'TEXT':       '#000000',
                                        'INPUT':      '#ffffff',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL':     '#f6fcff',
                                        'BUTTON':    ('#f6fcff', '#4d3efc'),
                                        'PROGRESS':  ('#f6fcff', '#4d3efc'),
                                        'BORDER': 1,
                                        'SLIDER_DEPTH': 0, 
                                        'PROGRESS_DEPTH': 0, }
# set the default theme to our own
sg.theme("FotoShopping")



layout_direita = [
        [sg.Text("Produto:"),sg.InputText()],
        [sg.Text("Tags:")],
        [sg.Checkbox(Tag) for Tag in tags.get_all_groups()],
        [sg.Checkbox(Tag)for Tag in tags.get_all_groups()],
        [sg.Button("Create Tag")]

]

layout_esquerda = [
        [sg.Image(img.resize("icone.png",80,80)),sg.Text("Bruno Nascimento")],
        [sg.Button("Confirmar",key="Confirmar")],
        [sg.Button("Cancelar",key="Cancelar")],
        
    
        ]

layout = [[Column(layout_esquerda,s=(210,500)),sg.VerticalSeparator(),Column(layout_direita,s=(500,500))]]

window = Window("Foto Shopping", layout = layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Cancelar":
        break



window.close()