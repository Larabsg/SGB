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
import tela_pagarEmprestimo
# import teste

from ContaPoupanca import ContaPoupanca

c_pri = "#2d6375"
branco = "#D7E0D7"

preta = "#f0f3f5"
verde = "#3fb5a3"
letra = "#403d3d"
valor = "#38576b"
azul = "#00008e"
c_sec = "#193842"


def janelaEntrar(nConta):

    janela2 = Tk()
    #janela2.title(f"Bem Vindo, {info[0][0]}! ")
    janela2.geometry("310x340")

    frame_cima = tkinter.Frame(
        janela2, width=310, height=50, relief='flat', bg=c_pri)
    frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(
        janela2, width=310, height=290, relief='flat', bg=c_pri)
    frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    # c = ContaPoupanca('0','0','0','0','0','0','0','0')
        
    # c.atualizarSaldo()
    # teste.job()
        

    cur.execute(
        f'select nome, saldo, tipoConta, temEmprestimo from conta where nConta = {nConta}')
    info = cur.fetchall()

    texto = tkinter.Label(frame_cima, text=f"Olá, {info[0][0]}! ", anchor=NE, font=(
        'Ivy', 18), bg=c_pri, fg=branco)
    texto.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW,
                          width=275, font=('Ivy 1'), bg=branco, fg=letra)
    linha.place(x=10, y=45)

    texto_saldo = tkinter.Label(
        frame_baixo, text=f"Saldo: {info[0][1]}", font=('Ivy 18'), bg=c_pri, fg=branco)
    texto_saldo.place(x=10, y=20)

    btnSacar = tkinter.Button(frame_baixo, text="Sacar", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda: [tela_sacar.janelaSacar(nConta),janela2.destroy()])
    btnSacar.place(x=10, y=90)

    btnDepositar = tkinter.Button(frame_baixo, text="Depositar", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda:[tela_depositar.janelaDepositar(nConta), janela2.destroy()])
    btnDepositar.place(x=10, y=140)

    btnExtrato = tkinter.Button(frame_baixo, text="Extrato", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(
        tela_extrato.janelaExtrato, nConta))
    btnExtrato.place(x=10, y=190)

    if info[0][3] == True:
        btnEmprestimo = tkinter.Button(frame_baixo, text="Empréstimo", width=39, height=2, bg=c_sec, fg=branco, font=(
            'Ivy 8 bold'), relief=FLAT, command=lambda:[tela_pagarEmprestimo.janelaPagarEmprestimo(nConta), janela2.destroy()])
        btnEmprestimo.place(x=10, y=240)

    
    
    