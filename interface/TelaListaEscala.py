from estrutura.Controller import BDControlador
import tkinter as tk
import tkinter as ttk

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

        self.lista_escala= ttk.Treeview(self.frame2, height=3, column=("col_1","col_2","col_3","col_4","col_5","col_6","col_7","col_8","col_9","col_10","col11") )
        self.lista_escala.heading ("#0", text= "")
        self.lista_escala.heading ("#1",text="CPF")
        self.lista_escala.heading ("#2",text="Regist. Geral")
        self.lista_escala.heading ("#3",text="Data Nasc.")
        self.lista_escala.heading ("#4",text="Nome")
        self.lista_escala.heading ("#5",text="Rua")
        self.lista_escala.heading ("#6",text="Bairro")
        self.lista_escala.heading ("#7",text="Cidade")
        self.lista_escala.heading ("#8",text="Estado")
        self.lista_escala.heading ("#9",text="Telefone")
        self.lista_escala.heading ("#10",text="Celular")
        self.lista_escala.heading ("#11",text="Est Civil")

        self.lista_escala.column ("#0",width=1)
        self.lista_escala.column ("#1",width=50)
        self.lista_escala.column ("#2",width=49)
        self.lista_escala.column ("#3",width=60)
        self.lista_escala.column ("#4",width=90)
        self.lista_escala.column ("#5",width=50)
        self.lista_escala.column ("#6",width=50)
        self.lista_escala.column ("#7",width=50)
        self.lista_escala.column ("#8",width=50)
        self.lista_escala.column ("#9",width=50)
        self.lista_escala.column ("#10",width=50)
        self.lista_escala.column ("#11",width=50)
        

        self.lista_escala.place(relx=0.01,rely=0.02, relwidth=0.95,relheight=0.9)

        #barra de rolagem 
        self.rolagem_lista_escala=Scrollbar(self.frame2, orient="vertical")
        self.lista_escala.configure(yscroll= self.rolagem_lista_cliente.set)
        self.rolagem_lista_escala.place(relx=0.96,rely=0.01, relwidth=0.03,relheight=0.85)

        self.lista_escala.bind("<Double-1>", self.duplo_click_cliente)


