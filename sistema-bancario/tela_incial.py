from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *
from tkinter import *
from tkinter.ttk import *
import tela_sacar
import tela_depositar
import tela_extrato

from Conta import Conta

def janelaEntrar(janela, nConta):

        cur.execute(f'select nome, saldo from conta where nConta = {nConta}')
        info = cur.fetchall()
        janela2 = Toplevel(janela)
        janela2.title(f"Bem Vindo, {info[0][0]}! ")
        janela2.geometry("300x240")

        texto = Label(janela2, text=f"Bem Vindo, {info[0][0]}! ")
        texto.place(x=70, y=20)

        texto_saldo = Label(janela2, text=f"Saldo = {info[0][1]}")
        texto_saldo.place(x=70, y=40)

        btnSacar = Button(janela2, text="Sacar", command=partial(tela_sacar.janelaSacar, janela, nConta))
        btnSacar.place(x=100, y=100)

        btnDepositar = Button(janela2, text="Depositar", command=partial(tela_depositar.janelaDepositar, janela, nConta))
        btnDepositar.place(x=50, y=150)
        
        btnExtrato = Button(janela2, text="Extrato", command=partial(tela_extrato.janelaExtrato, janela, nConta))
        btnExtrato.place(x=160, y=150)
