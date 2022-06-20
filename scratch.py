import PySimpleGUI as sg

sg.theme('DarkPurple6')


layout = [ 
    [sg.Text("Texto 1")],
    [sg.Text("Senha"), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window("Logart", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()