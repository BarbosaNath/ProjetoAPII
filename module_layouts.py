import PySimpleGUI as sg
import modules as mod
import tags
from math import floor
from image_manipulation import resize
from functions import *

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
        _choose_modules.append([sg.Button(module.capitalize(), k=("modulo_escolhido", module)), sg.Push(), sg.Button("❌", s=(2,1), key=("modules_reset_screen", lambda: mod.remove_module(module)), button_color=("white", "darkred"))])    
    _choose_modules.append([sg.Button('Cadastrar modulo', button_color=('white', 'green'))])
    _choose_modules.append([sg.VPush()])
    _choose_modules.append([sg.Button('Voltar', button_color=('white','purple'))])
    return _choose_modules

# --------------------------------------------------------------------------------------------------------------------------#
def show_images(module, tags=None):
    def image_layout(module, tags=None):
        _images = [[]]
        products = mod.get_module(module).values()
        contador = 0
        for product in products:
            code, image, _, inventory = product.values()
            print(image)
            _images[floor(contador // 3)].append(
                                    sg.Column([
                                        [sg.Column([[sg.Image(resize(image,150,300))]], s=(150,240))],
                                        [sg.Checkbox(code), sg.Text(inventory)],
                                        ]))
            contador += 1
            if contador % 3 == 0:
                _images.append([])

        return _images if _images != [] else [[]]
    return image_layout(module, tags)


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
            [sg.Text(f'Adicione {module}:')],
            [sg.Text('Codigo:'), sg.Input(key="product_code")],
            [sg.Text('Foto:'), sg.FileBrowse(key="file_image")],
            [sg.Text('Estoque:'), sg.Input(key="product_inventory")],
            [sg.VPush()],
            [sg.Text('Atribua filtros a esse produto:')]]
        for group in tags.get_all_groups():
            if group in mod.get_tags(module):
                _adicionar_produtos[module].append([sg.Text(group.capitalize()+':')])
                for tag in tags.get_tag_group(group):
                    tag=tag[0]
                    _adicionar_produtos[module].append([sg.Text(s=2), sg.Checkbox(tag.replace('_', " ").capitalize(), key=f"checkbox_cadastro_{module}_{group}_{tag}")])
        _adicionar_produtos[module].append([sg.Button('Adicionar', key=("button_add_product", module))])
        
        _adicionar_produtos[module].append([Botao("Voltar", f"adicionar_produto_{module}", "modulos")])
        
    return _adicionar_produtos

# --------------------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    window = sg.Window("teste", [[sg.Column(show_images("roupas"), scrollable=True, vertical_scroll_only=True, s=(510,500))]], finalize=True)
    window.read()
    window.close()
