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

c_pri = "#2d6375"
branco = "#D7E0D7"

preta = "#f0f3f5"
verde = "#3fb5a3"
letra = "#403d3d"
valor = "#38576b"
azul = "#00008e"
c_sec = "#193842"


def janelaPrincipal():
    janela = Tk()
    janela.geometry("300x240")
    janela.eval('tk::PlaceWindow . center')
    janela.configure(background="#feffff")
    janela.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(janela, width=300, height=50, relief='flat', bg=c_pri)
    frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela, width=300, height=190, relief='flat', bg=c_pri)
    frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    janela.title("Sistema Bancário")

    texto = tkinter.Label(frame_cima, text="Bem Vindo", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
    texto.place(x=5, y =5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
    linha.place(x=10, y =45)

    btn = tkinter.Button(frame_baixo, text="Fazer login", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda:[janelaLogin(), janela.destroy()] )
    btn.place(x=8, y =70)

    btnCadastro = tkinter.Button(frame_baixo, text="Cadastrar-se", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda:[janelaCadastrar(), janela.destroy()])
    btnCadastro.place(x=8, y =120)
    
    # fechando a janela principal
    mainloop()


janelaPrincipal()