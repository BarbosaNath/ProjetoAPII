import PySimpleGUI as sg
from   PySimpleGUI   import Window, Column
from   union_layouts import *


layout=[ [  Column(tela_inicial,      k='tela_inicial',      s=(210,500)),
            Column(menu_modulos,      k='modulos',           s=(210,500), visible=False),
            Column(cadastro_modulo,   k='cadastro_modulo',   s=(210,500), visible=False),
            Column(cadastrar_filtros, k='cadastrar_filtros', s=(210,500), visible=False),
            Column(consultar_filtros, k='consultar_filtros', s=(210,500), visible=False),
            Column(layout_central,    k='col_central'),
          ]
        ]


for modulo in modulos:
    layout[0].append(Column(modulos[modulo], k=f'modulo_{modulo}', s=(210,500), visible=False))


window = Window('Tela principal', layout=layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break
    elif callable(event):      event(window)
window.close()
