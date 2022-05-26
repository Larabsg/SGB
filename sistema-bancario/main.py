from ctypes.wintypes import DOUBLE
from functools import partial
import tkinter
from tokenize import Double
from turtle import bgcolor
from connection_sqlite import *

from tkinter import *
import tkinter.font as tk_font
from tkinter.ttk import *
from tela_login import janelaLogin
from tela_cadastro import janelaCadastrar

laranja = "#ff4000"
branco = "#feffff"

preta = "#f0f3f5"
verde = "#3fb5a3"
letra = "#403d3d"
valor = "#38576b"

def janelaPrincipal():
    janela = Tk()
    janela.geometry("300x240")
    janela.configure(background="#feffff")
    janela.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(janela, width=300, height=50, relief='flat', bg='#feffff')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela, width=300, height=190, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    janela.title("Sistema Bancário")

    texto = tkinter.Label(frame_cima, text="Bem Vindo!", anchor=NE, font=('Ivy', 20), bg=branco, fg=letra)
    texto.place(x=5, y =5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=verde, fg=letra)
    linha.place(x=10, y =45)

    btn = tkinter.Button(frame_baixo, text="Fazer login", width=39, height=2, bg=verde, fg=branco, font=('Ivy 8 bold'), relief=RAISED, command=partial(janelaLogin, janela))
    btn.place(x=8, y =70)

    btnCadastro = tkinter.Button(frame_baixo, text="Cadastrar-se", width=39, height=2, bg=verde, fg=branco, font=('Ivy 8 bold'), relief=RAISED, command=partial(janelaCadastrar, janela))
    btnCadastro.place(x=8, y =120)
    
    # fechando a janela principal
    mainloop()


janelaPrincipal()
