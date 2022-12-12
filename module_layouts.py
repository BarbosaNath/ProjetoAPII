import PySimpleGUI as sg
import modules as mod
import tags
from math import floor
from image_manipulation import resize
from functions import *

# Tema do Projeto
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
        [sg.Text('Qual tipo de produto irá trabalhar?')]
    ]

    for module in mod.get_all_modules():
        _choose_modules.append([sg.Button(module.capitalize(), k=tuple(("modulo_escolhido", module)), s=20), sg.Button("❌", s=(2,1), key=tuple(("modules_reset_screen", lambda: mod.remove_module(module))), button_color=("white", "darkred"))])

    # _choose_modules.append([sg.Sizer(v_pixels=300)])
    _choose_modules.append([sg.VPush()])
    _choose_modules.append([sg.Button('Cadastrar Modulo', button_color=('white', 'green'), s=17), sg.Button('Voltar', button_color=('white','purple'), s=5)])
    return _choose_modules

# --------------------------------------------------------------------------------------------------------------------------#
def show_images(module):
    _images = [[]]
    products = mod.get_module(module).values()
    contador = 0
    # _images[floor(contador // 3)].append(
    #                         sg.Frame(f"Adicionar {module.replace('_', ' ').capitalize()}",layout=[
    #                             [sg.VP()],
    #                             [sg.Column([[sg.P(),sg.Button("+", s=(5, 6), k=("ir_add_product", module), font="arial 30 bold", button_color=("grey","#f6fcff"), border_width=0), sg.P()]], s=(150,300))],
    #                             [sg.VP()],
    #                             ]))
    # contador += 1
    for product in products:
        code, image, _, inventory = product.values()
        print(image)
        _images[floor(contador // 3)].append(
                                sg.Column([
                                    [sg.Column([[sg.Image(resize(image,150,300))]], s=(150,240))],
                                    [sg.Checkbox(f"Codigo: {code}", key=f"checkbox_{code}"),sg.P(), sg.Button("❌", k=("deletar_produto_estoque", module, code), button_color=("white", "darkred"))],
                                    [sg.T(f"Em Estoque: {inventory}"), sg.P(), sg.Button("✏️", k=(f"editar_estoque", module, code))],
                                    ], k=f"image_{module}_{code}"))
        contador += 1
        if contador % 3 == 0:
            _images.append([])
    

    return _images if _images != [] else [[]]


# --------------------------------------------------------------------------------------------------------------------------#
def modules():
    _modules=dict()
    for module in mod.get_all_modules():
        _modules[module]=[
        gerar_botao_logout(f'modulo_{module}'),
        [sg.Push()],
        [sg.Text('Filtros:', size=(10,1))]]

        for group in tags.get_all_groups():
            if (group in mod.get_tags(module)):
                _modules[module] += [ 
                    [sg.Text("▸ " + group.replace('_', ' ').capitalize() + ":", s=10), sg.Combo(
                        [tag[0].replace('_', ' ').capitalize() for tag in tags.get_tag_group(group)],
                        s=10,
                        enable_events=True,
                        readonly=True,
                        k=f"combo_{module}_{group}"
                        ), sg.Button("❌", size=(1,2), font="arial 6", k=("remover_grupo_de_modulo", module, group), button_color=("white", "darkred"))] ]

        _modules[module] += [   
                                [sg.Sizer(v_pixels=25)],
                                [sg.Button("Pesquisar", key=tuple(("botao_pesquisar_module", module)), s=25)],
                                [sg.Button("Compartilhar Imagens Selecionadas", key=("botao_pegar_imagens", module), s=25)],
                                [sg.Sizer(v_pixels=25)],
                                [sg.Button("Adicionar Grupo de Filtros", key=("adicionar_grupo_a_modulo", module), button_color=("white", "green"),  s=25)],
                                [sg.Button(f'Adicionar {module.capitalize()}', key=tuple(("ir_add_product", module)), button_color=("white", "green"), s=17), sg.Button('Voltar',  key=tuple(("voltar_para_choose_modules", module)), s=5)],
                            ]
    return _modules

def popup_select_new_tag_group():
    layout = [
        [sg.Text("")],
        [sg.Combo(tags.get_all_groups(), size=(20,5), key='SELECTED', readonly=True)],
        [sg.Button('Adicionar', button_color=("white", "green")), sg.Button("Cancelar")],
    ]
    
    window = sg.Window('', layout).Finalize()
    
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        window.close()
        return
    elif event == 'Adicionar':
        window.close()
        return values['SELECTED']

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
        #[sg.Button('Cadastrar filtro')],
        [sg.VPush()],
        [sg.Button('Criar', key='submit_cadastro_modulo', button_color=('white', 'green'), s=17), sg.Button('Voltar', key='inicio', s=5)]
    ]
    return _cadastro_modulo  

# --------------------------------------------------------------------------------------------------------------------------#
def adicionar_produtos():
    _adicionar_produtos = dict()
    for module in mod.get_all_modules():
        _adicionar_produtos[module]=[
            gerar_botao_logout(f'adicionar_produto_{module}'),
            [sg.Text(f'Adicione {module}:')],
            [sg.Text('Codigo:' , s=6), sg.Input(key="product_code", s=16)],
            [sg.Text('Foto:'   , s=6), sg.FileBrowse("Imagem", key="file_image")],
            [sg.Text('Estoque:', s=6), sg.Input(key="product_inventory", s=16)],
            [sg.VPush()],
            [sg.Text('Atribua filtros a esse produto:')]]
        for group in tags.get_all_groups():
            if group in mod.get_tags(module):
                _adicionar_produtos[module].append([sg.Text(group.capitalize()+':')])
                for tag in tags.get_tag_group(group):
                    tag=tag[0]
                    _adicionar_produtos[module].append([sg.Text(s=2), sg.Checkbox(tag.replace('_', " ").capitalize(), key=f"checkbox_cadastro_{module}_{group}_{tag}")])
        _adicionar_produtos[module].append([sg.Button('Adicionar', key=tuple(("button_add_product", module)), s= 17), sg.Button("Voltar", key=tuple(("voltar_do_add_produtos", module)), s=5)])
        
    return _adicionar_produtos

# --------------------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    window = sg.Window("teste", [[sg.Column(show_images("roupas"), scrollable=True, vertical_scroll_only=True, s=(510,500))]], finalize=True)
    window.read()
    window.close()
