from cmath import inf
from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import messagebox

from Gerente import Gerente
from Diretor import Diretor

import tela_incial
import tela_inicial_funcionario

c_pri = "#2d6375"
branco = "#D7E0D7"
c_sec = "#193842"
letra = "#403d3d"


def emprestimo(nConta, valor, nome):

    valor = float(valor)

   
    gerente = Gerente('0','0','0','0','0','0','0')
    gerente.realizaEmprestimo(nConta,valor,nome)
        
     

def emprestimoFuncionario(nConta, valor, nome, matricula):
    
    matriculaVerificar = matricula.get()
    matricula = int(matricula.get())
    
    cur.execute(f'SELECT matricula FROM funcionario WHERE matricula = {matricula}')
    matricula_bd = cur.fetchall()
    
    if matricula_bd != []:
        if matriculaVerificar == matricula_bd[0][0]:
            valor = float(valor)
                        
            diretor = Diretor('0','0','0','0','0','0','0')
            diretor.emprestimoFuncionario(nConta, valor, nome)
        else:
            messagebox.showwarning('', 'Senha inválida! Tente novamente')
                
    else:
        messagebox.showwarning('', 'Usuário inválido! Tente novamente')       

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

    
    cur.execute(f'select * from funcionario where matricula = {matricula}')
    info = cur.fetchall()
    nome = info[0][1]
    
    textoInicial = tkinter.Label(frame_cima, text="EMPRESTIMO", anchor=NE, font=(
        'Ivy', 18), bg='#feffff', fg=c_pri)
    textoInicial.place(x=10, y=10)

    linha = tkinter.Label(frame_cima, text="", anchor=NW,
                          width=275, font=('Ivy 1'), bg=c_sec, fg=letra)
    linha.place(x=10, y=45)

    nConta = tkinter.Label(frame_baixo, text="Nº conta *: ",
                           anchor=NW, font=('Ivy', 10), bg='#feffff', fg=c_pri)
    nConta.place(x=10, y=30)

    inputnConta = tkinter.Entry(frame_baixo, width=25, font=(
        "", 8), highlightthickness=1, relief='solid')
    inputnConta.place(x=120, y=30)

    valor = tkinter.Label(frame_baixo, text="valor *: ", anchor=NW,
                          font=('Ivy', 10), bg='#feffff', fg=c_pri)
    valor.place(x=10, y=60)

    inputvalor = tkinter.Entry(frame_baixo, width=25, font=(
          "", 8), highlightthickness=1, relief='solid')
    inputvalor.place(x=120, y=60)

    if info[0][3] == "gerente":
        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=(
                'Ivy 8 bold'), relief=FLAT, command=lambda:[emprestimo(inputnConta.get(), inputvalor.get(), nome), janela7.destroy()])
        btnconfirmar.place(x=60, y=150)

    elif info[0][3] == "diretor":
        matricula = tkinter.Label(frame_baixo, text="matricula *: ", anchor=NW,
                          font=('Ivy', 10), bg='#feffff', fg=c_pri)
        matricula.place(x=10, y=90)

        inputmatricula = tkinter.Entry(frame_baixo, width=25, font=(
          "", 8), highlightthickness=1, relief='solid')
        inputmatricula.place(x=120, y=90)

        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=(
                'Ivy 8 bold'), relief=FLAT, command=lambda:[emprestimoFuncionario(inputnConta.get(), inputvalor.get(), nome, inputmatricula),janela7.destroy()])
        btnconfirmar.place(x=60, y=150)

    btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=(
            'Ivy 8 bold'), relief=FLAT, command=lambda:[tela_inicial_funcionario.janelaEntrarFuncionario(matricula),janela7.destroy()])
    btnCancelar.place(x=151, y=150)

  