from cmath import inf
from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import messagebox

import tela_incial

c_pri = "#2d6375"
branco = "#D7E0D7"
c_sec = "#193842"
letra = "#403d3d"


def pagarEmprestimo(nConta, valor):
    valor = float(valor.get())
    user_list = []
    cur.execute(f'SELECT * FROM conta WHERE nConta = {nConta}')

    for x in cur:
        user_list.append(x)
    if user_list.__len__() == 1:
        valorEmprestimo = user_list[0][10]
        saldo = user_list[0][5]

        if valorEmprestimo == 0:
            messagebox.showwarning('', 'Não há valor a ser pago')
        else:
            valorEmprestimo = (valorEmprestimo - valor)
            saldo = (saldo - valor)
            cur.execute(
                f'UPDATE conta SET valorEmprestimo = {valorEmprestimo}, saldo = {saldo} WHERE nConta = {nConta}')
            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Pagamento de Emprestimo", {valor});')
            con_sqlite.commit()
            print('Emprestimo pago com sucesso')
            tela_incial.janelaEntrar(nConta)
    else:
        print('conta ou senha incorreta\nVerifique os dados e tente novamente')


def janelaPagarEmprestimo(nConta):

    janela8 = Tk()
    janela8.title("SGB ")
    janela8.geometry("300x300")
    janela8.configure(background="#feffff")
    janela8.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(
        janela8, width=300, height=50, relief='flat', bg='#feffff')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(
        janela8, width=300, height=250, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    cur.execute(f'SELECT * FROM conta WHERE nConta= {nConta}')
    # user_list = []
    info = cur.fetchall()

    texto = tkinter.Label(frame_cima, text=f"Olá, {info[0][1]}! ", anchor=NE, font=(
        'Ivy', 18), bg='#feffff', fg=c_pri)
    texto.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW,
                          width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
    linha.place(x=10, y=45)

    valorEmp = tkinter.Label(frame_baixo, text=f"Valor a pagar {info[0][10]} ", anchor=NE, font=(
        'Ivy', 18), bg='#feffff', fg=c_pri)
    valorEmp.place(x=5, y=5)

    texto = tkinter.Label(frame_baixo, text="Quanto vai pagar?", anchor=NE, font=(
        'Ivy', 15), bg='#feffff', fg=c_pri)
    texto.place(x=15, y=60)

    valor = Entry(frame_baixo, width=25)
    valor.place(x=70, y=95)

    btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=(
        'Ivy 8 bold'), relief=FLAT, command=lambda: [pagarEmprestimo(nConta, valor), janela8.destroy()])
    btnconfirmar.place(x=60, y=150)

    btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=(
        'Ivy 8 bold'), relief=FLAT, command=lambda: [tela_incial.janelaEntrar(nConta), janela8.destroy()])
    btnCancelar.place(x=151, y=150)
