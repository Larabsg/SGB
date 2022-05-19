from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *

def extrato(nConta):
        user_list = []
        extrato = []
        # nconta = 1234
        cur.execute(f'select tipo, valor from transacao where nconta = {nConta}')

        for x in cur:
            extrato.append(x)
        return extrato

def janelaExtrato(janela, nConta):

        text_extrato = extrato(nConta)
        # lembrar de verificar qual o tipo de conta
        janela6 = Toplevel(janela)
        janela6.title("SGB ")
        janela6.geometry("300x240")
        
        texto = Label(janela6, text=" Extrato ")
        texto.place(x=70, y=20)

        index = 40
        for e in range(len(text_extrato)):
            # print(text_extrato[e])
            lista = Label(janela6, text=f'{text_extrato[e]}\n')
            lista.place(x=70, y=index)
            index+=20