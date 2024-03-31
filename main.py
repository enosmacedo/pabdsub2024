import psycopg2
from estrutura.BDControlador import BDControlador
from estrutura.Empresa import Empresa
from estrutura.Endereco import Endereco
from estrutura.Funcionario import Funcionario
from color_interface import *
from tkinter import * 

class Interface:
    def __init__(self,login):
    
        self.login = login
        self.controla_banco()
        self.janela_login()

    def controla_banco(self):

        self.databe_name = "vigilancia.com"
        self.user_name = "postgres"
        self.host_name = "localhost" 
        self.pass_ = "@Edi170380"
        self.port_name = 5432

        self.controlador_banco = BDControlador()
        self.controlador_banco.connect_database(self.databe_name, self.user_name, self.host_name, self.pass_, self.port_name)

    def janela_login(self,):
    
        self.login.title("Login")
        self.login.configure(background= cor_fundo_login)
        self.login.minsize(400, 300)
        self.login.resizable(False, False)
        
        nome_emp = Label(self.login, text="Vigilância.com", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 20))
        nome_emp.place(relx=0.09, rely=0.03, relwidth=0.8, relheight=0.20)

        self.username_label=Label(self.login, text="Usuário",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
        self.username_label.place(relx=0.42, rely=0.2 ,relwidth=0.15, relheight=0.1)
        self.username_entry=Entry(self.login, bg= cor_entry, fg=cor_letra_entry_login, border=1,  font=("Arial", 12))
        self.username_entry.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.08)


        self.password_label=Label(self.login, text="Senha",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
        self.password_label.place(relx=0.42, rely=0.4, relwidth=0.15, relheight=0.1)
        self.password_entry=Entry(self.login, bg= cor_entry, fg=cor_letra_entry_login, font=("Arial", 12), show="*")
        self.password_entry.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.08)
        self.btn=Button(self.login, text="Entrar", bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
        self.btn.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.1)
    

    def cadastro_func(self):
        self.cad_func = Toplevel()
        self.cad_func.minsize(1200, 800)
        self.cad_func.resizable(False, False)
        self.cad_func.title('Cadastro de Funcionários')
        self.cad_func.configure(background='gray')
        self.cad_func.transient(root)
        self.cad_func.focus_force()
        self.cad_func.grab_set()  
    
        self.frame1 = Frame(self.cad_func, bg='lightgray', borderwidth=2, relief='raised')
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        self.frame2 = Frame(self.cad_func, bg='lightgray', borderwidth=2, relief='raised')
        self.frame2.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.80)

        self.lbl = Label(self.frame1, text='Vigilancia.com', bg='lightgray', font='arial 40 bold')
        self.lbl.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.70)

        self.lbl = Label(self.frame2, text='Cadastro de Empresas ', bg='lightgray', font='arial 20 bold')
        self.lbl.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.10)

        self.lbl_cnpj = Label(self.frame2, text='CNPJ:', bg='lightgray')
        self.lbl_cnpj.place(relx=0.03, rely=0.25, relwidth=0.1, relheight=0.05)
        self.cnpj_entry = Entry(self.frame2)
        self.cnpj_entry.place(relx=0.12, rely=0.25, relwidth=0.20, relheight=0.05)

        self.lbl_fone = Label(self.frame2, text='Fone:', bg='lightgray')
        self.lbl_fone.place(relx=0.03, rely=0.32, relwidth=0.1, relheight=0.05)
        self.fone_entry = Entry(self.frame2)
        self.fone_entry.place(relx=0.12, rely=0.32, relwidth=0.20, relheight=0.05)

        self.lbl_email = Label(self.frame2, text='E-mail:', bg='lightgray')
        self.lbl_email.place(relx=0.03, rely=0.39, relwidth=0.1, relheight=0.05)
        self.email_entry = Entry(self.frame2)
        self.email_entry.place(relx=0.12, rely=0.39, relwidth=0.20, relheight=0.05)

        self.lbl_nome = Label(self.frame2, text='Nome:', bg='lightgray')
        self.lbl_nome.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.05)
        self.nome_entry = Entry(self.frame2)
        self.nome_entry.place(relx=0.43, rely=0.25, relwidth=0.42, relheight=0.05)

        self.lbl_rua = Label(self.frame2, text='Rua:', bg='lightgray')
        self.lbl_rua.place(relx=0.35, rely=0.32, relwidth=0.1, relheight=0.05)
        self.rua_entry = Entry(self.frame2)
        self.rua_entry.place(relx=0.43, rely=0.32, relwidth=0.4, relheight=0.05)

        self.lbl_num = Label(self.frame2, text='Nº:', bg='lightgray')
        self.lbl_num.place(relx=0.68, rely=0.32, relwidth=0.1, relheight=0.05)
        self.num_entry = Entry(self.frame2)
        self.num_entry.place(relx=0.75, rely=0.32, relwidth=0.1, relheigh=0.05)

        self.lbl_bairro = Label(self.frame2, text='Bairro:', bg='lightgray')
        self.lbl_bairro.place(relx=0.35, rely=0.39, relwidth=0.1, relheight=0.05)
        self.bairro_entry = Entry(self.frame2)
        self.bairro_entry.place(relx=0.43, rely=0.39, relwidth=0.40, relheight=0.05)

        self.lbl_cep = Label(self.frame2, text='CEP:', bg='lightgray')
        self.lbl_cep.place(relx=0.68, rely=0.39, relwidth=0.1, relheight=0.05)
        self.cep_entry = Entry(self.frame2)
        self.cep_entry.place(relx=0.75, rely=0.39, relwidth=0.1, relheight=0.05)

        self.cnpj_entry = Label(self.frame2, text='CNPJ:', bg='lightgray')
        self.cnpj_entry.place(relx=0.03, rely=0.5, relwidth=0.1, relheight=0.05)
        self.cnpj_entry = Entry(self.frame2)
        self.cnpj_entry.place(relx=0.12, rely=0.5, relwidth=0.20, relheight=0.05)

            
        self.btn = Button(self.frame2, text='Cadastrar', bg='gray', fg='white', font='arial 10 bold')
        self.btn.place(relx=0.80, rely=0.75, relwidth=0.10, relheight=0.05)
    



