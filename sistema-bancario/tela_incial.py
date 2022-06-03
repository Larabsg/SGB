from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *
from tkinter import *
from tkinter.ttk import *
import tkinter
import tela_sacar
import tela_depositar
import tela_extrato

c_pri = "#2d6375"
branco = "#D7E0D7"

preta = "#f0f3f5"
verde = "#3fb5a3"
letra = "#403d3d"
valor = "#38576b"
azul = "#00008e"
c_sec = "#193842"


def janelaEntrar(janela, nConta):
    
    janela2 = Toplevel(janela)
    #janela2.title(f"Bem Vindo, {info[0][0]}! ")
    janela2.geometry("310x300")

    frame_cima = tkinter.Frame(janela2, width=310, height=50, relief='flat', bg=c_pri)
    frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela2, width=310, height=250, relief='flat', bg=c_pri)
    frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    cur.execute(f'select nome, saldo from conta where nConta = {nConta}')
    info = cur.fetchall()

    texto = tkinter.Label(frame_cima, text=f"Olá, {info[0][0]}! ", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
    texto.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
    linha.place(x=10, y =45)

    texto_saldo = tkinter.Label(frame_baixo, text=f"Saldo: {info[0][1]}", font=('Ivy 18'), bg=c_pri, fg=branco)
    texto_saldo.place(x=10, y=20)

    btnSacar = tkinter.Button(frame_baixo, text="Sacar", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(
        tela_sacar.janelaSacar, janela, nConta))
    btnSacar.place(x=10, y=90)

    btnDepositar = tkinter.Button(frame_baixo, text="Depositar", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(
        tela_depositar.janelaDepositar, janela, nConta))
    btnDepositar.place(x=10, y=140)

    btnExtrato = tkinter.Button(frame_baixo, text="Extrato", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(
        tela_extrato.janelaExtrato, janela, nConta))
    btnExtrato.place(x=10, y=190)