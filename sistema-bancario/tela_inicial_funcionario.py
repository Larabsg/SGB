from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *
from tkinter import *
from tkinter.ttk import *
import tkinter
from tela_cadastro import janelaCadastrar
from Gerente import Gerente
from Autenticavel import Autenticavel
from Diretor import Diretor
from tela_visualizar_contas import janelaVisualizarContas
from tela_visualizar_funcionarios import janelaVisualizarFuncionarios
from tela_agencia import janelaAgencia
import tela_emprestimo 

c_pri = "#2d6375"
branco = "#D7E0D7"
letra = "#403d3d"
c_sec = "#193842"


def janelaEntrarFuncionario(matricula):
    janela2 = Tk()
    janela2.geometry("310x300")

    frame_cima = tkinter.Frame(janela2, width=310, height=50, relief='flat', bg=c_pri)
    frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela2, width=310, height=250, relief='flat', bg=c_pri)
    frame_baixo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    cur.execute(f'select * from funcionario where matricula = {matricula}')
    info = cur.fetchall()

    if info[0][3] == "gerente":

        gerente = Gerente(info[0][1], info[0][2], info[0][3], info[0][4], info[0][5], info[0][6], info[0][7])

        texto = tkinter.Label(frame_cima, text=f"Olá, {info[0][1]}! ", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
        texto.place(x=5, y=5)

        linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
        linha.place(x=10, y =45)

        btnConta = tkinter.Button(frame_baixo, text="Criar nova conta", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=gerente.criaConta)
        btnConta.place(x=10, y=90)

        btnViewConta = tkinter.Button(frame_baixo, text="Visualizar contas", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(janelaVisualizarContas, gerente.getContas()))
        btnViewConta.place(x=10, y=140)
        
        btnEmprestimo = tkinter.Button(frame_baixo, text="Realizar empréstimo", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda:tela_emprestimo.janelaEmprestimo(matricula))
        btnEmprestimo.place(x=10, y=190)

    elif info[0][3] == "diretor":

        diretor = Diretor(info[0][1], info[0][2], info[0][3], info[0][4], info[0][5], info[0][6], info[0][7])

        texto = tkinter.Label(frame_cima, text=f"Olá, {info[0][1]}! ", anchor=NE, font=('Ivy', 18), bg=c_pri, fg=branco)
        texto.place(x=5, y=5)

        linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=branco, fg=letra)
        linha.place(x=10, y =45)

        btnConta = tkinter.Button(frame_baixo, text="Criar novo funcionário", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=diretor.cadastrarFuncionarios)
        btnConta.place(x=10, y=50)

        btnViewFuncionarios = tkinter.Button(frame_baixo, text="Visualizar funcionários", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(janelaVisualizarFuncionarios, diretor.visualizarFuncionarios()))
        btnViewFuncionarios.place(x=10, y=100)

        btnViewContas = tkinter.Button(frame_baixo, text="Visualizar contas", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=partial(janelaAgencia, diretor))
        btnViewContas.place(x=10, y=150)

        btnEmprestimo = tkinter.Button(frame_baixo, text="Realizar empréstimo", width=39, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda:tela_emprestimo.janelaEmprestimo(matricula))
        btnEmprestimo.place(x=10, y=200)

