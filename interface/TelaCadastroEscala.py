import tkinter as tk
from estrutura.color_interface import *
from estrutura.Controller import BDControlador
from tkinter import messagebox

class TelaCadastroEscala():

    def __init__(self):
        self.controle = BDControlador()
        self.conectar_banco()
        self.janela_cadastro_escala()

    def conectar_banco(self):
        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432
        self.controle.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)

    def janela_cadastro_escala(self):
        self.cad_escala = tk.Tk()
        self.cad_escala.minsize(1200, 800)
        self.cad_escala.resizable(False, False)
        self.cad_escala.title('Cadastro de Escalas')
        self.cad_escala.configure(background= cor_fundo_janelas)
        
        self.frame3 = tk.Frame(self.cad_escala, bg='lightgray', borderwidth=2, relief='raised')
        self.frame3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        self.frame4 = tk.Frame(self.cad_escala, bg='lightgray', borderwidth=2, relief='raised')
        self.frame4.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.80)

        self.lbl = tk.Label(self.frame3, text='Vigilancia.com', bg='lightgray', font='arial 40 bold')
        self.lbl.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.70)

        self.lbl = tk.Label(self.frame4, text='Cadastro de Escalas ', bg='lightgray', font='arial 20 bold')
        self.lbl.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.10)

        self.lbl_nome_mes = tk.Label(self.frame4, text='Nome Mês:', bg='lightgray')
        self.lbl_nome_mes.place(relx=0.03, rely=0.25, relwidth=0.1, relheight=0.05)
        self.nome_mes = tk.Entry(self.frame4)
        self.nome_mes.place(relx=0.12, rely=0.25, relwidth=0.20, relheight=0.05)

        self.lbl_data_inicio = tk.Label(self.frame4, text='Data Inicio:', bg='lightgray')
        self.lbl_data_inicio.place(relx=0.03, rely=0.32, relwidth=0.1, relheight=0.05)
        self.data_inicio = tk.Entry(self.frame4)
        self.data_inicio.place(relx=0.12, rely=0.32, relwidth=0.20, relheight=0.05)

        self.lbl_data_final = tk.Label(self.frame4, text='Data Final:', bg='lightgray')
        self.lbl_data_final.place(relx=0.45, rely=0.32, relwidth=0.1, relheight=0.05)
        self.data_final = tk.Entry(self.frame4)
        self.data_final.place(relx=0.55, rely=0.32, relwidth=0.20, relheight=0.05)

        self.lbl_cnpj_emp = tk.Label(self.frame4, text='CNPJ Empresa:', bg='lightgray')
        self.lbl_cnpj_emp.place(relx=0.40, rely=0.25, relwidth=0.20, relheight=0.05)
        self.cnpj_emp = tk.Entry(self.frame4)
        self.cnpj_emp.place(relx=0.55, rely=0.25, relwidth=0.20, relheight=0.05)

        
        self.btn = tk.Button(self.frame4, text='Cadastrar', bg='gray', fg='white', font='arial 10 bold',command=self.cadastrar_escala)
        self.btn.place(relx=0.80, rely=0.75, relwidth=0.10, relheight=0.05)
    
        self.btn = tk.Button(self.frame4, text='Voltar', bg='gray', fg='white', font='arial 10 bold')
        self.btn.place(relx=0.1, rely=0.75, relwidth=0.10, relheight=0.05)
    
    def limparEntradas(self):
        self.nome_mes.delete(0, tk.END)
        self.data_inicio.delete(0, tk.END)
        self.data_final.delete(0, tk.END)
        self.cnpj_emp.delete(0, tk.END)

  
    def cadastrar_escala(self):
        
        if self.nome_mes.get() == '' or self.data_inicio.get() == '' or self.data_final.get() == '' or self.cnpj_emp.get() == '':
            messagebox.showinfo('Erro', 'Preencha todos os campos')
        else:
            verifica = self.controle.cadastroEscala
            if verifica == True:
                messagebox.showinfo('Erro', 'Escala já Cadastrada') 
            else:
                self.controle.cadastroEscala(self.nome_mes.get(), self.data_inicio.get(), self.data_final.get(), self.cnpj_emp.get())
                messagebox.showinfo('Sucesso', 'Escala Cadastrada')
                self.limparEntradas()
                
    def voltar(self):
        self.cad_escala.destroy()
        self.TelaListaEscala()
    





