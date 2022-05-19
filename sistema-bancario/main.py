from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
from tela_login import janelaLogin
from tela_cadastro import janelaCadastrar
from tela_incial import janelaEntrar

def janelaPrincipal():
    janela = Tk()
    janela.geometry("300x240")

    janela.title("Sistema Bancário")

    texto = Label(janela, text=" Bem Vindo! ")
    texto.place(x=100, y =10)

    btn = Button(janela, text="Fazer login", command=partial(janelaLogin, janela))
    btn.place(x=40, y =150)

    btnCadastro = Button(janela, text="Cadastrar-se", command=partial(janelaCadastrar, janela))
    btnCadastro.place(x=150, y =150)
    
    # fechando a janela principal
    mainloop()


janelaPrincipal()
