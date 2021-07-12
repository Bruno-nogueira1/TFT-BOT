import pyautogui as gui
from python_imagesearch.imagesearch import imagesearch as search
from time import sleep
import tkinter as tk

gui.FAILSAFE = True


#Verifica se há aquela imagem na tela, retornando sua posição.
def tela(image,precision = 0.8):
    pos = search(image,precision)
    if pos[0] != -1:
        return pos
    

#Move o cursor até a posição da imagem e dá um clique com o botão esquerdo
def clique(image):
    x = tela(image)
    gui.moveTo(x)
    sleep(0.15)
    gui.mouseDown()
    sleep(0.15)
    gui.mouseUp()

#Inicia a busca de partida
def encontrarpartida():
    if tela('encontrarpartida.png'):
        clique('encontrarpartida.png')


#Aceita a partida
def aceitar():
    if tela('Aceitar.png'):
        clique('Aceitar.png')


#Após as rodadas listadas, irá comprar xp automaticamente até o fim da partida
def xp():
    if tela('Xp.png'):
        clique('Xp.png')


champs = ['aatrox.png','gragas.png','kalista.png','khazix.png','kled.png','leona.png','lissandra.png',
'poppy.png','udyr.png','vayne.png','vladmir.png','warwick.png','ziggs.png']

#Nas rodadas iniciais, irá comprar os campeões selecionados assim que aparecerem
def compra():
    for c in champs:
        if tela(c):
            clique(c)


#Após o player ser derrotado, irá sair automaticamente da partida
def sairdapartida():
    if tela('sairpartida.png'):
        clique('sairpartida.png')


#Clica em jogar novamente
def jogarnovamente():
    if tela('jogarnovamente.png'):
        clique('jogarnovamente.png')

#Caso alguma missão seja concluída, ele aceita a missão e continua o loop
def missao():
    if tela('ok.png'):
        clique('ok.png')

#Pula a espera por estatísticas
def estatisticas():
    if tela('estatisticas.png'):
        clique('estatisticas.png')

#Programa principal
def principal():
    while True:
        ok1 = True
        ok = True
        while not tela('nafila.png'):
            encontrarpartida()
        while not tela('1-1.png'):
            if tela('Aceitar.png'):
                clique('Aceitar.png')
        while not tela('3-1.png'):
            compra()
        while ok:
            xp()
            if tela('sairpartida.png'):
                clique('sairpartida.png')
                ok = False
            if tela('continuar.png'):
                clique('continuar.png')
                ok = False
        while not tela('tft logo.png'):
            estatisticas()
            missao()
            jogarnovamente()