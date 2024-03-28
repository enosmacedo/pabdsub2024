import psycopg2
from estrutura.BDControlador import BDControlador
from estrutura.Empresa import Empresa
from color_interface import *
import tkinter as tk


if __name__ == '__main__':
    databe_name = "vigilancia.com"
    user_name = "postgres"
    host_name = "localhost" 
    pass_ = "@Edi170380"
    port_name = 5432

    controlador_banco = BDControlador()
    controlador_banco.connect_database(databe_name, user_name, host_name, pass_, port_name)

    

    login = tk.Tk()
    login.title("Login")
    login.configure(background= cor_fundo_login)
    login.minsize(400, 300)
    login.resizable(False, False)
    larg_login = login.winfo_reqheight()
    aut_login = login.winfo_reqwidth()
    larg_tela = login.winfo_screenwidth()
    alt_tela = login.winfo_screenheight()
    pos_x = (larg_tela // 2) - (larg_login // 2)
    pos_y = (alt_tela // 2) - (aut_login // 2)
    login.geometry(f"{larg_login}x{aut_login}+{larg_tela//2}+{alt_tela//2}")

    username_label=tk.Label(login, text="Usuario",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
    username_label.place(relx=0.42, rely=0.2 ,relwidth=0.15, relheight=0.1)
    username_entry=tk.Entry(login, bg= cor_entry, fg=cor_letra_login, border=1,  font=("Arial", 12))
    username_entry.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.08)


    password_label=tk.Label(login, text="Senha",bg= cor_fundo_login, fg=cor_letra_login, font=("Arial", 12))
    password_label.place(relx=0.42, rely=0.4, relwidth=0.15, relheight=0.1)
    password_entry=tk.Entry(login, bg= cor_entry, fg=cor_letra_login, font=("Arial", 12), show="*")
    password_entry.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.08)

    btn=tk.Button(login, text="Entrar", bg= cor_fundo_login, fg="white", font=("Arial", 12))
    btn.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.1)
    

    
    login.mainloop()















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
