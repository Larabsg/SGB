from ast import Return
from ctypes.wintypes import DOUBLE
from functools import partial
from pydoc import cli
from tkinter import messagebox
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

    # janela3.title("Cadastrar-se")
    janela3.geometry("300x320")

    janela3.configure(background="#feffff")
    janela3.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(
        janela3, width=300, height=50, relief='flat', bg='#feffff')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(
        janela3, width=300, height=270, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    textoInicial = tkinter.Label(frame_cima, text="CADASTRO", anchor=NE, font=(
        'Ivy', 18), bg='#feffff', fg=c_pri)
    textoInicial.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW,
                          width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
    linha.place(x=10, y=45)

    nome = tkinter.Label(frame_baixo, text="Nome completo *: ",
                         anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nome.place(x=10, y=20)

    inputNome = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8), highlightthickness=1, relief='solid')
    inputNome.place(x=120, y=20)

    cpf = tkinter.Label(frame_baixo, text="CPF *: ", anchor=NW,
                        font=('Ivy', 10), bg='#feffff', fg=c_pri)
    cpf.place(x=10, y=50)

    inputCpf = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8), highlightthickness=1, relief='solid')
    inputCpf.place(x=120, y=50)

    senha = tkinter.Label(frame_baixo, text="Senha *:",
                          anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    senha.place(x=10, y=80)

    inputSenha = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8),  highlightthickness=1, relief='solid')
    inputSenha.place(x=120, y=80)

    nconta = tkinter.Label(frame_baixo, text="N?? conta *:",
                           anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nconta.place(x=10, y=110)

    inputnconta = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8), highlightthickness=1, relief='solid')
    inputnconta.place(x=120, y=110)

    saldo = tkinter.Label(frame_baixo, text="Saldo *:",
                          anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    saldo.place(x=10, y=140)

    inputSaldo = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8), highlightthickness=1, relief='solid')
    inputSaldo.place(x=120, y=140)

    tipoConta = tkinter.Label(frame_baixo, text="Tipo de conta *:",
                          anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    tipoConta.place(x=10, y=170)

    inputTipoConta = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8), highlightthickness=1, relief='solid')
    inputTipoConta.place(x=120, y=170)

    r1 = tkinter.Label(frame_baixo, text="00 - Corrente", font=('Ivy', 8), bg='#feffff', fg=c_pri)
    r2 = tkinter.Label(frame_baixo, text="01 - Poupan??a", font=('Ivy', 8), bg='#feffff', fg=c_pri)

    # pegando os valores do radiubutton
    # def tipoConta():  # ta indo s?? a op????o corrente
    #     escolha = v0.get()
    #     # escolha
    #     print(escolha)
    #     if escolha == 1:
    #         return "Corrente"
    #     elif escolha == 2:
    #         return "Poupan??a"
    #     else:
    #         return "Invalida sele????o"

    # v0 = IntVar()
    # # v0.set(1)

    # r1 = tkinter.Radiobutton(frame_baixo, text="Corrente", variable=v0,
    #                          value=1, command=lambda: tipoConta)

    # r2 = tkinter.Radiobutton(frame_baixo, text="Poupan??a", variable=v0,
    #                          value=2,  command=lambda: tipoConta)

    r1.place(x=60, y=190)
    r2.place(x=140, y=190)
    btnCadastrar = tkinter.Button(frame_baixo, text="Cadastrar", width=34, height=2, bg=c_sec, fg=branco, font=(
        'Ivy 10 bold'), relief=FLAT, command=lambda:[cadastro(inputNome.get(), inputCpf.get(), inputSenha.get(), inputnconta.get(), inputSaldo.get(), inputTipoConta.get()), janela3.destroy()])
    
    btnCadastrar.place(x=10, y=215)

    def cadastro(nome, cpf, senha, nConta, saldo, tipoConta):
        if tipoConta == "00":
            tipoConta = "Corrente"
        elif tipoConta == "01":
            tipoConta = "Poupan??a"
            
        if not nConta:
            
            print("nConta est?? vazio")
        else:
            cur.execute(f"SELECT * from conta WHERE nConta = {nConta}")
            info = cur.fetchall()

            if info == []:
                c1 = Conta(nConta, saldo, cpf, nome, senha, tipoConta,
                        "0", True)  # ver essa modifica????o

                sql = "INSERT INTO conta (nome, cpf, senha, nConta, saldo, tipoConta, agencia) values(?,?,?,?,?,?,?)"
                cur.execute(sql, (c1.get_nome(), c1.get_cpf(), c1.get_senha(),
                                c1.get_nConta(), c1.get_saldo(), c1.get_tipoConta(), 1000))

                con_sqlite.commit()
                
                tela_incial.janelaEntrar(nConta)
            else:
                messagebox.showwarning("", "N??mero de conta j?? existe no sistema! Tente novamente")
    # mainloop()  

# janelaCadastrar()

