from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
import tkinter
from tkinter.ttk import *

c_pri = "#2d6375"
branco = "#D7E0D7"
c_sec = "#193842"

def depositar(valor, nConta):
        valor = float(valor.get())
        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)
        if user_list.__len__() == 1:
            saldo = user_list[0][5]
            if(saldo < 0):
                taxa = ((saldo*0.10)*-1)
                saldo = (saldo+valor)-taxa
                cur.execute(f'UPDATE conta SET saldo = {saldo} WHERE nConta = {nConta}')
                cur.execute(f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Depósito", {valor});')
                con_sqlite.commit()
                print('Depósito efetuado com sucesso')
            else:
                saldo = (saldo+valor)
                cur.execute(f'UPDATE conta SET saldo = {saldo} WHERE nConta = {nConta}')
                cur.execute(f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Depósito", {valor});')
                con_sqlite.commit()
                print('Depósito efetuado com sucesso')
        else:
            print('conta ou senha incorreta\nVerifique os dados e tente novamente')

def janelaDepositar(janela, nConta):
        # lembrar de verificar qual o tipo de conta
        janela5 = Toplevel(janela)
        janela5.title("SGB ")
        janela5.geometry("300x300")

        janela5.configure(background="#feffff")
        janela5.resizable(width=FALSE, height=FALSE)

        frame_cima = tkinter.Frame(janela5, width=300, height=50, relief='flat', bg='#feffff')
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        frame_baixo = tkinter.Frame(janela5, width=300, height=250, relief='flat', bg='#feffff')
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        
        texto = tkinter.Label(frame_cima, text="Quanto gostaria de depositar?", anchor=NE, font=('Ivy', 15), bg='#feffff', fg=c_pri)
        texto.place(x=15, y=23)
        
        valor = Entry(frame_baixo, width=25)
        valor.place(x=70, y= 50)
        
        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(depositar, valor, nConta))
        btnconfirmar.place(x=60, y=150)
        
        btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=janela5.destroy)
        btnCancelar.place(x=151, y=150)