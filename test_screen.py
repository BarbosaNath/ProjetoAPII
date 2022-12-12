from   PySimpleGUI import Window, Column
import PySimpleGUI as sg
import tags
import modules as mod
from   functions import *
import database.database as db

import sqlite3

from filters_layouts import *
from module_layouts  import *
from start_layouts   import *

import os, subprocess, sys, shutil

# def rmtree(top):
#     for root, dirs, files in os.walk(top, topdown=False):
#         for name in files:
#             filename = os.path.join(root, name)
#             os.chmod(filename, stat.S_IWUSR)
#             os.remove(filename)
#         for name in dirs:
#             os.rmdir(os.path.join(root, name))
#     os.rmdir(top)      

# TODO: ADICIONAR ROUPA TA BUGANDO TELA

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
            Column(tela_login(),              key='tela_login',                  s=(210,500), visible=first_screen=="tela_login"),
            Column(tela_inicial(),            key='tela_inicial',                s=(210,500), visible=first_screen=="tela_inicial"),
            Column(choose_modules(),          key='modulos',                     s=(210,500), visible=first_screen=="modulos"),
            Column(cadastro_modulo(),         key='cadastro_modulo',             s=(210,500), visible=first_screen=="cadastro_modulo"),
            Column(cadastrar_grupo_filtros(), key='tela_cadastrar_grupo_filtro', s=(210,500), visible=first_screen=="tela_cadastrar_grupo_filtro"),
            Column(cadastrar_filtro(),        key='tela_cadastrar_filtro',       s=(210,500), visible=first_screen=="tela_cadastrar_filtro"),
            Column(filtros(),                 key='consultar_filtros',           s=(210,500), visible=first_screen=="consultar_filtros", scrollable=True, vertical_scroll_only=True), 
            Column(create_acc(),              key='create_acc',                  s=(210,500), visible=first_screen=="create_acc"),
            Column(layout_central(),          key='col_central', visible=True)
        ]
    ]

    mods = modules()
    prod = adicionar_produtos()


    for module in mods:
        layout[0] += [Column([[sg.VerticalSeparator(), Column(show_images(module), s=(600, 600))]], key=f"images_{module}", scrollable=True, vertical_scroll_only=True, s=(607,606), visible=False)]
        layout[0] += [Column(mods[module], key=f'modulo_{module}', s=(210,500), visible=False)]
        layout[0] += [Column(prod[module], key=f'adicionar_produto_{module}', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False)]
    return layout

loading()
window = Window('Foto Shopping', generate_layout("tela_inicial"), finalize=True)
window.bring_to_front()

