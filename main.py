import PySimpleGUI as sg
import time

sg.theme('DarkPurple6')


layout = [ 
    [sg.Text('Por favor, coloque suas informações:', text_color='white', size=50, font='Gotham')],
    [sg.Text('Nome', text_color='white', size=12, font='Gotham'), sg.InputText(key='nome',  do_not_clear=False)],
    [sg.Text('Nacionalidade', text_color='white', size=12, font='Gotham'), sg.InputText(key='nacionalidade', do_not_clear=False)],
    [sg.Text('Idade', text_color='white', size=12, font='Gotham'), sg.InputText(key='idade', font='Gotham', do_not_clear=False)],
    [sg.Text('', key='error_message')],
    [sg.Button('Ok', button_color='green', size=2, font='Gotham', ), sg.Button('Cancel', button_color='red', size=12, font='Gotham')]
]

window = sg.Window("Logart", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        
        name = values['nome']
        nacionality = values['nacionalidade']
        idade = values['idade']



        if name == '':
             window['error_message'].update('Entrada Vazia')
             time.sleep(0.5)
             window['error_message'].update('')

            






window.close()