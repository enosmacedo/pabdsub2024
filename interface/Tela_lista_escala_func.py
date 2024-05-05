from estrutura.Controller import BDControlador
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TelaListaEscalaFunc():
    def __init__(self):
        self.controlador_banco = BDControlador()
        self.janela_lista_escala_func()

    def conectar_banco(self):
        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432
        self.controlador_banco.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)

    def janela_lista_escala_func(self):
        self.list_func = tk.Tk()
        self.list_func.title("Lista de Escalas")
        self.list_func.minsize(1200, 800)
        self.list_func.resizable(False, False)
        self.list_func.configure(background= "lightgray")
         
        self.frame_func = tk.Frame(self.list_func, bg='lightgray', borderwidth=2, relief='raised')
        self.frame_func.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.20)
        self.frame_func1 = tk.Frame(self.list_func, bg='lightgray', borderwidth=2, relief='raised')
        self.frame_func1.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.75)

        self.nomeempresa = tk.Label(self.frame_func, text='Vigilancia.com',bg='lightgray', font='arial 40 bold')
        self.nomeempresa.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)
        self.nome_lista = tk.Label(self.frame_func, text='lista de Escalas',bg='lightgray', font='arial 30 bold')
        self.nome_lista.place(relx=0.15, rely=0.50, relwidth=0.70, relheight=0.45)

        self.label_pesquisar_func = tk.Label(self.frame_func1, text='Pesquisar:', bg='lightgray', font='arial 10 bold')
        self.label_pesquisar_func.place(relx=0.35, rely=0.02, relwidth=0.20, relheight=0.05)
        self.entrada_buscar_func = tk.Entry(self.frame_func1)
        self.entrada_buscar_func.place(relx=0.50, rely=0.02, relwidth=0.25, relheight=0.05)

        self.image_visualizar_func = PhotoImage(file="img/olho.png")
        self.image_visualizar_func = self.image_visualizar_func.subsample(2,2)
        self.botao_visual_func = tk.Button(self.frame_func1, image=self.image_visualizar_func, bg="lightgray")
        self.botao_visual_func.place(relx=0.8, rely=0.02, relwidth=0.05, relheight=0.05)

        self.lista_escala_func = ttk.Treeview (self.frame_func1, height=3, column=("col_1","col_2","col_3","col_4")) 
        
        self.lista_escala_func.heading ("#0", text= "")
        self.lista_escala_func.heading ("#1",text="Nome Mês")
        self.lista_escala_func.heading ("#2",text="Data Inicial")
        self.lista_escala_func.heading ("#3",text="Data Final.")
        self.lista_escala_func.heading ("#4",text="CNPJ Empresa")
       
        self.lista_escala_func.column ("#0",width=1)
        self.lista_escala_func.column ("#1",width=99)
        self.lista_escala_func.column ("#2",width=80)
        self.lista_escala_func.column ("#3",width=80)
        self.lista_escala_func.column ("#4",width=80)
        
        
        self.lista_escala_func.place(relx=0.01,rely=0.08, relwidth=0.95,relheight=0.9)

        self.rolagem_lista_escala_func=Scrollbar(self.frame_func1, orient="vertical")
        self.lista_escala_func.configure(yscroll= self.rolagem_lista_escala_func.set)
        self.rolagem_lista_escala_func.place(relx=0.97,rely=0.08, relwidth=0.015,relheight=0.9)

        
        self.lista_escala_func.bind("<Double-1>")
        

    