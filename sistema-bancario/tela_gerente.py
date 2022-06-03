#criar contas, visualizar contas da agencia, fazer emprestimos

from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *
from tkinter import *
from tkinter.ttk import *
import tkinter
from tela_cadastro import janelaCadastrar
from Gerente import Gerente

c_pri = "#2d6375"
branco = "#D7E0D7"
letra = "#403d3d"
c_sec = "#193842"


def janelaEntrarGerente(nConta=1234):
    
    gerente = Gerente("lara", "12345678", "gerente", 1200, "12345")
    janela2 = Tk()
    janela2.geometry("310x300")

    frame_cima = tkinter.Frame(janela2, width=310, height=50, relief='flat', bg=c_pri)
    frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela2, width=310, height=250, relief='flat', bg=c_pri)
    frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    cur.execute(f'select nome, saldo from funcionario where nConta = {nConta}')
    info = cur.fetchall()

    texto = tkinter.Label(frame_cima, text=f"Olá, {info[0][0]}! ", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
    texto.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
    linha.place(x=10, y =45)

    btnSacar = tkinter.Button(frame_baixo, text="Criar nova conta", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=gerente.criaConta)
    btnSacar.place(x=10, y=90)

    btnDepositar = tkinter.Button(frame_baixo, text="Visualizar contas", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=gerente.getContas)
    btnDepositar.place(x=10, y=140)

    btnExtrato = tkinter.Button(frame_baixo, text="Realizar empréstimo", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=gerente.realizaEmprestimo)
    btnExtrato.place(x=10, y=190)
#     mainloop()

# janelaEntrarGerente()
