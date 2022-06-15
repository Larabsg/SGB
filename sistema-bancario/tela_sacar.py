from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tkinter

from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

c_pri = "#2d6375"
branco = "#D7E0D7"
c_sec = "#193842"

def sacar(valor, nConta):
        valor = float(valor.get())
        user_list = [] 
        
        cur.execute(f'select * from conta where nConta = {nConta}')
        # info = cur.fetchall()
        # print(info[0][6])
        
        for x in cur:
            user_list.append(x)
            
        if user_list.__len__() == 1:
            saldo = user_list[0][5]
            
            
            if user_list[0][6] == "Corrente":
                c1 = ContaCorrente(nConta, 0, '0', '0', '0', '0', '0', '0')
                c1.sacar(valor,nConta)
                
            elif user_list[0][6] == "Poupança":
                
                if(saldo-valor) < 0:
                    print('Saldo insuficiente, sua conta não possui Cheque especial')
                else:
                    c2 = ContaPoupanca(nConta, 0, '0', '0', '0', '0', '0', '0', '0')
                    c2.sacar(valor,nConta)
            else:
                print("Sem tipo de conta")
        else:
            print('conta ou senha incorreta\nVerifique os dados e tente novamente')

def janelaSacar(nConta):
        # lembrar de verificar qual o tipo de conta
        
        janela4 = Tk()
        janela4.title("SGB ")
        janela4.geometry("300x300")

        janela4.configure(background="#feffff")
        janela4.resizable(width=FALSE, height=FALSE)

        frame_cima = tkinter.Frame(janela4, width=300, height=50, relief='flat', bg='#feffff')
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        frame_baixo = tkinter.Frame(janela4, width=300, height=250, relief='flat', bg='#feffff')
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        
        texto = tkinter.Label(frame_cima, text=" Quanto gostaria de sacar? ", anchor=NE, font=('Ivy', 15), bg='#feffff', fg=c_pri)
        texto.place(x=15, y=23)
        
        valor = Entry(frame_baixo, width=25)
        valor.place(x=70, y= 50)

        btnconfirmar = tkinter.Button(frame_baixo, text="Confirmar", width=10, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=lambda:[sacar(valor,  nConta)])
        btnconfirmar.place(x=60, y=150)
        
        btnCancelar = tkinter.Button(frame_baixo, text="Cancelar", width=10, height=2, bg=c_sec, fg=branco, font=('Ivy 8 bold'), relief=FLAT, command=janela4.destroy)
        btnCancelar.place(x=151, y=150)