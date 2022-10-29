from PySimpleGUI import Window, Button, Text, Image, Column, VerticalSeparator, Input
import PySimpleGUI as sg

def window_A():
    layout_esquerda=[
    [Text('Qual tipo de produto irá trabalhar?')],
    [Button('Roupas')],
    [Button('Outros')],
    ]

    layout_direita=[
        [Text('O foto shopping é um programa focado em ajudar o vendedor' "\n" 'no gerenciamento de suas vendas')]
    ]

    layout_central=[
    [Image(filename='logo.png')]
    ]
    layout=[
        [Column(layout_esquerda),
    VerticalSeparator(),
    Column(layout_central),
    VerticalSeparator(),
    Column(layout_direita)]
    ]
    return Window('Menu Principal', layout=layout)


def window_B():
    layout_esquerda=[
    [Text('Filtros:', size=(10,1)), ],
    [Text('Tamanho')],
    [sg.OptionMenu(
                [
                    '36',
                    '38',
                    '40',
                    '42',
                    '44',
                    '46',
                    '48',
                ],
                s=(15, 2),
                ),
    ],
    [Text('Modelo')],
    [sg.OptionMenu(
                [
                    'Blusa',
                    'Vestido',
                    'Macacão',
                    'Conjunto',
                    'Short',
                    'Saia',
                    'Calça',
                ],
                s=(15, 2),
                ),
    ],
    ]

    layout_direita=[
        [Text('O foto shopping é um programa focado em ajudar o vendedor' "\n" 'no gerenciamento de suas vendas')],
        [Button('Menu Principal')]
    ]

    layout_central=[
    [Image(filename='logo.png')]
    ]
    layout=[
        [Column(layout_esquerda),
    VerticalSeparator(),
    Column(layout_central),
    VerticalSeparator(),
    Column(layout_direita)]
    ]

    return Window('Menu Roupas', layout=layout)


def window_C():
    layout_esquerda=[
    [Text('Cadastre o tipo de produto')],
    [Text('Tipo:'), sg.Input(s=15)],
    ]

    layout_direita=[
        [Text('O foto shopping é um programa focado em ajudar o vendedor' "\n" 'no gerenciamento de suas vendas')],
        [Button('Menu Principal')]
    ]

    layout_central=[
    [Image(filename='logo.png')]
    ]
    layout=[
        [Column(layout_esquerda),
    VerticalSeparator(),
    Column(layout_central),
    VerticalSeparator(),
    Column(layout_direita)]
    ]
    return Window('Menu Cadastro', layout=layout)

window = window_A()

while True:
    event, values = window.read()
    match(event):
        case 'Roupas' | 'Outros' | 'Menu Principal':
            window.close()
            match (event):
                case 'Roupas':
                    window = window_B()
                case 'Outros':
                    window = window_C()
                case 'Menu Principal':
                    window = window_A()
        case None:
            break

window.close()