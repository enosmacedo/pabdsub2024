from estrutura.Controller import BDControlador
import tkinter as tk

class TelaListaEscala():
    def __init__(self):
        self.controlador_banco = BDControlador()
        self.conectar_banco()
        self.janela_lista_escala()

    def conectar_banco(self):
        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432
        self.controlador_banco.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)

    def janela_lista_escala(self,):
        self.list = tk.Toplevel()
        self.list.title("Lista de Escalas")
        self.list.minsize(1200, 800)
        self.list.resizable(False, False)
        self.list.configure(background= "lightgray")
         
        self.frame = tk.Frame(self.list, bg='lightgray', borderwidth=2, relief='raised')
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.20)
        self.frame2 = tk.Frame(self.list, bg='green', borderwidth=2, relief='raised')
        self.frame2.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.75)

        self.nomeempresa = tk.Label(self.frame, text='Vigilancia.com',bg='lightgray', font='arial 40 bold')
        self.nomeempresa.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)
        self.btn_cad= tk.Button(self.frame,bg="lightgray", text="Cadastrar Escala")
        self.btn_cad.place(relx=0.8, rely=0.70, relwidth=0.10, relheight=0.20)
