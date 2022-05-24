import PySimpleGUI as sg
lay = [[sg.Button(f'{n}')] for n in range(1, 8)]

window = sg.Window('NEW', lay)
while True:  # Event Loop
    event, values = window.Read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == '1':
        la= [[sg.Text(f'{n}'), sg.In(key=f'{n}')] for n in range(1, 8)
             ],[sg.Button('but')]

        window=sg.Window('second',la)

        while True:
            event, values = window.read(timeout=100)
            if event == "Exit" or event == sg.WIN_CLOSED:
                while True:
                    break
            if event =='but':
                print(values)
        window.close()
    if event == '2':
        pass
    if event == '3':
        pass
    if event == '4':
        pass
    if event == '5':
        pass
    if event == '6':
        layout = [[sg.Text("New Window", key="new")]]
        window = sg.Window("Second Window", layout, modal=True)
        choice = None
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
        window.close()
    if event == '7':
        window=sg.Window('NEW', [[sg.OK(), sg.Cancel()]])
        while True:
            event, values = window.read()
            if event == "Cancel" or event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
        window.close()
window.Close()