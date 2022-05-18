import Conta

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

        
        
        btnSacar = Button(janela2, text="Sacar", command=janelaSacar)
        btnSacar.place(x=100, y=100)

        btnDepositar = Button(janela2, text="Depositar", command=janelaDepositar)
        btnDepositar.place(x=50, y=150)
        
        btnExtrato = Button(janela2, text="Extrato", command=janelaExtrato)
        btnExtrato.place(x=160, y=150)
    

    
    def janelaCadastrar():
        janela3 = Toplevel(janela)

        janela3.title("Cadastrar-se")
        janela3.geometry("300x300")

        textoInicial = Label(janela3, text=" Cadastrar-se! ")
        textoInicial.place(x=100, y =10)

        nome = Label(janela3, text="Nome completo: ")
        nome.place(x=20, y =40)

        inputNome = Entry(janela3, width=25)
        inputNome.place(x=120, y =40)

        cpf = Label(janela3, text="CPF: ")
        cpf.place(x=20, y =70)

        inputCpf = Entry(janela3, width=25)
        inputCpf.place(x=120, y =70)

        senha = Label(janela3, text="Senha: ")
        senha.place(x=20, y =100)

        inputSenha = Entry(janela3, width=25)
        inputSenha.place(x=120, y =100)

        nConta = Label(janela3, text="Nº conta: ")
        nConta.place(x=20, y =130)

        inputnConta = Entry(janela3, width=25)
        inputnConta.place(x=120, y =130)
        
        saldo = Label(janela3, text=" Saldo: ")
        saldo.place(x=20, y=165)
        
        inputSaldo = Entry(janela3, width=25)
        inputSaldo.place(x=120, y= 165)
        
        # radiubuttons
        v0 = IntVar()
        v0.set(1)
        r1 = Radiobutton(janela3, text="Corrente", variable=v0, value=1)
        r2 = Radiobutton(janela3, text="Poupança", variable=v0, value=2)
        r1.place(x=70, y=200)
        r2.place(x=150, y=200)
        
        tipoConta = 'undefinied'
        
        if r1 is not None:
            tipoConta = 'corrente'
        elif r2 is not None:
            tipoConta = 'poupança'
        else:
            tipoConta = 'undefinied'
        
        btnCadastrar = Button(janela3, text="Cadastrar", command=janelaEntrar)
        btnCadastrar.place(x=100, y=230)
        
     
        c1 = Conta()
        c1.depositar
            
    janela.title("Sistema Bancário")

    texto = Label(janela, text=" Bem Vindo! ")
    texto.place(x=100, y =10)

    nConta = Label(janela, text="Nº conta: ")
    nConta.place(x=20, y =40)

    input1 = Entry(janela, width=25)
    input1.place(x=90, y =40)

    senha = Label(janela, text="Senha: ")
    senha.place(x=20, y =70)

    input2 = Entry(janela, width=25)
    input2.place(x=90, y =70)

    btn = Button(janela, text="Entrar", command=janelaEntrar)
    btn.place(x=40, y =150)

    btnCadastro = Button(janela, text="Cadastrar-se", command=janelaCadastrar)
    btnCadastro.place(x=150, y =150)

    # fechando a janela principal
    mainloop()


janelaPrincipal()
