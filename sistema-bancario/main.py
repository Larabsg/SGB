from ctypes.wintypes import DOUBLE
from functools import partial
from tkinter import font
from tokenize import Double
from turtle import position
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
from tela_login import janelaLogin
from tela_cadastro import janelaCadastrar

def janelaPrincipal():
    janela = Tk()
    janela.geometry("300x240")
    janela.configure(background='#DCDFE5')
    
    janela.title("Sistema Bancário" )

    texto = Label(janela, text=" Bem Vindo! ")
    # texto.configure(font=("Courier", 20))
    texto.place(x=100, y =10)

    btn = Button(janela, text="Fazer login", command=partial(janelaLogin, janela))
    btn.place(x=40, y =150)

    btnCadastro = Button(janela, text="Cadastrar-se", command=partial(janelaCadastrar, janela))
    btnCadastro.place(x=150, y =150)
    
    # fechando a janela principal
    mainloop()


janelaPrincipal()
