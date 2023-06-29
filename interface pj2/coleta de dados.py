import PySimpleGUI as sg



class Telapy:
    def __init__(self):
        # Layout
        Layout = [
            [sg.Text('Usuario'),sg.Input(key='Usuario')],
            [sg.Text('Senha'),sg.Input(key='Senha', password_char='*')],
            [sg.Button('Entrar')]
        ]
        
        # Janela
        Janela = sg.Window("Dados do Usuario").Layout(Layout)
        # Extrair dados da tela
        eventos, valores = Janela.Read()

        if eventos == sg.WINDOW_CLOSED:
            breakpoint
        if eventos == 'Entrar':
            if valores ['Usuario'] == 'usuario' and ['Senha'] == 'senha':
                print('Carregando')



