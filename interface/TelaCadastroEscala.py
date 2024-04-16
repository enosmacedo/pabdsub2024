import tkinter as tk
from estrutura.color_interface import *
from estrutura.Controller import BDControlador

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
        self.cad_emp = tk.Tk()
        self.cad_emp.minsize(1200, 800)
        self.cad_emp.resizable(False, False)
        self.cad_emp.title('Cadastro de Escalas')
        self.cad_emp.configure(background= cor_fundo_janelas)
        self.cad_emp.focus_force()
        self.cad_emp.grab_set()  
    
        self.frame3 = tk.Frame(self.cad_emp, bg='lightgray', borderwidth=2, relief='raised')
        self.frame3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        self.frame4 = tk.Frame(self.cad_emp, bg='lightgray', borderwidth=2, relief='raised')
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
    
    


    def cadastrar_escala(self):
        nome_mes = self.nome_mes.get()
        data_inicio = self.data_inicio.get()
        data_final = self.data_final.get()
        cnpj_emp = self.cnpj_emp.get()
        self.controle.cadastroEscala(nome_mes, data_inicio, data_final, cnpj_emp)





