
import tkinter as tk
from estrutura.Controller import BDControlador
from estrutura.color_interface import *
class TelaCadastroFunc:

    def __init__(self ):
        self.controle = BDControlador()
        self.janela_cadastro_func()
    



    def janela_cadastro_func(self):
        self.cad_func = tk.Tk()
        self.cad_func.minsize(1200, 800)
        self.cad_func.resizable(False, False)
        self.cad_func.title('Cadastro de Funcionários')
        self.cad_func.configure(background= cor_fundo_janelas)
        self.cad_func.focus_force()
        self.cad_func.grab_set()  
    
        self.frame1 = tk.Frame(self.cad_func, bg='lightgray', borderwidth=2, relief='raised')
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        self.frame2 = tk.Frame(self.cad_func, bg='lightgray', borderwidth=2, relief='raised')
        self.frame2.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.80)

        self.lbl = tk.Label(self.frame1, text='Vigilancia.com', bg='lightgray', font='arial 40 bold')
        self.lbl.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.70)

        self.lbl = tk.Label(self.frame2, text='Cadastro de Empresas ', bg='lightgray', font='arial 20 bold')
        self.lbl.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.10)

        self.lbl_cpf = tk.Label(self.frame2, text='CPF:', bg='lightgray')
        self.lbl_cpf.place(relx=0.03, rely=0.25, relwidth=0.1, relheight=0.05)
        self.cpf_func = tk.Entry(self.frame2)
        self.cpf_func.place(relx=0.12, rely=0.25, relwidth=0.20, relheight=0.05)

        self.lbl_fone = tk.Label(self.frame2, text='Fone:', bg='lightgray')
        self.lbl_fone.place(relx=0.03, rely=0.32, relwidth=0.1, relheight=0.05)
        self.fone_func = tk.Entry(self.frame2)
        self.fone_func.place(relx=0.12, rely=0.32, relwidth=0.20, relheight=0.05)

        self.lbl_email = tk.Label(self.frame2, text='E-mail:', bg='lightgray')
        self.lbl_email.place(relx=0.03, rely=0.39, relwidth=0.1, relheight=0.05)
        self.email_func = tk.Entry(self.frame2)
        self.email_func.place(relx=0.12, rely=0.39, relwidth=0.20, relheight=0.05)

        self.lbl_nome = tk.Label(self.frame2, text='Nome:', bg='lightgray')
        self.lbl_nome.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.05)
        self.nome_func = tk.Entry(self.frame2)
        self.nome_func.place(relx=0.43, rely=0.25, relwidth=0.42, relheight=0.05)

        self.lbl_rua = tk.Label(self.frame2, text='Rua:', bg='lightgray')
        self.lbl_rua.place(relx=0.35, rely=0.32, relwidth=0.1, relheight=0.05)
        self.rua_func = tk.Entry(self.frame2)
        self.rua_func.place(relx=0.43, rely=0.32, relwidth=0.4, relheight=0.05)

        self.lbl_num = tk.Label(self.frame2, text='Nº:', bg='lightgray')
        self.lbl_num.place(relx=0.68, rely=0.32, relwidth=0.1, relheight=0.05)
        self.num_func = tk.Entry(self.frame2)
        self.num_func.place(relx=0.75, rely=0.32, relwidth=0.1, relheigh=0.05)

        self.lbl_bairro = tk.Label(self.frame2, text='Bairro:', bg='lightgray')
        self.lbl_bairro.place(relx=0.35, rely=0.39, relwidth=0.1, relheight=0.05)
        self.bairro_func = tk.Entry(self.frame2)
        self.bairro_func.place(relx=0.43, rely=0.39, relwidth=0.40, relheight=0.05)

        self.lbl_cep = tk.Label(self.frame2, text='CEP:', bg='lightgray')
        self.lbl_cep.place(relx=0.68, rely=0.39, relwidth=0.1, relheight=0.05)
        self.cep_func = tk.Entry(self.frame2)
        self.cep_func.place(relx=0.75, rely=0.39, relwidth=0.1, relheight=0.05)

        self.cnpj = tk.Label(self.frame2, text='CNPJ:', bg='lightgray')
        self.cnpj.place(relx=0.03, rely=0.5, relwidth=0.1, relheight=0.05)
        self.cnpj_func = tk.Entry(self.frame2)
        self.cnpj_func.place(relx=0.12, rely=0.5, relwidth=0.20, relheight=0.05)
 
        self.btn = tk.Button(self.frame2, text='Cadastrar', bg='gray', fg='white', font='arial 10 bold', command=self.controle.cadastrar_func)
        self.btn.place(relx=0.80, rely=0.75, relwidth=0.10, relheight=0.05)
    