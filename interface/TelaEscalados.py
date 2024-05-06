from estrutura.Controller import BDControlador
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TelaEscalados():
    def __init__(self):
        self.controlador_banco = BDControlador()
        self.conectar_banco()
        self.janela_escalados()

    def conectar_banco(self):
        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432
        self.controlador_banco.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)

    def janela_escalados(self):
        self.escalados = tk.Tk()
        self.escalados.geometry("1200x800")
        self.escalados.resizable(False, False)
        self.escalados.title("Escalados")

        self.frame = tk.Frame(self.escalados, bg='lightgray', borderwidth=2, relief='raised')
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.20)
        self.frame2 = tk.Frame(self.escalados, bg='lightgray', borderwidth=2, relief='raised')
        self.frame2.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.75)

        self.nomeempresa = tk.Label(self.frame, text='Vigilancia.com',bg='lightgray', font='arial 40 bold')
        self.nomeempresa.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)
        self.nome_lista = tk.Label(self.frame, text='lista de Escalados',bg='lightgray', font='arial 30 bold')
        self.nome_lista.place(relx=0.15, rely=0.50, relwidth=0.70, relheight=0.45)

        self.lista_escalado = ttk.Treeview (self.frame2, height=3, column=("col_1","col_2","col_3","col_4","col_5","col_6", "col_7")) 
        
        self.lista_escalado.heading ("#0", text= "")
        self.lista_escalado.heading ("#1",text="Nome ")
        self.lista_escalado.heading ("#2",text="Data Entrada")
        self.lista_escalado.heading ("#3",text="Horario Entrada")
        self.lista_escalado.heading ("#4",text="Data Saida")
        self.lista_escalado.heading ("#5",text="Horario Saida")
        self.lista_escalado.heading ("#6",text="Posto")
        self.lista_escalado.heading ("#7",text="Cnpj Empresa")
       
        
        

        self.lista_escalado.column ("#0",width=1)
        self.lista_escalado.column ("#1",width=99)
        self.lista_escalado.column ("#2",width=80)
        self.lista_escalado.column ("#3",width=80)
        self.lista_escalado.column ("#4",width=80)
        self.lista_escalado.column ("#5",width=80)
        self.lista_escalado.column ("#6",width=80)
        self.lista_escalado.column ("#7",width=80)
        
        

        self.lista_escalado.place(relx=0.01,rely=0.08, relwidth=0.95,relheight=0.9)

        self.rolagem_lista_escalado=Scrollbar(self.frame2, orient="vertical")
        self.lista_escalado.configure(yscroll= self.rolagem_lista_escalado.set)
        self.rolagem_lista_escalado.place(relx=0.97,rely=0.08, relwidth=0.015,relheight=0.9)

    

        