from estrutura.Controller import BDControlador
import tkinter as tk
from estrutura.color_interface import *
root = tk.Tk()
class TelaLogin():
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
        self.username_login=tk.Entry(self.login, bg= cor_entry, fg=cor_letra_entry_login, border=1,  font=("Arial", 12))
        self.username_login.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.08)


        self.password_label=tk.Label(self.login, text="Senha",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
        self.password_label.place(relx=0.42, rely=0.4, relwidth=0.15, relheight=0.1)
        self.password_login=tk.Entry(self.login, bg= cor_entry, fg=cor_letra_entry_login, font=("Arial", 12), show="*")
        self.password_login.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.08)
        self.usuario = self.username_login.get()
        self.senha = self.password_login.get()
        self.login_senha =self.controlador_banco.get_password(self.usuario)
        if login_senha == self.senha:
            #Deu certo. Login aceito.
            #Passe para a proxima tela.
        else:
            return messagebox.showwarning("Erro", "Login ou senha inválidos")

        self.btn=tk.Button(self.login, text="Entrar", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12), command= self.login_emp)
        self.btn.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.1)
    
    

    
    
