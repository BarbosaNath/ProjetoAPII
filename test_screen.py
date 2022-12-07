from   PySimpleGUI import Window, Column
import PySimpleGUI as sg
import tags
import modules as mod
from   functions import *
import database.database as db

from filters_layouts import *
from module_layouts  import *
from start_layouts   import *


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

loading = lambda: sg.popup_no_buttons('Carregando...', auto_close = True, auto_close_duration = .4,
                                                        no_titlebar = True, keep_on_top = True, non_blocking=True)

def generate_layout(first_screen):
    layout=[ [
            Column(tela_login(),        key='tela_login',        s=(210,500), visible=first_screen=="tela_login"       ),
            Column(tela_inicial(),      key='tela_inicial',      s=(210,500), visible=first_screen=="tela_inicial"     ),
            Column(choose_modules(),    key='modulos',           s=(210,500), visible=first_screen=="modulos"           ),
            Column(cadastro_modulo(),   key='cadastro_modulo',   s=(210,500), visible=first_screen=="cadastro_modulo"  ),
            # Column(cadastrar_filtros(), key='cadastrar_filtros', s=(210,500), visible=first_screen=="cadastrar_filtros"),
            Column(filtros(),           key='consultar_filtros', s=(210,500), visible=first_screen=="consultar_filtros", scrollable=True, vertical_scroll_only=True), 
            Column(create_acc(),        key='create_acc',        s=(210,500), visible=first_screen=="create_acc"       ),
            Column(layout_central(),    key='col_central',                    visible=True)
        ]
    ]

    mods = modules()
    prod = adicionar_produtos()

    for module in mods:
        # layout[0] += [Column(show_images(module), key=f'imagens_{module}', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False)]
        layout[0] += [Column(mods[module], key=f'modulo_{module}', s=(210,500), visible=False)]
        layout[0] += [Column(prod[module], key=f'adicionar_produto_{module}', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False)]

    return layout

loading()
window = Window('Foto Shopping', generate_layout("tela_inicial"), finalize=True)
window.bring_to_front()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "buton_cancel_login": break

    if   event == 'Cadastrar modulo':         swap_screens(window, 'modulos',           'cadastro_modulo')
    elif event == 'inicio':                   swap_screens(window, 'cadastro_modulo',   'modulos')
    elif event == 'Produtos':                 swap_screens(window, 'tela_inicial',      'modulos')
    elif event == 'Voltar':                   swap_screens(window, 'modulos',           'tela_inicial')
    elif event == 'Cadastrar Filtro':         swap_screens(window, 'tela_inicial',      'cadastrar_filtros')
    elif event == 'frente':                   swap_screens(window, 'cadastrar_filtros', 'tela_inicial')
    elif event == 'Consultar Filtros':        swap_screens(window, 'tela_inicial',      'consultar_filtros')
    elif event == 'retornar':                 swap_screens(window, 'consultar_filtros', 'tela_inicial')
    elif event == 'sair':                     swap_screens(window, 'tela_inicial',      'tela_login')
    elif event == 'adicionar_roupas':         swap_screens(window, 'modulo_roupas',     'adicionar_produtos')
    elif event == 'button_create_acc':        swap_screens(window, 'tela_login',        'create_acc')
    elif event == 'cancel_submit_create_acc': swap_screens(window, 'create_acc' ,       'tela_login')

    elif event == 'proceed_login':
        dados_login = db.get_table('database/test.db', 'usuario')

        for datum in dados_login:
            if datum[1] == values['login_user'] and datum[2] == values['login_password']:
                sg.popup('Olá {}, bem-vindo ao Foto Shopping'.format(values['login_user']))
                swap_columns(window,'tela_login', 'tela_inicial','col_central')
                break
        else:        
            sg.popup('Esta conta não existe!')


    elif event == 'submit_cadastro_modulo':
        _tag_groups = ''
        for group in tags.get_all_groups():
            if values[f'checkbox_tag_{group}']:
                _tag_groups += group+" "
        mod.create_module(values['nome_novo_produto'], _tag_groups)

        
        loading()
        window.close()
        window = sg.Window('Foto Shopping', generate_layout("modulos"), finalize=True)
        window.bring_to_front()


    elif type(event) == tuple:
        if event[0] == 'modules_reset_screen':
            if sg.popup_yes_no('Deseja mesmo excluir?', no_titlebar=True, grab_anywhere = True) == "No": continue

            event[1]()

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("modulos"), finalize=True)
            window.bring_to_front()


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
                        window[f"checkbox_cadastro_{event[1]}_{group}_{tag}"]('')


            db.add_to_db("database/modules.db", event[1], dados)
            swap_columns(window, f"adicionar_produto_{event[1]}", f"modulo_{event[1]}", "col_central")


            window['product_code']('')
            window["file_image"].InitialFolder = r"C:\\"
            window["file_image"]('Imagem')
            window['product_inventory']('')
            

    elif event == "submit_create_acc":
        sg.popup("Conta Criada")

        swap_columns(window, "create_acc" , "tela_login", "col_central")

        db.add_to_db("database/test.db", "usuario", {
            "user": values['create_user'],
            "password": values['create_password']
        })
        

    elif callable(event): event(window)
    

window.close()
