from cgitb import text
from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
import tkinter
from tkinter.ttk import *

c_pri = "#2d6375"
branco = "#D7E0D7"
letra = "#403d3d"
c_sec = "#193842"

def janelaVisualizarFuncionarios(funcionarios):

        #text_extrato = extrato(nConta)
        # lembrar de verificar qual o tipo de conta
        janela = Tk()
        janela.geometry("310x300")

        frame_cima = tkinter.Frame(janela, width=310, height=50, relief='flat', bg=c_pri)
        frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
        frame_baixo = tkinter.Frame(janela, width=310, height=250, relief='flat', bg=c_pri)
        frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)
        
        texto = tkinter.Label(frame_cima, text="FUNCIONÁRIOS", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
        texto.place(x=5, y=5)

        linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
        linha.place(x=10, y =45)

        index = 40
        txt = tkinter.Label(frame_baixo, text='NOME \t| MATRÍCULA |\t AGÊNCIA', font=('Ivy 10 bold'), bg=c_pri, fg=branco)
        txt.place(x=15, y=10)
        for e in range(len(funcionarios)):
            lista = tkinter.Label(frame_baixo, text=f'{funcionarios[e][1]} \t| {funcionarios[e][2]} \t| {funcionarios[e][5]}\n', font=('Ivy 10 bold'), bg=c_pri, fg=branco)
            lista.place(x=10, y=index)
            index+=20