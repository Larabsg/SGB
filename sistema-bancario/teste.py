import tkinter
from tkinter import *
# pegando os valores do radiubutton
def tela_teste():
    janela3 = Tk()
    
    frame_baixo = tkinter.Frame(
        janela3, width=300, height=260, relief='flat', bg='#feffff')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    def tipoConta():  # ta indo só a opção corrente
        escolha = v0.get()
            # escolha
        print(escolha)
        if escolha == 1:
            return "Corrente"
        elif escolha == 2:
            return "Poupança"
        else:
            return "Invalida seleção"

    v0 = IntVar()
    v0.set(1)

    r1 = tkinter.Radiobutton(frame_baixo, text="Corrente", variable=v0,
                                value=1, command=lambda: tipoConta)

    r2 = tkinter.Radiobutton(frame_baixo, text="Poupança", variable=v0,
                                value=2,  command=lambda: tipoConta)

    r1.place(x=60, y=170)
    r2.place(x=140, y=170)
    btnCadastrar = tkinter.Button(frame_baixo, text="Cadastrar", width=34, height=2, font=(
        'Ivy 10 bold'), relief=FLAT, command=lambda: cadastro(tipoConta()))
    btnCadastrar.place(x=10, y=205)
    
    def cadastro(value):
        print(value)

    
    mainloop()
    
tela_teste()