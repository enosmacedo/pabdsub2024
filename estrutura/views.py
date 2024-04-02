from estrutura.Controller import BDControlador
import tkinter as tk
from estrutura.color_interface import *
root = tk.Tk()
class Interface():
    def __init__(self): 
        self.login=root
        self.controlador_banco=BDControlador()
        self.connect_database()
        self.janela_login()
        self.login.mainloop()
       

    def connect_database(self):
        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432
        self.controlador_banco.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)
    def janela_login(self):
        self.login.title("Login")
        self.login.configure(background= cor_fundo_login)
        self.login.minsize(400, 300)
        self.login.resizable(False, False)
        
        nome_emp = tk.Label(self.login, text="Vigilância.com", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 20))
        nome_emp.place(relx=0.09, rely=0.03, relwidth=0.8, relheight=0.20)

        self.username_label=tk.Label(self.login, text="Usuário",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
        self.username_label.place(relx=0.42, rely=0.2 ,relwidth=0.15, relheight=0.1)
        self.username_entry=tk.Entry(self.login, bg= cor_entry, fg=cor_letra_entry_login, border=1,  font=("Arial", 12))
        self.username_entry.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.08)


        self.password_label=tk.Label(self.login, text="Senha",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
        self.password_label.place(relx=0.42, rely=0.4, relwidth=0.15, relheight=0.1)
        self.password_entry=tk.Entry(self.login, bg= cor_entry, fg=cor_letra_entry_login, font=("Arial", 12), show="*")
        self.password_entry.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.08)
        self.btn=tk.Button(self.login, text="Entrar", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12), command= self.janela_principal)
        self.btn.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.1)
    
    def janela_principal(self,):
        self.princ = tk.Toplevel()
        self.princ.title("Janela principal")
        self.princ.minsize(1200, 800)
        self.princ.resizable(False, False)
        self.princ.transient(self.login)
        self.princ.configure(background= cor_fundo_janelas)
        self.princ.focus_force()
        self.princ.grab_set()  
        
        self.frame_janela_principal = tk.Frame(self.princ, bg='lightgray', borderwidth=2, relief='raised')
        self.recado=tk.Label(self.frame_janela_principal, text="Apenas para teste", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 20))
        self.recado.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)
        self.frame_janela_principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)
        self.btn=tk.Button(self.princ, text="cadastrar funcionário", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12), command= self.janela_cadastro_func)
        self.btn.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.1)
    

    def janela_cadastro_func(self):
        self.cad_func = tk.Toplevel()
        self.cad_func.minsize(1200, 800)
        self.cad_func.resizable(False, False)
        self.cad_func.title('Cadastro de Funcionários')
        self.cad_func.configure(background= cor_fundo_janelas)
        self.cad_func.transient(self.princ)
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
        self.cpf_entry = tk.Entry(self.frame2)
        self.cpf_entry.place(relx=0.12, rely=0.25, relwidth=0.20, relheight=0.05)

        self.lbl_fone = tk.Label(self.frame2, text='Fone:', bg='lightgray')
        self.lbl_fone.place(relx=0.03, rely=0.32, relwidth=0.1, relheight=0.05)
        self.fone_entry = tk.Entry(self.frame2)
        self.fone_entry.place(relx=0.12, rely=0.32, relwidth=0.20, relheight=0.05)

        self.lbl_email = tk.Label(self.frame2, text='E-mail:', bg='lightgray')
        self.lbl_email.place(relx=0.03, rely=0.39, relwidth=0.1, relheight=0.05)
        self.email_entry = tk.Entry(self.frame2)
        self.email_entry.place(relx=0.12, rely=0.39, relwidth=0.20, relheight=0.05)

        self.lbl_nome = tk.Label(self.frame2, text='Nome:', bg='lightgray')
        self.lbl_nome.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.05)
        self.nome_entry = tk.Entry(self.frame2)
        self.nome_entry.place(relx=0.43, rely=0.25, relwidth=0.42, relheight=0.05)

        self.lbl_rua = tk.Label(self.frame2, text='Rua:', bg='lightgray')
        self.lbl_rua.place(relx=0.35, rely=0.32, relwidth=0.1, relheight=0.05)
        self.rua_entry = tk.Entry(self.frame2)
        self.rua_entry.place(relx=0.43, rely=0.32, relwidth=0.4, relheight=0.05)

        self.lbl_num = tk.Label(self.frame2, text='Nº:', bg='lightgray')
        self.lbl_num.place(relx=0.68, rely=0.32, relwidth=0.1, relheight=0.05)
        self.num_entry = tk.Entry(self.frame2)
        self.num_entry.place(relx=0.75, rely=0.32, relwidth=0.1, relheigh=0.05)

        self.lbl_bairro = tk.Label(self.frame2, text='Bairro:', bg='lightgray')
        self.lbl_bairro.place(relx=0.35, rely=0.39, relwidth=0.1, relheight=0.05)
        self.bairro_entry = tk.Entry(self.frame2)
        self.bairro_entry.place(relx=0.43, rely=0.39, relwidth=0.40, relheight=0.05)

        self.lbl_cep = tk.Label(self.frame2, text='CEP:', bg='lightgray')
        self.lbl_cep.place(relx=0.68, rely=0.39, relwidth=0.1, relheight=0.05)
        self.cep_entry = tk.Entry(self.frame2)
        self.cep_entry.place(relx=0.75, rely=0.39, relwidth=0.1, relheight=0.05)

        self.cnpj_entry = tk.Label(self.frame2, text='CNPJ:', bg='lightgray')
        self.cnpj_entry.place(relx=0.03, rely=0.5, relwidth=0.1, relheight=0.05)
        self.cnpj_entry = tk.Entry(self.frame2)
        self.cnpj_entry.place(relx=0.12, rely=0.5, relwidth=0.20, relheight=0.05)

        self.cadastro_funcionario = self.controlador_banco.cadastrar_func  
        self.btn = tk.Button(self.frame2, text='Cadastrar', bg='gray', fg='white', font='arial 10 bold', command=self.cadastro_funcionario)
        self.btn.place(relx=0.80, rely=0.75, relwidth=0.10, relheight=0.05)
    



