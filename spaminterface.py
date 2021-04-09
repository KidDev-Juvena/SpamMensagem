import pyautogui, pyperclip, string
from time import sleep
import PySimpleGUI as sg

def AcharArquivo():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('File Explorer:')],
        [sg.Input(), sg.FileBrowse('Browser')],
        [sg.Button('Ok'), sg.Button('Voltar')]
    ]
    return sg.Window('Browser', layout, finalize=True)
    


def janela_escolha():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Escolha o Ataque:')],
        [sg.Button('Mensagem'), sg.Button('Txt'), sg.Button('Transferencia'), sg.Button('Figurinha')]
    ]
    return sg.Window('Spammador', layout, finalize=True)

def janela_Mensagem():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Ataque Mensagem')],
        [sg.Text('Digite a mensagem no campo abaixo e clique em atacar.')],
        [sg.Text('Conteúdo do Spam:'), sg.Input(size=(20, 1)), sg.Text('Quantidade de Mensagens:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1), sg.Text('Tempo para Atacar:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1)],
        [sg.Button('Atacar'), sg.Button('Voltar')]
    ]
    return sg.Window('Ataque', layout, finalize=True)

def janela_Txt():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Ataque Txt')],
        [sg.Text('Bote a mensagem a ser enviada em um arquivo de texto.')],
        [sg.Text('Obs: Use o botão Achar Arquivo para e ecncontre o documento de texto.')],
        [sg.Text('Quantidade de Mensagens:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1), sg.Text('Tempo para Atacar:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1)],
        [sg.Button('Atacar'), sg.Button('Voltar'), sg.Button('Achar Arquivo', key=('file'))]
    ]
    return sg.Window('Ataque', layout, finalize=True)


def janela_Transferencia():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Ataque Transferencia')],
        [sg.Text('Copie a mensagem que vc quer enviar, aperte Atacar e clique na barra do chat.')],
        [sg.Text('Quantidade de Mensagens:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1), sg.Text('Tempo para Atacar:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1)],
        [sg.Button('Atacar'), sg.Button('Voltar')]
    ]
    return sg.Window('Ataque', layout, finalize=True)


def janela_Figurinha():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Ataque Figurinha')],
        [sg.Text('Deixe a aba de figurinha aberta clique em atacar e bote o mouse em cima da figurinha.')],
        [sg.Text('Quantidade de Mensagens:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1), sg.Text('Tempo para Atacar:'), sg.Spin([i for i in range(1,10000)], size=(6, 1), initial_value=1)],
        [sg.Button('Atacar'), sg.Button('Voltar')]
    ]
    return sg.Window('Ataque', layout, finalize=True)


def AtaqueMensagem():
    mensagem = str(valores[0])
    tamanho = int(valores[1])
    tempo = int(valores[2])

    pyperclip.copy(mensagem)

    sleep(tempo)
    for c in range(0, int(tamanho)): #Número de vezes que vai mandar
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')

def AtaqueTxt():
    arquivo = open(diretorio2)
    conteudo = arquivo.read()
    pyperclip.copy(conteudo)
    arquivo.close()

    tamanho = int(valores[0])
    tempo = int(valores[1])

    sleep(tempo)
    for c in range(0, int(tamanho)): #Número de vezes que vai mandar
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')

def AtaqueTranferencia():
    tamanho = int(valores[0])
    tempo = int(valores[1])

    sleep(tempo)
    for c in range(0, int(tamanho)): #Número de vezes que vai mandar
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')

def AtaqueFigurinha():
    tamanho = int(valores[0])
    tempo = int(valores[1])

    sleep(tempo)
    figurinha = pyautogui.position()

    for c in range(0, tamanho): #Número de vezes que vai mandar                                                                                                                                                                                                                                                                                                                                                                                                                                        0): #Número de vezes que vai mandar
        pyautogui.click(figurinha[0], figurinha[1])

janela1, janela2, janela3, janela4, janela5, janela6 = janela_escolha(), None, None, None, None, None

while True:
    window,evento,valores = sg.read_all_windows()
    
    if window == janela1 and evento == sg.WIN_CLOSED:
        break

    if window == janela2 and evento == sg.WIN_CLOSED:
        break

    if window == janela3 and evento == sg.WIN_CLOSED:
        break

    if window == janela4 and evento == sg.WIN_CLOSED:
        break

    if window == janela5 and evento == sg.WIN_CLOSED:
        break

    if window == janela6 and evento == sg.WIN_CLOSED:
        break

    if window == janela1 and evento == 'Mensagem':
        janela2 = janela_Mensagem()
        janela1.hide()

    if window == janela1 and evento == 'Txt':
        janela3 = janela_Txt()
        janela1.hide()

    if window == janela1 and evento == 'Transferencia':
        janela4 = janela_Transferencia()
        janela1.hide()

    if window == janela1 and evento == 'Figurinha':
        janela5 = janela_Figurinha()
        janela1.hide()

    if window == janela3 and evento == 'file':
        janela6 = AcharArquivo()
        janela3.hide()
    
    if window == janela2 and evento == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela3 and evento == 'Voltar':
        janela3.hide()
        janela1.un_hide()

    if window == janela4 and evento == 'Voltar':
        janela4.hide()
        janela1.un_hide()

    if window == janela5 and evento == 'Voltar':
        janela5.hide()
        janela1.un_hide()

    if window == janela6 and evento == 'Voltar':
        janela6.hide()
        janela3.un_hide()

    if window == janela6 and evento == 'Ok':
        diretorio = valores[0]
        janela6.hide()
        janela3.un_hide()
        print(valores[0])

    if window == janela2 and evento == 'Atacar':
        janela2.hide()
        janela1.un_hide()
        sg.popup('Clique em Ok para começar a contagem.')
        AtaqueMensagem()

    if window == janela3 and evento == 'Atacar':
        diretorio2 = diretorio
        janela3.hide()
        janela1.un_hide()
        sg.popup('Clique em Ok para começar a contagem.')
        AtaqueTxt()

    if window == janela4 and evento == 'Atacar':
        janela4.hide()
        janela1.un_hide()
        sg.popup('Clique em Ok para começar a contagem.')
        AtaqueTranferencia()

    if window == janela5 and evento == 'Atacar':
        janela5.hide()
        janela1.un_hide()
        sg.popup('Clique em Ok para começar a contagem.')
        AtaqueFigurinha()