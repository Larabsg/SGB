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

def extrato(nConta):
        user_list = []
        extrato = []
        cur.execute(f'select tipo, valor from transacao where nconta = {nConta}')

        for x in cur:
            extrato.append(x)
        return extrato

def janelaExtrato(nConta):

        text_extrato = extrato(nConta)
        # lembrar de verificar qual o tipo de conta
        janela6 = Tk()
        janela6.geometry("310x300")

        frame_cima = tkinter.Frame(janela6, width=310, height=50, relief='flat', bg=c_pri)
        frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
        frame_baixo = tkinter.Frame(janela6, width=310, height=250, relief='flat', bg=c_pri)
        frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)
        
        texto = tkinter.Label(frame_cima, text="EXTRATO", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
        texto.place(x=5, y=5)

        linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
        linha.place(x=10, y =45)

        index = 40
        for e in range(len(text_extrato)):
            lista = tkinter.Label(frame_baixo, text=f'{text_extrato[e][0]} .............................................. {text_extrato[e][1]}\n', font=('Ivy 10 bold'), bg=c_pri, fg=branco)
            lista.place(x=10, y=index)
            index+=20