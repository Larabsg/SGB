from cmath import inf
from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tkinter

c_pri = "#2d6375"
branco = "#D7E0D7"
c_sec = "#193842"
letra = "#403d3d"


def emprestimo(nConta, valor, nome, matricula):
    # COLOCAR TUDO ISSO NAS CLASSES
    user_list = []
    # nConta = 10101
    cur.execute(f'select * from conta where nConta = {nConta}')

    valor = float(valor)

    for x in cur:
        user_list.append(x)
    if user_list.__len__() == 1:
        saldo = user_list[0][5]
    
    cur.execute(f'select * from funcionario where matricula = {matricula}')
    # mdar essa logica
    if matricula != 0:
        if saldo < 0:
            # Quando o saldo está negativo

            taxa = ((saldo*0.2)*-1)
            saldo = saldo + valor
            valor = valor + taxa
            sql = "UPDATE conta SET saldo = ?, temEmprestimo = ?, gerente = ?, valorEmprestimo = ? WHERE nConta = ?"
            cur.execute(sql, (saldo, TRUE, nome, valor, nConta))

            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Empréstimo", {valor});')
            con_sqlite.commit()
            print('Empréstimo efetuado com sucesso')

        else:

            taxa = (saldo*0.2)
            saldo = saldo + valor
            valor = valor + taxa

            sql = "UPDATE conta SET saldo = ?, temEmprestimo = ?, gerente = ?, valorEmprestimo = ? WHERE nConta = ?"
            cur.execute(sql, (saldo, TRUE, nome, valor, nConta))

            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Empréstimo", {valor});')
            con_sqlite.commit()

            print('Empréstimo efetuado com sucesso')

    else:

        if saldo < 0:
            # Quando o saldo está negativo

            taxa = ((saldo*0.5)*-1)
            saldo = saldo + valor
            valor = valor + taxa
            sql = "UPDATE conta SET saldo = ?, temEmprestimo = ?, gerente = ?, valorEmprestimo = ? WHERE nConta = ?"
            cur.execute(sql, (saldo, TRUE, nome, valor, nConta))

            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Empréstimo", {valor});')
            con_sqlite.commit()
            print('Empréstimo efetuado com sucesso')

        else:

            taxa = (saldo*0.5)
            saldo = saldo + valor
            valor = valor + taxa

            sql = "UPDATE conta SET saldo = ?, temEmprestimo = ?, gerente = ?, valorEmprestimo = ? WHERE nConta = ?"
            cur.execute(sql, (saldo, TRUE, nome, valor, nConta))

            cur.execute(
                f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Empréstimo", {valor});')
            con_sqlite.commit()

            print('Empréstimo efetuado com sucesso')


def janelaEmprestimo(matricula):

    janela7 = Tk()
    janela7.title("SGB ")
    janela7.geometry("300x300")
    janela7.configure(background="#feffff")
    janela7.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(
        janela7, width=300, height=50, relief='flat', bg='#feffff')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(
        janela7, width=300, height=250, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # user_list = []
    cur.execute(f'select * from funcionario where matricula = {matricula}')
    info = cur.fetchall()
    nome = info[0][1]
    # cargo = info[0][3]
    textoInicial = tkinter.Label(frame_cima, text="EMPRESTIMO", anchor=NE, font=(
        'Ivy', 18), bg='#feffff', fg=c_pri)
    textoInicial.place(x=10, y=10)

    linha = tkinter.Label(frame_cima, text="", anchor=NW,
                          width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
    linha.place(x=10, y=45)

    if info[0][3] == "gerente":

        nConta = tkinter.Label(frame_baixo, text="Nº conta *: ",
                               anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
        nConta.place(x=10, y=30)

        inputnConta = tkinter.Entry(frame_baixo, width=25, font=(
            "", 8), highlightthickness=1, relief='solid')
        inputnConta.place(x=120, y=30)

        valor = tkinter.Label(frame_baixo, text="valor *: ", anchor=NW,
                              font=('Ivy', 10), bg='#feffff', fg=c_pri)
        valor.place(x=10, y=70)

        inputvalor = tkinter.Entry(frame_baixo, width=25, font=(
            "", 8), highlightthickness=1, relief='solid')
        inputvalor.place(x=120, y=70)

        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=(
            'Ivy 8 bold'), relief=FLAT, command=lambda: emprestimo(inputnConta.get(), inputvalor.get(), nome, 0))
        btnconfirmar.place(x=60, y=150)

        btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=(
            'Ivy 8 bold'), relief=FLAT, command=janela7.destroy)
        btnCancelar.place(x=151, y=150)

    elif info[0][3] == "diretor":

        nConta = tkinter.Label(frame_baixo, text="Nº conta *: ",
                               anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
        nConta.place(x=10, y=30)

        inputnConta = tkinter.Entry(frame_baixo, width=25, font=(
            "", 8), highlightthickness=1, relief='solid')
        inputnConta.place(x=120, y=30)

        valor = tkinter.Label(frame_baixo, text="valor *: ", anchor=NW,
                              font=('Ivy', 10), bg='#feffff', fg=c_pri)
        valor.place(x=10, y=70)

        inputvalor = tkinter.Entry(frame_baixo, width=25, font=(
            "", 8), highlightthickness=1, relief='solid')
        inputvalor.place(x=120, y=70)

        matriculat = tkinter.Label(frame_baixo, text="matricula *: ", anchor=NW,
                              font=('Ivy', 10), bg='#feffff', fg=c_pri)
        matriculat.place(x=10, y=70)

        inputmatricula = tkinter.Entry(frame_baixo, width=25, font=(
            "", 8), highlightthickness=1, relief='solid')
        inputmatricula.place(x=120, y=70)
        
        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=(
            'Ivy 8 bold'), relief=FLAT, command=lambda: emprestimo(inputnConta.get(), inputvalor.get(), nome, matricula))
        btnconfirmar.place(x=60, y=150)

        btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=(
            'Ivy 8 bold'), relief=FLAT, command=janela7.destroy)
        btnCancelar.place(x=151, y=150)

