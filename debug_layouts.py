import PySimpleGUI as sg
import database.database as db
# Main ---------------------------------------------------------------------------------------
# X-------------------------X
# | [Mostrar DB] [Cancelar] |
# X-------------------------X
main = [[sg.Button("Mostrar DB", key=lambda window: swap_columns(window, "col-main", "col-show"), border_width=0, size=(7, 1)), sg.Button("Cancelar", key="cancel", border_width=0, size=(7, 1))]]

# Show DataBase ------------------------------------------------------------------------------
# X--------------------X
# | text text ... text |
# | text text ... text |
# | ...  ...  ... ...  |
# | text text ... text |
# X--------------------X
show = []
def update_show():
    global show
    show = []
    
    for e in db.list_table("database/test.db", "usuario"):
        show.append([])
        for i in e:
            show[len(show)-1].append(sg.Text(f"{i}", size=(7, 1)))
            
    show.append([ sg.Button("Voltar",    key=lambda window: swap_columns(window, "col-show", "col-main"), border_width=0, size=(7, 1)),
                  sg.Button("Atualizar", key=lambda _:update_show(), border_width=0, size=(7, 1))
    ])

update_show()


def swap_columns(window, column1, column2):
    window[column1].update(visible= False)
    window[column2].update(visible= True)

