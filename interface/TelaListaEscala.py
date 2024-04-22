from estrutura.Controller import BDControlador
from interface.TelaCadastroEscala import TelaCadastroEscala
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk





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

    def janela_lista_escala(self):
        self.list = tk.Tk()
        self.list.title("Lista de Escalas")
        self.list.minsize(1200, 800)
        self.list.resizable(False, False)
        self.list.configure(background= "lightgray")
         
        self.frame = tk.Frame(self.list, bg='lightgray', borderwidth=2, relief='raised')
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.20)
        self.frame2 = tk.Frame(self.list, bg='lightgray', borderwidth=2, relief='raised')
        self.frame2.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.75)

        self.nomeempresa = tk.Label(self.frame, text='Vigilancia.com',bg='lightgray', font='arial 40 bold')
        self.nomeempresa.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)
        self.nome_lista = tk.Label(self.frame, text='lista de Escalas',bg='lightgray', font='arial 30 bold')
        self.nome_lista.place(relx=0.15, rely=0.50, relwidth=0.70, relheight=0.45)
        
        self.btn_cad= tk.Button(self.frame,bg="lightgray", text="Cadastrar Escala", command= self.cadastro_escala)
        self.btn_cad.place(relx=0.88, rely=0.30, relwidth=0.10, relheight=0.20)
        
        
        self.label_pesquisar = tk.Label(self.frame2, text='Pesquisar:', bg='lightgray', font='arial 10 bold')
        self.label_pesquisar.place(relx=0.35, rely=0.02, relwidth=0.20, relheight=0.05)
        self.entrada_buscar = tk.Entry(self.frame2)
        self.entrada_buscar.place(relx=0.50, rely=0.02, relwidth=0.25, relheight=0.05)

        self.image_visualizar = PhotoImage(file="img/olho.png")
        self.image_visualizar = self.image_visualizar.subsample(2,2)
        self.botao_delete = tk.Button(self.frame2, image=self.image_visualizar, bg="lightgray", command= self.busca_escala)
        self.botao_delete.place(relx=0.8, rely=0.02, relwidth=0.05, relheight=0.05)

        self.image_delete = PhotoImage(file="img/delete.png")
        self.image_delete = self.image_delete.subsample(2,2)
        self.btn_delete = tk.Button(self.frame2, image=self.image_delete, bg="lightgray",command= self.deleta_escala)
        self.btn_delete.place(relx=0.88, rely=0.02, relwidth=0.05, relheight=0.05)
        

        
        self.lista_escala = ttk.Treeview (self.frame2, height=3, column=("col_1","col_2","col_3","col_4")) 
        
        self.lista_escala.heading ("#0", text= "")
        self.lista_escala.heading ("#1",text="Nome Mês")
        self.lista_escala.heading ("#2",text="Data Inicial")
        self.lista_escala.heading ("#3",text="Data Final.")
        self.lista_escala.heading ("#4",text="CNPJ Empresa")
       
        
        

        self.lista_escala.column ("#0",width=1)
        self.lista_escala.column ("#1",width=99)
        self.lista_escala.column ("#2",width=80)
        self.lista_escala.column ("#3",width=80)
        self.lista_escala.column ("#4",width=80)
        
        

        self.lista_escala.place(relx=0.01,rely=0.08, relwidth=0.95,relheight=0.9)

        #barra de rolagem 
        self.rolagem_lista_escala=Scrollbar(self.frame2, orient="vertical")
        self.lista_escala.configure(yscroll= self.rolagem_lista_escala.set)
        self.rolagem_lista_escala.place(relx=0.97,rely=0.08, relwidth=0.015,relheight=0.9)

        self.lista_escala.bind("<<TreeviewSelect>>", self.click_escala)
        self.lista_escala.bind("<Double-1>", self.double_click)
        

    

    def get_escala(self):
        
        resp= self.controlador_banco.getEscala()
        if resp is None:
            messagebox.showinfo('Erro', 'Nenhuma Escala Cadastrada')
        else:
            self.lista_escala.delete(*self.lista_escala.get_children())
            for i in resp:
                self.lista_escala.insert("", tk.END, values=i)
        
    


    def click_escala(self, event):
        self.entrada_buscar.delete(0, tk.END)
        self.lista_escala.selection()
        for i in self.lista_escala.selection():
           
            col1,col2, col3, col4  = self.lista_escala.item(i, 'values')
            self.entrada_buscar.insert(tk.END,col1)
    def double_click(self, event):
        self.cadastro_escala()
       
              
    def cadastro_escala(self):
        self.list.destroy()
        TelaCadastroEscala()
        

    def deleta_escala(self):
        nome_mes= self.entrada_buscar.get()
        self.controlador_banco.excluirEscala(nome_mes)
        self.entrada_buscar.delete(0, tk.END)
        self.get_escala()

    def busca_escala(self):
        if self.entrada_buscar.get()=='':
            self.get_escala()
        else:
            self.lista_escala.delete(*self.lista_escala.get_children())
            nome_mes= self.entrada_buscar.get()
            busca_nome= self.controlador_banco.buscaEscala(nome_mes)
            if busca_nome is None:
                messagebox.showinfo('Erro', 'Nenhuma Escala Cadastrada')
            else:
                for i in busca_nome:
                    self.lista_escala.insert("",tk.END,values=i)
        
            self.entrada_buscar.delete(0, tk.END)
       
        
            


