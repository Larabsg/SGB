from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
import tela_incial


def janelaCadastrar(janela):
        janela3 = Toplevel(janela)

        janela3.title("Cadastrar-se")
        janela3.geometry("300x300")

        textoInicial = Label(janela3, text=" Cadastrar-se! ")
        textoInicial.place(x=100, y=10)

        nome = Label(janela3, text="Nome completo: ")
        nome.place(x=20, y=40)

        inputNome = Entry(janela3, width=25)
        inputNome.place(x=120, y=40)

        cpf = Label(janela3, text="CPF: ")
        cpf.place(x=20, y=70)

        inputCpf = Entry(janela3, width=25)
        inputCpf.place(x=120, y=70)

        senha = Label(janela3, text="Senha: ")
        senha.place(x=20, y=100)

        inputSenha = Entry(janela3, width=25)
        inputSenha.place(x=120, y=100)

        nconta = Label(janela3, text="Nº conta: ")
        nconta.place(x=20, y=130)

        inputnconta = Entry(janela3, width=25)
        inputnconta.place(x=120, y=130)

        saldo = Label(janela3, text=" Saldo: ")
        saldo.place(x=20, y=165)

        inputSaldo = Entry(janela3, width=25)
        inputSaldo.place(x=120, y=165)

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

        r1 = Radiobutton(janela3, text="Corrente", variable=v0,
                     value=1, command=tipoConta)
        r2 = Radiobutton(janela3, text="Poupança", variable=v0, 
                     value=2, command=tipoConta)
                     
        r1.place(x=70, y=200)
        r2.place(x=150, y=200)
        
        
        btnCadastrar = Button(janela3, text="Cadastrar", command=lambda value="cadastrar": partial(tela_incial.janelaEntrar(value, tipoConta, inputCpf.get(),
                                                                                                                        inputnconta.get(), inputNome.get(), inputSaldo.get(), inputSenha.get(), janela)))
        btnCadastrar.place(x=100, y=230)