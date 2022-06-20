import PySimpleGUI as sg

sg.theme('DarkPurple6')


layout = [ 
    [sg.Text('Por favor, coloque suas informações:', text_color='white', size=50, font='Gotham')],
    [sg.Text('Nome', text_color='white', size=12, font='Gotham'), sg.InputText(key='nome')],
    [sg.Text('Nacionalidade', text_color='white', size=12, font='Gotham'), sg.InputText(key='nacionalidade')],
    [sg.Text('Idade', text_color='white', size=12, font='Gotham'), sg.InputText(key='idade')],

    [sg.Button('Ok', button_color='green', size=2, font='Gotham'), sg.Button('Cancel', button_color='red', size=12, font='Gotham')]
]

window = sg.Window("Logart", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        f = open("pessoas.txt", 'w')

        name = values['nome']
        nacionality = values['nacionalidade']
        idade = values['idade']

        with open('pessoas.txt', 'w') as f:
            f.write(name)







window.close()