from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
#import conta
#from entidades import conta
#from connection import *
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *
from interface_grafica import *
from interface_grafica import janela

def sacar(valor):
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
            if(saldo-valor) < 0:
                print('Saldo insuficiente')
            else:
                saldo = (saldo-valor)
                cur.execute(f'UPDATE conta SET saldo = {saldo} WHERE cpf = {cpf};')
                #cur.nextset()
                cur.execute(f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nconta}, "Saque", {valor});')
                con_sqlite.commit()
                print('Saque efetuado com sucesso')
        else:
            print('conta ou senha incorreta\nVerifique os dados e tente novamente')

def janelaSacar():
        # lembrar de verificar qual o tipo de conta
        
        janela4 = Toplevel(janela)
        janela4.title("SGB ")
        janela4.geometry("300x240")
        
        texto = Label(janela4, text=" Quanto gostaria de sacar? ")
        texto.place(x=70, y=20)
        
        
        valor = Entry(janela4, width=25)
        valor.place(x=70, y= 50)

        btnconfirmar = Button(janela4, text="confirmar", command=partial(sacar, valor))
        btnconfirmar.place(x=50, y=150)
        
        btnCancelar = Button(janela4, text="Cancelar")
        btnCancelar.place(x=160, y=150)