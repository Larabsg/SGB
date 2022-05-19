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
from tela_incial import *

def verifica_login(nConta, senha):
        
        nConta = int(nConta.get())
        print(type(nConta))
        cur.execute(f"SELECT senha from conta where nConta = {nConta}")
        senha_bd = cur.fetchall()
        print(senha_bd[0][0])
        if senha.get() == senha_bd[0][0]:
            janelaEntrar(nConta)
        else:
            janelaLogin(message="Usuário ou senha inválidos! Tente novamente")

def janelaLogin(message=""):
        janela10 = Toplevel(janela)
        janela10.title("Login")
        janela10.geometry("300x300")
        nconta = Label(janela10, text="Nº conta: ")
        nconta.place(x=20, y =40)

        login = Entry(janela10, width=25)
        login.place(x=90, y =40)

        senha = Label(janela10, text="Senha: ")
        senha.place(x=20, y =70)

        passwd = Entry(janela10, width=25)
        passwd.place(x=90, y =70)

        btn = Button(janela10, text="Entrar", command=lambda: verifica_login(login, passwd))
        btn.place(x=40, y =150)

        if message != "":
            messagem = Label(janela10, text=message)
            messagem.place(x=20, y=190)