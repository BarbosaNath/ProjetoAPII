import PySimpleGUI as sg
from image_manipulation import resize
from functions import *
import modules as mod
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

# --------------------------------------------------------------------------------------------------------------------------#

def choose_modules():
    _choose_modules=[
        gerar_botao_logout('modulos'),
        [sg.Text('Qual tipo de produto irá trabalhar?')]]

    for module in mod.get_all_modules():
        _choose_modules.append([Botao(module.capitalize(), 'modulos',  f'modulo_{module}'), sg.Push(), sg.Button("❌", s=(2,1), key=("modules_reset_screen", lambda: mod.remove_module(module)), button_color=("white", "darkred"))])    
    _choose_modules.append([sg.Button('Cadastrar modulo', button_color=('white', 'green'))])
    _choose_modules.append([sg.VPush()])
    _choose_modules.append([sg.Button('Voltar', button_color=('white','purple'))])
    return _choose_modules

# --------------------------------------------------------------------------------------------------------------------------#

def modules():
    _modules=dict()
    for module in mod.get_all_modules():
        _modules[module]=[
        gerar_botao_logout(f'modulo_{module}'),
        [sg.Push()],
        [Botao(f'Adicionar {module.capitalize()}', f'modulo_{module}', f'adicionar_produto_{module}')],
        [sg.Text('Filtros:', size=(10,1))]]

        for group in tags.get_all_groups():
            if (group in mod.get_tags(module)):
                _modules[module] += [ 
                    [sg.Text(group.replace('_', ' ').capitalize())],
                    [sg.Combo(
                        [tag[0].replace('_', ' ').capitalize() for tag in tags.get_tag_group(group)],
                        s=(15, 22),
                        enable_events=True,
                        readonly=True,
                        )] ]

        _modules[module] += [   [sg.Push()],
                                [sg.Button("Pesquisar")],
                                [Botao('Menu Principal',  f'modulo_{module}', 'modulos')]
                            ]
    return _modules

# --------------------------------------------------------------------------------------------------------------------------#
def cadastro_modulo():
    _cadastro_modulo=[
        gerar_botao_logout('cadastro_modulo'),
        [sg.Text('Cadastre o tipo de produto')],
        [sg.Text('Tipo:'), sg.Input(s=15, key='nome_novo_produto')],
        [sg.Text('Defina os filtros a serem ultilizados:')]]

    for group in tags.get_all_groups():
        _cadastro_modulo.append([sg.Checkbox(group.replace('_', ' ').capitalize(), key=f'checkbox_tag_{group}')])

    _cadastro_modulo+=[
        [sg.Button('Cadastrar filtro')],
        [sg.VPush()],
        [sg.Button('Criar', key='submit_cadastro_modulo', button_color=('white', 'green'))],
        [sg.Button('Menu Principal', key='inicio')]
    ]
    return _cadastro_modulo  

# --------------------------------------------------------------------------------------------------------------------------#
def adicionar_produtos():

    
    _adicionar_produtos = dict()
    for module in mod.get_all_modules():
        _adicionar_produtos[module]=[
            gerar_botao_logout(f'adicionar_produto_{module}'),
            [sg.Text(f'Adicione um(a) {module[:-1]}:')],
            [sg.Input(s=15)],
            [sg.Push()],
            [sg.Text('Atribua filtros a esse produto:')]]
        for group in tags.get_all_groups():
            _adicionar_produtos[module].append([sg.Text(group.capitalize()+':')])
            for tag in tags.get_tag_group(group):
                _adicionar_produtos[module].append([sg.Text(s=2), sg.Checkbox(tag)])
        _adicionar_produtos[module].append([sg.Button('Adicionar')])
        
        _adicionar_produtos[module].append([Botao("Voltar", f"adicionar_produto_{module}", "modulos")])
        
    return _adicionar_produtos

# --------------------------------------------------------------------------------------------------------------------------#

  