if __name__ == '__main__':
    root=Tk()
    App=Interface(root)
    root.mainloop()















# if __name__ == '__main__':
    # conn = connect_database("ticketcontroller", "postgres", "localhost", "postgres", 5432)
    # # create_table(conn, "teste4", [("id", "SERIAL PRIMARY KEY"), ("rg", "INTEGER")  ])

    # update_element(conn, "teste4", ("id", "12"), [("rg", "100")])
    # select_elements(conn, "teste4", ("id", "12"), ["rg"])
    # select_all_elements(conn, "teste4", ["rg"])

    # delete_element(conn, "teste4", ("id", "12"))

    # disconnect_dabase(conn)


    # Create the main window
    # root = tk.Tk()
    # root.title("Label and Button Example")

    # # Create a label widget
    # label = tk.Label(root, text="Tkinter Exercises (Label Text)")
    # label.pack(padx=20, pady=20)

    # # Create a button widget
    # button = tk.Button(root, text="Click Me", command=change_label_text)
    # button.pack()

    # # Start the Tkinter main loop
    # root.mainloop()
    
###########################################################

# def connect_database(databe_name, user_name, host_name, pass_, port_name):
#     conn = psycopg2.connect(database = databe_name,
#             	            user = user_name,
#                             host = host_name,
#                             password = pass_,
#                             port = port_name)
#     return conn


# def disconnect_dabase(conn):
#     conn.close()


# def create_table(conn, name_table, params):
#     cmd_sql = "CREATE TABLE " + name_table + "("
#     for index, p in enumerate(params):
#         if index == len(params) -1 :
#             cmd_sql = cmd_sql + p[0] + " " + p[1] 
#         else:
#             cmd_sql = cmd_sql + p[0] + " " + p[1] + ", "
#     cmd_sql = cmd_sql + ")"

#     cur = conn.cursor()
#     try:
#         cur.execute(cmd_sql)
#     except:
#         print("Nao consegui criar a tabela")
#     conn.commit()
#     cur.close()


