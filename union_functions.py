import PySimpleGUI as sg
from functions import swap_columns

def gerar_checkboxes(filtros, por_linha):
    checkboxes =[]

    for i in range(0, len(filtros), por_linha):
        linha = []

        for j in range(por_linha):
            linha.append(sg.Checkbox(filtros[i+j], s=(7,1), k='cb-filtro-{i=}-{j=}'))

        checkboxes.append(linha)

    return checkboxes


def popular(campo, com, como):
    for elemento in com:
        campo.append([como(elemento)])


trocar_tela = lambda window, x, y: swap_columns(window, x, y, 'col_central')
botao       = lambda   name, x, y: sg.Button(name, k=lambda window: trocar_tela(window, x, y))
