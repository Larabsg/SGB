from tkinter import *
from tkinter.ttk import *


def janelaPrincipal():
    janela = Tk()
    janela.geometry("300x240")

    def janelaSacar():
        # lembrar de verificar qual o tipo de conta
        janela4 = Toplevel(janela)
        janela4.title("SGB ")
        janela4.geometry("300x240")
        
        texto = Label(janela4, text=" Quanto gostaria de sacar ? ")
        texto.place(x=70, y=20)
        
        input1 = Entry(janela4, width=25)
        input1.place(x=70, y= 50)
        
        btnConfirmar = Button(janela4, text="Confirmar")
        btnConfirmar.place(x=50, y=150)
        
        btnCancelar = Button(janela4, text="Cancelar")
        btnCancelar.place(x=160, y=150)

    
    def janelaDepositar():
        # lembrar de verificar qual o tipo de conta
        janela5 = Toplevel(janela)
        janela5.title("SGB ")
        janela5.geometry("300x240")
        
        texto = Label(janela5, text=" Quanto gostaria de depositar ? ")
        texto.place(x=70, y=20)
        
        input1 = Entry(janela5, width=25)
        input1.place(x=70, y= 50)
        
        btnConfirmar = Button(janela5, text="Confirmar")
        btnConfirmar.place(x=50, y=150)
        
        btnCancelar = Button(janela5, text="Cancelar")
        btnCancelar.place(x=160, y=150)
    def janelaExtrato():
        # lembrar de verificar qual o tipo de conta
        janela6 = Toplevel(janela)
        janela6.title("SGB ")
        janela6.geometry("300x240")
        
        texto = Label(janela6, text=" Extrato ")
        texto.place(x=70, y=20)
        
    def janelaEntrar():
        janela2 = Toplevel(janela)
        janela2.title("Bem Vindo, xxxx! ")
        janela2.geometry("300x240")

        input2 = Entry(janela2, width=25)
        input2.place(x=70, y= 30)
        
        btnSacar = Button(janela2, text="Sacar", command=janelaSacar)
        btnSacar.place(x=100, y=100)

        btnDepositar = Button(janela2, text="Depositar", command=janelaDepositar)
        btnDepositar.place(x=50, y=150)
        
        btnExtrato = Button(janela2, text="Extrato", command=janelaExtrato)
        btnExtrato.place(x=160, y=150)

        
        

    
    def janelaCadastrar():
        janela3 = Toplevel(janela)

        janela3.title("Cadastrar-se")
        janela3.geometry("300x240")

        textoInicial = Label(janela3, text=" Cadastrar-se! ")
        textoInicial.grid(column=1, row=0)

        nome = Label(janela3, text="Nome completo: ")
        nome.grid(column=0, row=1)
        

        input1 = Entry(janela3, width=25)
        input1.grid(column=1, row=1)

        cpf = Label(janela3, text="CPF: ")
        cpf.grid(column=0, row=2)

        input2 = Entry(janela3, width=25)
        input2.grid(column=1, row=2)

        senha = Label(janela3, text="Senha: ")
        senha.grid(column=0, row=3)

        input3 = Entry(janela3, width=25)
        input3.grid(column=1, row=3)

        # radiubuttons
        v0 = IntVar()
        v0.set(1)
        r1 = Radiobutton(janela3, text="Corrente", variable=v0, value=1)
        r2 = Radiobutton(janela3, text="Poupança", variable=v0, value=2)
        r1.place(x=100, y=100)
        r2.place(x=180, y=100)

        btnCadastrar = Button(janela3, text="Cadastrar", command=janelaEntrar)
        btnCadastrar.place(x=120, y=130)

    janela.title("Sistema Bancário")

    texto = Label(janela, text=" Bem Vindo! ")
    texto.grid(column=1, row=0)

    nConta = Label(janela, text="Nº conta: ")
    nConta.grid(column=0, row=1)

    input1 = Entry(janela, width=25)
    input1.grid(column=1, row=1)

    senha = Label(janela, text="Senha: ")
    senha.grid(column=0, row=3)

    input2 = Entry(janela, width=25)
    input2.grid(column=1, row=3)

    btn = Button(janela, text="Entrar", command=janelaEntrar)
    btn.grid(column=1, row=4)

    btnCadastro = Button(janela, text="Cadastrar-se", command=janelaCadastrar)
    btnCadastro.grid(column=1, row=5)

    # fechando a janela principal
    mainloop()


janelaPrincipal()
