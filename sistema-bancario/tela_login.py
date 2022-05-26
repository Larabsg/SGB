from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
import tela_incial

c_pri = "#2d6375"
branco = "#D7E0D7"

preta = "#f0f3f5"
verde = "#3fb5a3"
letra = "#403d3d"
valor = "#38576b"
azul = "#00008e"
c_sec = "#193842"

def janelaLogin(janela):
        janela10 = Toplevel(janela)
        janela10.title("Login")
        janela10.geometry("310x300")

        janela10.configure(background="#feffff")
        janela.resizable(width=FALSE, height=FALSE)

        frame_cima = tkinter.Frame(janela10, width=300, height=50, relief='flat', bg='#feffff')
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        frame_baixo = tkinter.Frame(janela10, width=300, height=250, relief='flat', bg='#feffff')
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        texto = tkinter.Label(frame_cima, text="LOGIN", anchor=NE, font=('Ivy', 18), bg='#feffff', fg=c_pri)
        texto.place(x=5, y =5)

        linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
        linha.place(x=10, y =45)

        nconta = tkinter.Label(frame_baixo, text="Nº conta *", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
        nconta.place(x=10, y =20)

        login = tkinter.Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        login.place(x=14, y =50)

        senha = tkinter.Label(frame_baixo, text="Senha *", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
        senha.place(x=10, y =95)

        passwd = tkinter.Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
        passwd.place(x=14, y =125)

        btn = tkinter.Button(frame_baixo, text="Entrar", width=34, height=2, bg=c_sec, fg=branco, font=('Ivy 10 bold'), relief=FLAT, command=lambda: verifica_login(janela, login, passwd))
        btn.place(x=14, y =170)

def verifica_login(janela, nConta, senha):
        
        nConta = int(nConta.get())
        cur.execute(f"SELECT senha from conta where nConta = {nConta}")
        senha_bd = cur.fetchall()
        if senha_bd != []:
            if senha.get() == senha_bd[0][0]:
                tela_incial.janelaEntrar(janela, nConta)
            else:
                messagebox.showwarning('', 'Senha inválida! Tente novamente')
        else:
            messagebox.showwarning('', 'Usuário inválido! Tente novamente')

