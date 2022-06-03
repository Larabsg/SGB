from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tela_incial
import tkinter

from Conta import Conta

c_pri = "#2d6375"
branco = "#D7E0D7"

preta = "#f0f3f5"
verde = "#3fb5a3"
letra = "#403d3d"
valor = "#38576b"
azul = "#00008e"
c_sec = "#193842"

def janelaCadastrar():
    janela3 = Tk()

    #janela3.title("Cadastrar-se")
    janela3.geometry("300x310")

    janela3.configure(background="#feffff")
    janela3.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(janela3, width=300, height=50, relief='flat', bg='#feffff')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela3, width=300, height=260, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    textoInicial = tkinter.Label(frame_cima, text="CADASTRO", anchor=NE, font=('Ivy', 18), bg='#feffff', fg=c_pri)
    textoInicial.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
    linha.place(x=10, y =45)

    nome = tkinter.Label(frame_baixo, text="Nome completo *: ", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nome.place(x=10, y=20)

    inputNome = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputNome.place(x=120, y=20)

    cpf = tkinter.Label(frame_baixo, text="CPF *: ", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    cpf.place(x=10, y=50)

    inputCpf = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputCpf.place(x=120, y=50)

    senha = tkinter.Label(frame_baixo, text="Senha *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    senha.place(x=10, y=80)

    inputSenha = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputSenha.place(x=120, y=80)

    nconta = tkinter.Label(frame_baixo, text="Nº conta *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nconta.place(x=10, y=110)

    inputnconta = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputnconta.place(x=120, y=110)

    saldo = tkinter.Label(frame_baixo, text="Saldo *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    saldo.place(x=10, y=140)

    inputSaldo = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputSaldo.place(x=120, y=140)

    # pegando os valores do radiubutton
    def tipoConta():
        escolha = v0.get()
        if escolha == 1:
            return "Corrente"
        elif escolha == 2:
            return "Poupança"
        else:
            return "Invalida seleção"

    v0 = IntVar()
    v0.set(1)

    r1 = tkinter.Radiobutton(frame_baixo, text="Corrente", variable=v0,
                     value=1, command=tipoConta)
    r2 = tkinter.Radiobutton(frame_baixo, text="Poupança", variable=v0,
                     value=2, command=tipoConta)

    r1.place(x=60, y=170)
    r2.place(x=140, y=170)

    btnCadastrar = tkinter.Button(frame_baixo, text="Cadastrar", width=34, height=2, bg=c_sec, fg=branco, font=('Ivy 10 bold'), relief=FLAT, command=lambda: cadastro(inputNome.get(), inputCpf.get(), inputSenha.get(), inputnconta.get(), inputSaldo.get(), tipoConta()))
    btnCadastrar.place(x=10, y=205)

    def cadastro(nome, cpf, senha, nConta, saldo, tipoConta):
        c1 = Conta(nConta, saldo, cpf, nome, senha, tipoConta)
        # cur.execute(f'INSERT INTO conta (nome, cpf, senha, nConta, saldo, tipoConta) values({c1.get_nome()}, {c1.get_cpf()}, {c1.get_senha()}, {c1.get_nConta()}, {c1.get_saldo()}, {c1.get_tipoConta()});')
        sql = "INSERT INTO conta (nome, cpf, senha, nConta, saldo, tipoConta) values(?,?,?,?,?,?)"
        cur.execute(sql, (c1.get_nome(), c1.get_cpf(), c1.get_senha(), 
                          c1.get_nConta(), c1.get_saldo(), c1.get_tipoConta()))

        con_sqlite.commit()
        

        tela_incial.janelaEntrar(nConta)