# def connect_database(databe_name, user_name, host_name, pass_, port_name):
#     conn = psycopg2.connect(database = databe_name,
#             	            user = user_name,
#                             host = host_name,
#                             password = pass_,
#                             port = port_name)
#     return conn


# def disconnect_dabase(conn):
#     conn.close()


# def create_table(conn, name_table, params):
#     cmd_sql = "CREATE TABLE " + name_table + "("
#     for index, p in enumerate(params):
#         if index == len(params) -1 :
#             cmd_sql = cmd_sql + p[0] + " " + p[1] 
#         else:
#             cmd_sql = cmd_sql + p[0] + " " + p[1] + ", "
#     cmd_sql = cmd_sql + ")"

#     cur = conn.cursor()
#     try:
#         cur.execute(cmd_sql)
#     except:
#         print("Nao consegui criar a tabela")
#     conn.commit()
#     cur.close()


# def insert_element(conn, name_table, params):
#     cmd_sql_colunas = "INSERT INTO " + name_table + "("
#     cmd_sql_values  = " VALUES ("

#     for index_vetor_params, single_param in enumerate(params):
#         if index_vetor_params == len(params) - 1:
#             cmd_sql_colunas += single_param[0] + ") "
#             cmd_sql_values += single_param[1] + ") "
#         else:
#             cmd_sql_colunas += single_param[0] + ", "
#             cmd_sql_values += single_param[1] + ", "

#     cmd_sql = cmd_sql_colunas + cmd_sql_values

#     cursor = conn.cursor()
#     try:
#         cursor.execute(cmd_sql)
#         print(cmd_sql)
#         print("Dados inseridos")
#     except Exception as e:
#         print(f"Falha: {e}")
#     finally:
#         conn.commit()
#         cursor.close()


# def update_element(conn, name_table, condicional, params):
#     cmd_sql_colunas = "UPDATE " + name_table + " SET "

#     for index_vetor_params, single_param in enumerate(params):
#         cmd_sql_colunas += single_param[0] + "=" + single_param[1]
#         if index_vetor_params != len(params) - 1: #o ultimo elmento
#             cmd_sql_colunas += ", "

#     cmd_sql = cmd_sql_colunas + " WHERE " + condicional[0] + " = " + condicional[1] 

#     cursor = conn.cursor()
#     try:
#         cursor.execute(cmd_sql)
#         print(cmd_sql)
#     except Exception as e:
#         print(f"Falha: {e}")
#     finally:
#         conn.commit()
#         cursor.close()


# def select_elements(conn, name_table, condicional, params):
#     cmd_sql = "SELECT "
#     for index_vetor_params, single_param in enumerate(params):
#         cmd_sql += single_param
#         if index_vetor_params != len(params) - 1: #nao for o ultimo elmento
#             cmd_sql += ", "

#     cmd_sql += " FROM " + name_table + " WHERE "  + condicional[0] + " = " + condicional[1] 

#     cursor = conn.cursor()
#     try:
#         cursor.execute(cmd_sql)
#         print(cmd_sql)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Falha: {e}")
#     finally:
#         conn.commit()
#         cursor.close()


# def select_all_elements(conn, name_table, params):
#     cmd_sql = "SELECT "
#     for index_vetor_params, single_param in enumerate(params):
#         cmd_sql += single_param
#         if index_vetor_params != len(params) - 1: #nao for o ultimo elmento
#             cmd_sql += ", "

#     cmd_sql += " FROM " + name_table

#     cursor = conn.cursor()
#     try:
#         cursor.execute(cmd_sql)
#         print(cmd_sql)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Falha: {e}")
#     finally:
#         conn.commit()
#         cursor.close()


# def delete_element(conn, name_table, condicional):
#     cmd_sql = "DELETE FROM " + name_table + " WHERE "  + condicional[0] + " = " + condicional[1] 

#     cursor = conn.cursor()
#     try:
#         cursor.execute(cmd_sql)
#         print(cmd_sql)
#     except Exception as e:
#         print(f"Falha: {e}")
#     finally:
#         conn.commit()
#         cursor.close()


# Function to change the label text
# def change_label_text(id):
