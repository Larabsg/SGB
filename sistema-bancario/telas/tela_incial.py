from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
#import conta
#from entidades import conta
#from connection import *
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
from interface_grafica import *
from interface_grafica import janela
from tela_sacar import *
from tela_depositar import *
from tela_extrato import *

def janelaEntrar(nConta):

        #nConta = int(nConta.get())
        cur.execute(f'select nome, saldo from conta where nConta = {nConta}')
        info = cur.fetchall()
        print(info)
        janela2 = Toplevel(janela)
        janela2.title(f"Bem Vindo, {info[0][0]}! ")
        janela2.geometry("300x240")

        texto = Label(janela2, text=f"Bem Vindo, {info[0][0]}! ")
        texto.place(x=70, y=20)

        texto_saldo = Label(janela2, text=f"Saldo = {info[0][1]}")
        texto_saldo.place(x=70, y=40)

        btnSacar = Button(janela2, text="Sacar", command=janelaSacar)
        btnSacar.place(x=100, y=100)

        btnDepositar = Button(janela2, text="Depositar", command=janelaDepositar)
        btnDepositar.place(x=50, y=150)
        
        btnExtrato = Button(janela2, text="Extrato", command=janelaExtrato)
        btnExtrato.place(x=160, y=150)