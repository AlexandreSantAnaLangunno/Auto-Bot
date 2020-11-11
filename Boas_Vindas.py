
# Ola Mundo Para Dar Certo \( * ^0^ * )/

olamundo = {print ("Olá Mundo! "), True}
# Importando Bibliotecas

import os

import PySimpleGUI as Pysg
   
    ## Essas Será as Bibliotecas


# Criar Tela

    ## Funções Iniciais para Uma Tela

        ### Definir Requisitos da Tela
    
    #### Descobri que pode colocar temas =)

Pysg.theme('LightBlue') 
    ##### coloquei o 'Azul Claro' PorQue Combina com o 'Canva'

requisito = [ [ Pysg.Text("Auto-Bot" ) ],
    
              [ Pysg.Text("Olá Ben-Vindo de Volta " )  ],
              
              [Pysg.Text( " Obs. Colocar o Ano Abreviado: ' xx/xx/yy ' ", text_color = 'red') ],

              [ Pysg.Text('Data 1: ') ], [ Pysg.Input(key='-INPUT-', size = ( 8, 4 )) ],      
              
              [ Pysg.Text('Data 2: ') ], [ Pysg.Input(key='-INPUT-', size = ( 8, 4 )) ],
              
              [ Pysg.Button( 'Começar ' ) ] ]             
       
### Definir Função ("Desenhar e Atualizar")
                    
                    # Titulo   
janela = Pysg.Window('Auto-Bot', requisito)

        ### Chamar as Funções ("Desenhar e Atualizar")
while True:
    
    desenhar, atualizar = janela.read()
    
    if desenhar == Pysg.WINDOW_CLOSED or desenhar == 'Quit':
        break
    
    



    # Definir o Botão ("Começar")

        ## O Arquivo que ele ira Abrir \\ ( "Bot-Drive" )



























## Olá Mundo Concluido
if olamundo == ( True ):
    print ("Olá Mundo Concluido")

    ### Fim do Olá Mundo 
