from estrutura.Controller import BDControlador
from interface.TelaListaEscala import TelaListaEscala
from interface.TelaCadastroFunc import TelaCadastroFunc
import tkinter as tk
from estrutura.color_interface import *
from tkinter import messagebox
class TelaLogin():
    def __init__(self): 
        
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
        self.login=tk.Tk()
        self.login.title(" Login")
        self.login.geometry("400x300")
        self.login.iconbitmap()
        self.login.configure(bg=cor_fundo_login)
        self.login.resizable(False,False)

        self.texto=tk.Label(self.login,text="Vigilancia.Com",bg=cor_fundo_login ,font=("Times",20),fg=cor_letra_login)
        self.texto.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.12)

        self.username_login=tk.Entry(self.login,font=("Times",15))
        self.password_login=tk.Entry(self.login,font=("Times",15),show="*")
        self.btn_login=tk.Button(self.login,text="login", command=self.acessar_login)

        self.username_login.place(relx=0.2,rely=0.3, relwidth=0.6,relheight=0.15)
        self.password_login.place(relx=0.2,rely=0.5, relwidth=0.6,relheight=0.15)
        self.btn_login.place(relx=0.29,rely=0.72, relwidth=0.4,relheight=0.15)

        self.login.bind("<Return>",self.entrar_login)
    
    def limpar_campos(self):
        self.username_login.delete(0, tk.END)
        self.password_login.delete(0, tk.END)

    def entrar_login(self,event):
        self.acessar_login()

    def acessar_login(self, event=None):
        if self.username_login.get() == "" or self.password_login.get() == "":
            self.limpar_campos()
            msg = "Preencha todos os campos"
            messagebox.showinfo("Erro", msg)
        else:
            usuario = self.username_login.get()
            senha = self.password_login.get()
            cargo, password = self.controlador_banco.get_password(usuario, senha)
        
            if cargo == "Gerente" and password is not None: 
                self.login.destroy()
                TelaListaEscala()
        
            elif cargo != "Gerente" and password is not None:
                self.login.destroy()
                TelaCadastroFunc()
            else:
                self.limpar_campos()
                msg = "Login ou senha inválidos"
                messagebox.showinfo("Erro", msg)
