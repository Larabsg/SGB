from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tela_incial
import tkinter
from Funcionario import Funcionario
#from tela_inicial_funcionario import janelaEntrarFuncionario

from Conta import Conta

c_pri = "#2d6375"
branco = "#D7E0D7"
letra = "#403d3d"
c_sec = "#193842"

def janelaCadastrarFuncionario():
    janela = Tk()
    janela.geometry("300x330")

    janela.configure(background="#feffff")
    janela.resizable(width=FALSE, height=FALSE)

    frame_cima = tkinter.Frame(janela, width=300, height=50, relief='flat', bg='#feffff')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = tkinter.Frame(janela, width=300, height=280, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    textoInicial = tkinter.Label(frame_cima, text="CADASTRO FUNCIONÁRIOS", anchor=NE, font=('Ivy', 15), bg='#feffff', fg=c_pri)
    textoInicial.place(x=5, y=5)

    linha = tkinter.Label(frame_cima, text="", anchor=NW, width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
    linha.place(x=10, y =45)

    nome = tkinter.Label(frame_baixo, text="Nome completo *: ", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nome.place(x=10, y=20)

    inputNome = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputNome.place(x=120, y=20)

    matricula = tkinter.Label(frame_baixo, text="Matrícula *: ", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    matricula.place(x=10, y=50)

    inputmatricula = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputmatricula.place(x=120, y=50)

    cargo = tkinter.Label(frame_baixo, text="Cargo *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    cargo.place(x=10, y=80)

    inputCargo = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputCargo.place(x=120, y=80)

    senha = tkinter.Label(frame_baixo, text="Senha *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    senha.place(x=10, y=110)

    inputSenha = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputSenha.place(x=120, y=110)

    salario = tkinter.Label(frame_baixo, text="Valor salário *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    salario.place(x=10, y=140)

    inputSalario = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputSalario.place(x=120, y=140)
    
    nConta = tkinter.Label(frame_baixo, text="Nº Conta *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nConta.place(x=10, y=170)

    inputnConta = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputnConta.place(x=120, y=170)

    agencia = tkinter.Label(frame_baixo, text="Agência *:", anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    agencia.place(x=10, y=200)

    inputAgencia = tkinter.Entry(frame_baixo, width=25, font=("", 8), highlightthickness=1, relief='solid')
    inputAgencia.place(x=120, y=200)

    btnCadastrar = tkinter.Button(frame_baixo, text="Cadastrar", width=34, height=2, bg=c_sec, fg=branco, font=('Ivy 10 bold'), relief=FLAT, command=lambda: cadastro(inputNome.get(), inputmatricula.get(), inputCargo.get(), inputSalario.get(), inputAgencia.get(), inputSenha.get(), inputnConta.get()))
    btnCadastrar.place(x=10, y=225)

    def cadastro(nome, matricula, cargo, salario, agencia, senha, nConta):
        
        funcionario = Funcionario(nome, matricula, cargo, salario, agencia, senha, nConta)
       
        sql = "INSERT INTO funcionario (nome, matricula, cargo, salario, agencia, senha, id_nConta) values(?,?,?,?,?,?,?)"
        cur.execute(sql, (funcionario.getNome, funcionario.getMatricula, funcionario.getCargo, 
                          funcionario.getSalario, funcionario.getAgencia, funcionario.getSenha, funcionario.getnConta))

        con_sqlite.commit()
        

        #janelaEntrarFuncionario(matriculaDiretor)
