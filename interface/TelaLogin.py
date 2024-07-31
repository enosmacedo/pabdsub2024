import sys
import os
import psycopg2
from estrutura.Empresa import Empresa
from estrutura.BDControlador import BDControlador
import tkinter as tk
import Constants

textUsuario = None
textSenha = None
label_res = None

def buttonPress():
    global textUsuario
    global textSenha
    global label_res
    print("Button Pressed!!")

    usuario = textUsuario.get()
    senha   = textSenha.get()

    controlador_banco = BDControlador()
    controlador_banco.connect_database(Constants.databe_name, Constants.user_name, Constants.host_name, Constants.pass_,  Constants.port_name)

    usuario = controlador_banco.get_usuario(usuario, senha)
    print(usuario)
    
    if (usuario == None) or (usuario == "Usuario nao encontrado."):
        label_res.config(text="Login errado")
    else:
        label_res.config(text="Login Certo")
    



def textBox():
    print(textb.get())
    
def slideValue():
    print (Slider.get())


def run_tela():
    global textUsuario
    global textSenha
    global label_res

    mywindow = tk.Tk()
    #Label
    label = tk.Label(mywindow, text="Faça seu login")
    label.grid(row=0,column=1)

    textUsuario = tk.Entry(mywindow,text="Usuário")
    textUsuario.grid(row=1,column=1)

    textSenha = tk.Entry(mywindow,text="Senha")
    textSenha.grid(row=2,column=1)
    

    label_res = tk.Label(mywindow, text="")
    label_res.grid(row=3,column=1)

    button = tk.Button(mywindow,text='Log in!',command=buttonPress)
    button.grid(row=4,column=1)


    mywindow.mainloop()











