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

        