from ctypes.wintypes import DOUBLE
from functools import partial
from tokenize import Double
from connection_sqlite import *

from tkinter import *
from tkinter.ttk import *


def sacar(valor, nConta):
        valor = float(valor.get())
        user_list = []
        cur.execute(f'select * from conta where nConta = {nConta}')

        for x in cur:
            user_list.append(x)
        if user_list.__len__() == 1:
            saldo = user_list[0][5]
            if(saldo-valor) < 0:
                print('Saldo insuficiente')
            else:
                saldo = (saldo-valor)
                cur.execute(f'UPDATE conta SET saldo = {saldo} WHERE nConta = {nConta};')
    
                cur.execute(f'INSERT INTO transacao (nconta, tipo, valor) VALUES ({nConta}, "Saque", {valor});')
                con_sqlite.commit()
                print('Saque efetuado com sucesso')
        else:
            print('conta ou senha incorreta\nVerifique os dados e tente novamente')

def janelaSacar(janela, nConta):
        # lembrar de verificar qual o tipo de conta
        
        janela4 = Toplevel(janela)
        janela4.title("SGB ")
        janela4.geometry("300x240")
        
        texto = Label(janela4, text=" Quanto gostaria de sacar? ")
        texto.place(x=70, y=20)
        
        
        valor = Entry(janela4, width=25)
        valor.place(x=70, y= 50)

        btnconfirmar = Button(janela4, text="confirmar", command=partial(sacar, valor,  nConta))
        btnconfirmar.place(x=50, y=150)
        
        btnCancelar = Button(janela4, text="Cancelar")
        btnCancelar.place(x=160, y=150)