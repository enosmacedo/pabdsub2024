import tkinter as tk
from estrutura.color_interface import *
from estrutura.Controller import BDControlador

class TelaCadastroEmp():

    def __init__(self):
        self.controle = BDControlador()
        self.janela_cadastro_emp()

    def janela_cadastro_emp(self):
        self.cad_emp = tk.Tk()
        self.cad_emp.minsize(1200, 800)
        self.cad_emp.resizable(False, False)
        self.cad_emp.title('Cadastro de Empresas')
        self.cad_emp.configure(background= cor_fundo_janelas)
        self.cad_emp.focus_force()
        self.cad_emp.grab_set()  
    
        self.frame3 = tk.Frame(self.cad_emp, bg='lightgray', borderwidth=2, relief='raised')
        self.frame3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        self.frame4 = tk.Frame(self.cad_emp, bg='lightgray', borderwidth=2, relief='raised')
        self.frame4.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.80)

        self.lbl = tk.Label(self.frame3, text='Vigilancia.com', bg='lightgray', font='arial 40 bold')
        self.lbl.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.70)

        self.lbl = tk.Label(self.frame4, text='Cadastro de Empresas ', bg='lightgray', font='arial 20 bold')
        self.lbl.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.10)

        self.lbl_cnpj = tk.Label(self.frame4, text='CNPJ:', bg='lightgray')
        self.lbl_cnpj.place(relx=0.03, rely=0.25, relwidth=0.1, relheight=0.05)
        self.cnpj_emp = tk.Entry(self.frame4)
        self.cnpj_emp.place(relx=0.12, rely=0.25, relwidth=0.20, relheight=0.05)

        self.lbl_fone = tk.Label(self.frame4, text='Fone:', bg='lightgray')
        self.lbl_fone.place(relx=0.03, rely=0.32, relwidth=0.1, relheight=0.05)
        self.fone_emp = tk.Entry(self.frame4)
        self.fone_emp.place(relx=0.12, rely=0.32, relwidth=0.20, relheight=0.05)

        self.lbl_email = tk.Label(self.frame4, text='E-mail:', bg='lightgray')
        self.lbl_email.place(relx=0.03, rely=0.39, relwidth=0.1, relheight=0.05)
        self.email_emp = tk.Entry(self.frame4)
        self.email_emp.place(relx=0.12, rely=0.39, relwidth=0.20, relheight=0.05)

        self.lbl_nome = tk.Label(self.frame4, text='Nome:', bg='lightgray')
        self.lbl_nome.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.05)
        self.nome_emp = tk.Entry(self.frame4)
        self.nome_emp.place(relx=0.43, rely=0.25, relwidth=0.42, relheight=0.05)

        self.lbl_rua = tk.Label(self.frame4, text='Rua:', bg='lightgray')
        self.lbl_rua.place(relx=0.35, rely=0.32, relwidth=0.1, relheight=0.05)
        self.rua_emp = tk.Entry(self.frame4)
        self.rua_emp.place(relx=0.43, rely=0.32, relwidth=0.4, relheight=0.05)

        self.lbl_num = tk.Label(self.frame4, text='Nº:', bg='lightgray')
        self.lbl_num.place(relx=0.68, rely=0.32, relwidth=0.1, relheight=0.05)
        self.num_emp = tk.Entry(self.frame4)
        self.num_emp.place(relx=0.75, rely=0.32, relwidth=0.1, relheigh=0.05)

        self.lbl_bairro = tk.Label(self.frame4, text='Bairro:', bg='lightgray')
        self.lbl_bairro.place(relx=0.35, rely=0.39, relwidth=0.1, relheight=0.05)
        self.bairro_emp = tk.Entry(self.frame4)
        self.bairro_emp.place(relx=0.43, rely=0.39, relwidth=0.40, relheight=0.05)

        self.lbl_cep = tk.Label(self.frame4, text='CEP:', bg='lightgray')
        self.lbl_cep.place(relx=0.68, rely=0.39, relwidth=0.1, relheight=0.05)
        self.cep_emp = tk.Entry(self.frame4)
        self.cep_emp.place(relx=0.75, rely=0.39, relwidth=0.1, relheight=0.05)
 
        self.btn = tk.Button(self.frame4, text='Cadastrar', bg='gray', fg='white', font='arial 10 bold')
        self.btn.place(relx=0.80, rely=0.75, relwidth=0.10, relheight=0.05)
    



