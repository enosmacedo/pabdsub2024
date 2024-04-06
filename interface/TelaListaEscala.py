from estrutura.Controller import BDControlador
import tkinter as tk

class TelaListaEscala():
    def __init__(self):
        self.controlador_banco = BDControlador()
        self.connect_database()
        self.janela_lista_escala()

    def connect_database(self):
        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432
        self.controlador_banco.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)

    def janela_lista_escala(self,):
        self.list = tk.Toplevel()
        self.list.title("Janela principal")
        self.list.minsize(1200, 800)
        self.list.transient(login)
        self.list.resizable(False, False)
        self.list.configure(background= "lightgray")
         
        
        self.frame_janela_Lista = tk.Frame(self.list, bg="lightgray", borderwidth=2, relief='raised')
        self.frame_janela_Lista.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)
        self.recado=tk.Label(self.frame_janela_Lista, text="Apenas para teste", bg= "gray", fg="white", font=("Arial", 20))
        self.recado.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.recado1=tk.Label(self.frame_janela_Lista, text="janela a definir funções", bg= "gray", fg= "white", font=("Arial", 20))
        self.recado1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        
