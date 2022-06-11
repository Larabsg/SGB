from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
import tkinter
from tkinter.ttk import *
from tela_visualizar_contas import janelaVisualizarContas
from Diretor import Diretor

c_pri = "#2d6375"
branco = "#D7E0D7"
c_sec = "#193842"

def janelaAgencia(diretor: Diretor):
        # lembrar de verificar qual o tipo de conta
        janela = Tk()
        janela.title("SGB ")
        janela.geometry("300x300")

        janela.configure(background="#feffff")
        janela.resizable(width=FALSE, height=FALSE)

        frame_cima = tkinter.Frame(janela, width=300, height=50, relief='flat', bg='#feffff')
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        frame_baixo = tkinter.Frame(janela, width=300, height=250, relief='flat', bg='#feffff')
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        
        texto = tkinter.Label(frame_cima, text="De qual agência gostaria de verificar?", anchor=NE, font=('Ivy', 12), bg='#feffff', fg=c_pri)
        texto.place(x=15, y=23)
        
        agencia = Entry(frame_baixo, width=25)
        agencia.place(x=70, y= 50)
        
        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda: janelaVisualizarContas(diretor.visualizarContas(agencia.get())))
        btnconfirmar.place(x=60, y=150)
        
        btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=janela.destroy)
        btnCancelar.place(x=151, y=150)