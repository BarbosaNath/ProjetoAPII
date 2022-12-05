from PySimpleGUI import Window, Button, Text, Column, VerticalSeparator
import PySimpleGUI as sg
from PIL import Image
import tags
import modules as mod
from functions import *
from image_manipulation import resize
import database.database as db

from filters_layouts import *
from module_layouts import *
from start_layouts import *

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

layout=[
    [Column(tela_login(), key='tela_login', s=(210,500), visible=True),
    Column(tela_inicial(), key='tela_inicial', visible=False, s=(210,500)),
    Column(choose_modules(), key='modulos', s=(210,500), visible=False),
    Column(cadastro_modulo(), key='cadastro_modulo', s=(210,500), visible=False),
    Column(cadastrar_filtros(), key='cadastrar_filtros', s=(210,500), visible=False),
    Column(filtros(), key='consultar_filtros', s=(210,500), scrollable=True, vertical_scroll_only=True, visible=False), 
    Column(create_acc(), key='create_acc', s=(210,500), visible=False),
    Column(layout_central(), key='col_central')
    ]
]
mods = modules()
prod = adicionar_produtos()

for module in mods:
    layout[0] += [Column(mods[module], key=f'modulo_{module}', s=(210,500), visible=False)]
    layout[0] += [Column(prod[module], key=f'adicionar_produto_{module}', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False)]

window = Window('Foto Shopping', layout=layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "buton_cancel_login": break

    if event == 'Roupas':             
        swap_columns(window,'modulos', 'modulo_roupas','col_central')
    elif event == 'Menu Principal':   
        swap_columns(window,'modulo_roupas', 'modulos','col_central')
    elif event == 'Cadastrar modulo': 
        swap_columns(window,'modulos', 'cadastro_modulo','col_central')
    elif event == 'inicio':           
        swap_columns(window,'cadastro_modulo', 'modulos','col_central')
    elif event == 'Produtos':
        swap_columns(window,'tela_inicial', 'modulos','col_central')
    elif event == 'Voltar':
        swap_columns(window,'modulos', 'tela_inicial','col_central')
    elif event == 'Cadastrar Filtro':
        swap_columns(window,'tela_inicial', 'cadastrar_filtros','col_central')
    elif event == 'frente':
        swap_columns(window,'cadastrar_filtros', 'tela_inicial','col_central')
    elif event == 'Consultar Filtros':
        swap_columns(window,'tela_inicial', 'consultar_filtros','col_central')
    elif event == 'retornar':
        swap_columns(window,'consultar_filtros', 'tela_inicial','col_central')
    elif event == 'sair':
        swap_columns(window,'tela_inicial', 'tela_login','col_central')
    elif event == 'proceed_login':
        dados_login = db.get_table('database/test.db', 'usuario')

        for datun in dados_login:
            if datun[1] == values['login_user']:
                if datun[2] == values['login_password']:
                    sg.popup('Olá {}, bem-vindo ao Foto Shopping'.format(values['login_user']))
                    swap_columns(window,'tela_login', 'tela_inicial','col_central')
                    break
        else:        
            sg.popup('Esta conta não existe!')

    elif event == 'adicionar_roupas':
        swap_columns(window,'modulo_roupas', 'adicionar_produtos','col_central')
    elif event == 'button_create_acc':
        swap_columns(window,'tela_login', 'create_acc','col_central')
    elif event == 'submit_cadastro_modulo':
        _tag_groups = ''
        for group in tags.get_all_groups():
            if values[f'checkbox_tag_{group}']:
                _tag_groups += group+" "
        mod.create_module(values['nome_novo_produto'], _tag_groups)

        layout=[
        [Column(tela_login(), key='tela_login', s=(210,500), visible=False),
        Column(tela_inicial(), key='tela_inicial', visible=False, s=(210,500)),
        Column(choose_modules(), key='modulos', s=(210,500), visible=True),
        Column(cadastro_modulo(), key='cadastro_modulo', s=(210,500), visible=False),
        Column(cadastrar_filtros(), key='cadastrar_filtros', s=(210,500), visible=False),
        Column(consultar_filtros(), key='consultar_filtros', s=(210,500), visible=False), 
        Column(create_acc(), key='create_acc', s=(210,500), visible=False),
        Column(layout_central(), key='col_central')
        ]
]

        mods = modules()
        prod = adicionar_produtos()

        for module in mods:
            layout[0] += [Column(mods[module], key=f'modulo_{module}', s=(210,500), visible=False)]
            layout[0] += [Column(prod[module], key=f'adicionar_produto_{module}', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False)]

        
        window.close()
        window = sg.Window('Foto Shopping', layout=layout, finalize=True)

    elif callable(event):
        event(window)
    elif type(event) == tuple:
        if event[0] == 'modules_reset_screen':
            if sg.popup_yes_no('Deseja mesmo excluir?') == "Yes":
                event[1]()

                layout=[
                    [Column(tela_login(), key='tela_login', s=(210,500), visible=False),
                    Column(tela_inicial(), key='tela_inicial', visible=False, s=(210,500)),
                    Column(choose_modules(), key='modulos', s=(210,500), visible=True),
                    Column(cadastro_modulo(), key='cadastro_modulo', s=(210,500), visible=False),
                    Column(cadastrar_filtros(), key='cadastrar_filtros', s=(210,500), visible=False),
                    Column(consultar_filtros(), key='consultar_filtros', s=(210,500), visible=False), 
                    Column(create_acc(), key='create_acc', s=(210,500), visible=False),
                    Column(layout_central(), key='col_central')
                    ]
                ]


                mods = modules()
                prod = adicionar_produtos()

                for module in mods:
                    layout[0] += [Column(mods[module], key=f'modulo_{module}', s=(210,500), visible=False)]
                    layout[0] += [Column(prod[module], key=f'adicionar_produto_{module}', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False)]

                window.close()
                window = sg.Window('Foto Shopping', layout=layout, finalize=True)
        elif event[0] == "button_add_product":
            dados = {
                "code": values["product_code"],
                "image": values["file_image"],
                "tags": "",
                "inventory": int(values["product_inventory"])
            }

            for group in mod.get_tags(event[1]):
                for tag in tags.get_tag_group(group):
                    tag = tag[0]
                    if values[f"checkbox_cadastro_{event[1]}_{group}_{tag}"]:
                        dados["tags"] += f"{group}->{tag} "


            db.add_to_db("database/modules.db", event[1], dados)
            swap_columns(window, f'modulo_{event[1]}', "modulos", "col_central")

    elif event == "submit_create_acc":
        sg.popup("Conta Criada")

        swap_columns(window, "create_acc" , "tela_login", "col_central")

        db.add_to_db("database/test.db", "usuario", {
            "user": values['create_user'],
            "password": values['create_password']
        })
    
    elif event == "cancel_submit_create_acc":
        swap_columns(window, "create_acc" , "tela_login", "col_central")

window.close()