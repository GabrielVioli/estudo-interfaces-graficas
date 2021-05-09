import PySimpleGUI as sg
import time
from pynput import keyboard

sg.theme('Light Blue 3')
layout = [
    [sg.Text('Nome Completo')],
    [sg.Input(key = 'complete_name')],
    [sg.Text('Idade')],
    [sg.Input(key = 'age')],
    [sg.Text('Gênero', size = (20,2))],
    [sg.Radio('feminino', 'gene', key = 'gender1')],[sg.Radio('masculino','gene',key = 'gender2')],
    [sg.Text('Recomendações', size = (20,1))],
    [sg.Radio('sim', 'recomend', key = 'yes')],[sg.Radio('não', 'recomend', key = 'no')],
    [sg.Button('enviar informações', size = (9,2))],
]

window = sg.Window('Apresentação', layout, size = (400,400)) 
while True:    
    event, values = window.read() 
    if event is None:
        break

    if event == 'enviar informações':
        complete_name = values['complete_name']
        gender1 = values['gender1']
        gender2 = values['gender2']
        age = values['age']
        recomend_yes = values['yes']
        recomend_no = values['no']
    
    if gender1 == True:
        values['gender1'] = False

    if gender2 == True:
        values['gender2'] = False
        

    window.close()

    sg.theme('Light Blue 3')
        
    layout2 = [
        [sg.Text(f'seja bem vindo {complete_name}', size = (30,1))],
        [sg.Text('filename')],
        [sg.Input(key = 'filename'), sg.FileBrowse(key = 'file', size = (8,1))],
        [sg.OK()],
        [sg.Cancel()]
    ]

    window2 = sg.Window('Apresentação', layout2, size  = (450,400))

    while True:    
        event2, values = window2.read()

        filename = values['filename']
        file = values['file']

        if event2 is None or event2 == 'Cancel':
            break

        if event2 == 'OK':
            break

if event2 == 'OK':
    op = open(filename, 'r')
    t = op.read()
    print(t)
    op.close() 

window2.close()

sg.theme('Light Blue 3')
        
layout2 = [
    [sg.Text(f'seja bem vindo {complete_name}', size = (30,1))],
    [sg.Text('filename')],
    [sg.Input(key = 'filename'), sg.FileBrowse(key = 'file', size = (8,1))],
    [sg.OK()],
    [sg.Cancel()]
]

window2 = sg.Window('Apresentação', layout2, size  = (450,400))

while True:    
    event2, values = window2.read()

    filename = values['filename']
    file = values['file']

    if event2 is None or event2 == 'Cancel':
            break

    if event2 == 'OK':
            break








