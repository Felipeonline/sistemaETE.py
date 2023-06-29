import PySimpleGUI as sg

class Telapy:
    def __init__(self):
        # Layout
        Layout = [
            [sg.Text('Bem Vindo ao sistema ETE (sistema online de Estação de tratamento de Efluentes)')]
            [sg.Button('Entrar')]
        ]
        # Janela
        Janela = sg.Window("Botao de entrada ").Layoud(Layout)
        
        self.button= Janela.Read()
