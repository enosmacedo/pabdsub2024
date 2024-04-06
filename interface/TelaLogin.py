from estrutura.Controller import BDControlador
from interface.TelaPrincipal import TelaPrincipal
import customtkinter
import tkinter as tk
from estrutura.color_interface import *
from tkinter import messagebox
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
        self.login.title(" Login")
        self.login.geometry("400x300")
        self.login.iconbitmap()
        self.login.configure(bg=cor_fundo_login)
        self.login.resizable(False,False)

        self.texto=tk.Label(self.login,text="Vigilancia.Com",bg=cor_fundo_login ,font=("Times",20),fg=cor_letra_login)
        self.texto.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.12)

        self.username_login=customtkinter.CTkEntry(self.login,placeholder_text="Usuario")
        self.password_login=customtkinter.CTkEntry(self.login,placeholder_text="Senha",show="*")
        self.btn_login=customtkinter.CTkButton(self.login,text="login", command=self.acessar_login)

        self.username_login.place(relx=0.2,rely=0.3, relwidth=0.6,relheight=0.15)
        self.password_login.place(relx=0.2,rely=0.5, relwidth=0.6,relheight=0.15)
        self.btn_login.place(relx=0.29,rely=0.72, relwidth=0.4,relheight=0.15)


    def acessar_login(self):
        usuario = self.username_login.get()
        senha = self.password_login.get()
        password = self.controlador_banco.get_password(usuario, senha)
        if password is not None:
            
            self.tela_principal = TelaPrincipal().janela_principal()
            self.login.destroy()
        else:
            msg="Login ou senha inválidos"
            msg+="\n ou Campos vazios, Tente novamente"
            messagebox.showinfo("Erro", msg)
            


    
    
