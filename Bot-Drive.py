# Importando Bibliotecas
import selenium

import time

import webdriver_manager

import PySimpleGUI as Pysg

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from time import sleep

# Olá Mundo para dar tudo certo \(•ω• \)
print("Olá Mundo")

def Comecar():

    data01 = str(atualizar['Data01'])
    data02 = str(atualizar['Data02'])

    driver = webdriver.Chrome(ChromeDriverManager().install())  

    driver.get('https://docs.google.com/document/d/1AD_09SmLzTRvJ-6kWg1kTs_0BNyt0bmWv4yONgO9vrs/edit?usp=sharing')

    time.sleep(20) 

    Find_Data = driver.find_elements_by_link_text(data01)

    Find_Data.click()
    Find_Data.click()
    Find_Data.click()


Pysg.theme('LightBlue')
tela = [
    # Texto Inicial
    [Pysg.Text('Bot-Canva', font=('Bold'))], 
    [Pysg.Text('Bem-vindo de volta!', text_color='blue')],
    # Aviso De Formatação 
    [Pysg.Text('Por Favor Colocar a data separada por "/" : ("01/01/2020")', text_color ='red', size=(25,2))],
    # Campos de Input
    [Pysg.Text("Data 1: "), Pysg.Input(size=(38,20), key ='Data01')],
    [Pysg.Text("Data 2: "), Pysg.Input(size=(38,20), key ='Data02')],
    # Começa a Automação com Selenium
    [Pysg.Button('Começar', size = (40,1))]
    ]

# Definir a Janela
janela = Pysg.Window( 'Auto-Bot', tela )

# Loop de Janela
while True:
    desenhar, atualizar = janela.read()

    if desenhar == Pysg.WINDOW_CLOSED or desenhar == 'Quit':
        break

    if desenhar == 'Começar':
        Comecar()
        
# Olá Mundo Concluido com Sucesso
Ola_Mundo = True
if Ola_Mundo == True:
    print (" Obrigado ;) ")

