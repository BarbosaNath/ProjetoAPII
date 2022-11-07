import PySimpleGUI as sg
import database.database as db
# Main ---------------------------------------------------------------------------------------
# X-------------------------X
# | [Mostrar DB] [Cancelar] |
# X-------------------------X
main = [[sg.Button("Mostrar DB", key='show_db', border_width=0, size=(7, 1)), sg.Button("Cancelar", key="cancel", border_width=0, size=(7, 1))]]
show = []
def update_show():
    global show
    
    for e in db.list_table("database/test.db", "usuario"):
        show.append([])
        for i in e:
            show[len(show)-1].append(sg.Text(f"{i}", size=(7, 1)))
            
    show.append([
            sg.Button("Voltar", key='back', border_width=0, size=(7, 1)),
            sg.Button("Atualizar", key='update', border_width=0, size=(7, 1))
    ])

update_show()