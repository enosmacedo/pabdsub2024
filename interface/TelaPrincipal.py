
import tkinter as tk
from estrutura.color_interface import *
from interface.TelaCadastroFunc import TelaCadastroFunc
from interface.TelaCadastroEmp import TelaCadastroEmp
class TelaPrincipal():
    def __init__(self):
        self.tela_cad_func = TelaCadastroFunc()
        self.tela_cad_emp = TelaCadastroEmp()
        self.janela_principal()

    def janela_principal(self,):
        self.princ = tk.Tk()
        self.princ.title("Janela principal")
        self.princ.minsize(1200, 800)
        self.princ.resizable(False, False)
        self.princ.configure(background= cor_fundo_janelas)
        self.princ.focus_force()
        self.princ.grab_set()  
        
        self.frame_janela_principal = tk.Frame(self.princ, bg='lightgray', borderwidth=2, relief='raised')
        self.frame_janela_principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)
        self.recado=tk.Label(self.frame_janela_principal, text="Apenas para teste", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 20))
        self.recado.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.recado1=tk.Label(self.princ, text="janela a definir funções", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 20))
        self.recado1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)



        self.btn=tk.Button(self.princ, text="cadastrar funcionário", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 8),
                            command= self.tela_cad_func.janela_cadastro_func)
        self.btn.place(relx=0.1, rely=0.75, relwidth=0.12, relheight=0.08)
        self.btn=tk.Button(self.princ, text="cadastrar Empresa", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 8),
                            command= self.tela_cad_emp.janela_cadastro_emp)
        self.btn.place(relx=0.3, rely=0.75, relwidth=0.12, relheight=0.08)
    