while True:
    event, values = window.read()

    if   event == sg.WIN_CLOSED or event == "buton_cancel_login": break
    elif event == 'Cadastrar Modulo':         swap_screens(window, 'modulos',           'cadastro_modulo')
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


    # ===============================================================
    elif type(event) == tuple:
        if event[0] == 'modules_reset_screen':
            if sg.popup_yes_no('Deseja mesmo excluir?', no_titlebar=True, grab_anywhere = True) == "No": continue

            event[1]()

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("modulos"), finalize=True)
            window.bring_to_front()

        elif event[0] == "editar_estoque":
            inventory = sg.popup_get_text(f"Digite o novo estoque de {event[2]}:")
            if inventory is None: continue
            if inventory == "":
                sg.popup_no_buttons(f"Estoque não pode ser vazio!", background_color = "red", auto_close = True, auto_close_duration = 1, no_titlebar = True, keep_on_top = True)
                continue

            try:
                mod.change_inventory(event[1], event[2], int(inventory))
            except:
                sg.popup_no_buttons(f"Estoque tem que ser um número!", background_color = "red", auto_close = True, auto_close_duration = 1, no_titlebar = True, keep_on_top = True)
                continue

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout(f"modulos"), finalize=True)
            window.bring_to_front()

            swap_columns(window, f"modulos", f"modulo_{event[1]}")
            swap_columns(window, "col_central", f"images_{event[1]}")

        elif event[0] == "botao_pesquisar_module":
            products = mod.get_module(event[1])


            for code in products: 
                window[f'image_{event[1]}_{code}'].update(visible=True)
                for group in mod.get_tags(event[1]):
                    for tag in tags.get_tag_group(group):
                        tag = tag[0]
                        if f"{group}->{tag}" not in products[code]["tags"] and values[f"combo_{event[1]}_{group}"] == tag:
                            window[f'image_{event[1]}_{code}'].update(visible=False)
                

        elif event [0] == 'deletar_produto_estoque':
            if sg.popup_yes_no('Deseja mesmo excluir?', no_titlebar=True, grab_anywhere = True) == "No": continue

            mod.remove_product(event[1], event[2])

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout(f"modulos"), finalize=True)
            window.bring_to_front()

            swap_columns(window, f"modulos", f"modulo_{event[1]}")
            swap_columns(window, "col_central", f"images_{event[1]}")


        elif event[0] == "botao_pegar_imagens": 
            products = mod.get_module(event[1])
            os.mkdir(dir := './temp')
            for code in products:
                if values[f"checkbox_{code}"]:
                    arquivo = products[code]["image"].split('/')[-1]
                    shutil.copy2(products[code]["image"], dir+"/"+arquivo)
            #  sg.popup_get_file("Ctrl+A e arraste as imagens para o whatsapp!", default_path = dir)
            if "win" in sys.platform: subprocess.Popen(fr'explorer /select,.\temp\{arquivo}')
            else: os.system("xdg-open ./temp")

            sg.popup("Selecione as imagens e arraste-as para a ferramenta de contato com o cliente!")      

            if "win" in sys.platform: os.system(f'rmdir /Q /S .\\temp')
            else: os.system(f'rmdir -rf ./temp')


            window.bring_to_front()

        elif event[0] == "delete_filter_group":
            if sg.popup_yes_no('Deseja mesmo excluir?', no_titlebar=True, grab_anywhere = True) == "No": continue

            tags.remove_tag_group(event[1])

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("consultar_filtros"), finalize=True)
            window.bring_to_front()


        elif event[0] == "delete_filter":
            if sg.popup_yes_no('Deseja mesmo excluir?', no_titlebar=True, grab_anywhere = True) == "No": continue

            tags.remove_tag(event[1], f"'{event[2]}'")

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("consultar_filtros"), finalize=True)
            window.bring_to_front()


        elif event[0] == "adicionar_ao_grupo":
            tag = sg.popup_get_text("Digite o nome do novo filtro:")
            if tag is None: continue
            if tag == "":
                sg.popup_no_buttons(f"Filtro não pode ser vazio!", background_color = "red", auto_close = True, auto_close_duration = 1, no_titlebar = True, keep_on_top = True)
                continue

            try:
                tags.add_tags_to_group(event[1], tag)
            except sqlite3.IntegrityError:
                sg.popup_no_buttons(f"Filtro {tag} já existe!", background_color = "red", auto_close = True, auto_close_duration = 1, no_titlebar = True, keep_on_top = True)
                continue

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("consultar_filtros"), finalize=True)
            window.bring_to_front()

            sg.popup_no_buttons(f"Grupo {values['create_new_tag_group_name']} criado com sucesso", background_color="green", auto_close = True, auto_close_duration = .5, no_titlebar = True, keep_on_top = True)
            window.bring_to_front()

            window['create_new_tag_group_name']('')

        elif event[0] == "button_add_product":
            dados = {
                "code": values["product_code"],
                "image": values["file_image"],
                "tags": "",
                "inventory": int(values["product_inventory"])
            }

            for group in mod.get_tags(event[1]):
                try:
                    for tag in tags.get_tag_group(group):
                        tag = tag[0]
                        if values[f"checkbox_cadastro_{event[1]}_{group}_{tag}"]:
                            dados["tags"] += f"{group}->{tag} "
                            window[f"checkbox_cadastro_{event[1]}_{group}_{tag}"]('')
                except: pass


            db.add_to_db("database/modules.db", event[1], dados)

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("modulos"), finalize=True)
            window.bring_to_front()

            swap_columns(window, f"modulos", f"modulo_{event[1]}")
            swap_columns(window, "col_central", f"images_{event[1]}")
            

        elif event[0] == "modulo_escolhido":
            swap_columns(window, "modulos", f"modulo_{event[1]}")
            swap_columns(window, "col_central", f"images_{event[1]}")

        elif event[0] == "voltar_para_choose_modules":
            swap_columns(window, f"modulo_{event[1]}", "modulos")
            swap_columns(window, f"images_{event[1]}", "col_central")

        elif event[0] == "voltar_do_add_produtos": 
            swap_columns(window, f"adicionar_produto_{event[1]}", f'modulo_{event[1]}')
            swap_columns(window, "col_central", f"images_{event[1]}")

        elif event[0] == "ir_add_product":
            swap_columns(window, f'modulo_{event[1]}', f'adicionar_produto_{event[1]}')
            swap_columns(window, "col_central", f"images_{event[1]}")
        
        elif event[0] == "adicionar_grupo_a_modulo":
            new_group = popup_select_new_tag_group()
            if new_group is None: continue
            mod.add_tag_group(event[1], new_group.replace(" ", "_").lower())

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("modulos"), finalize=True)
            window.bring_to_front()

            swap_columns(window, f"modulos", f"modulo_{event[1]}")
            swap_columns(window, "col_central", f"images_{event[1]}")

        elif event[0] == "remover_grupo_de_modulo":
            if sg.popup_yes_no('Deseja mesmo excluir?', no_titlebar=True, grab_anywhere = True) == "No": continue

            mod.remove_tag_group(event[1], event[2].replace(" ", "_").lower())

            loading()
            window.close()
            window = sg.Window('Foto Shopping', generate_layout("modulos"), finalize=True)
            window.bring_to_front()

            swap_columns(window, f"modulos", f"modulo_{event[1]}")
            swap_columns(window, "col_central", f"images_{event[1]}")


    elif event == "botao_adicionar_grupo":
        group = sg.popup_get_text("Digite o nome do novo Grupo de Filtros:")
        if group is None: continue
        if group == "":
            sg.popup_no_buttons(f"Grupo de Filtros não pode ser vazio!", background_color = "red", auto_close = True, auto_close_duration = 1, no_titlebar = True, keep_on_top = True)
            continue

        tags.create_tag_group(group)

        loading()
        window.close()
        window = sg.Window('Foto Shopping', generate_layout("consultar_filtros"), finalize=True)
        window.bring_to_front()

    elif event == "submit_create_acc":
        sg.popup("Conta Criada")

        swap_columns(window, "create_acc" , "tela_login", "col_central")

        db.add_to_db("database/test.db", "usuario", {
            "user": values['create_user'],
            "password": values['create_password']
        })

    elif callable(event): event(window)
    

window.close()
