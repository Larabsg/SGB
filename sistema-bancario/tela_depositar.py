from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *

def depositar(valor):
        valor = float(valor.get())
        user_list = []
        cpf = "12345"
        nconta = 1234
        cur.execute(f'select * from conta where cpf = {cpf}')

        for x in cur:
            user_list.append(x)
        if user_list.__len__() == 1:
            #saldo = str(user_list)
            saldo = user_list[0][5]
            #valor = float(input('Digite o valor para saque'))
            saldo = (saldo+valor)
            cur.execute(f'UPDATE conta SET saldo = {saldo} WHERE cpf = {cpf}')
            #cur.nextset()
            cur.execute(f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nconta}, "Depósito", {valor});')
            con_sqlite.commit()
            print('Depósito efetuado com sucesso')
        else:
            print('conta ou senha incorreta\nVerifique os dados e tente novamente')

def janelaDepositar(janela):
        # lembrar de verificar qual o tipo de conta
        janela5 = Toplevel(janela)
        janela5.title("SGB ")
        janela5.geometry("300x240")
        
        texto = Label(janela5, text=" Quanto gostaria de depositar ? ")
        texto.place(x=70, y=20)
        
        valor = Entry(janela5, width=25)
        valor.place(x=70, y= 50)
        
        btnconfirmar = Button(janela5, text="confirmar", command=partial(depositar, valor))
        btnconfirmar.place(x=50, y=150)
        
        btnCancelar = Button(janela5, text="Cancelar")
        btnCancelar.place(x=160, y=150)