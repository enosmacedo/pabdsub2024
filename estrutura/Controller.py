import psycopg2
import tkinter as tk
from models import Endereco, Funcionario, Empresa
import tkinter.messagebox as messagebox





class BDControlador:

    def __init__(self):
        self.conn = None

    def connect_database(self, databe_name, user_name, host_name, pass_, port_name):
        if self.conn == None:
            self.conn = psycopg2.connect(database = databe_name,
                                    user = user_name,
                                    host = host_name,
                                    password = pass_,
                                    port = port_name)
        else:
            print("Essa conexao existe... nao vou criar novamente" )

    def disconnect_dabase(self, conn):
        self.conn.close()

    def get_empresa(self, id_empresa):
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            cursor = self.conn.cursor()
            
            consulta = "SELECT nome, cnpj, email FROM empresa where cnpj = '" + str(id_empresa) + "';" 
            cursor.execute(consulta)
            
            resultado = cursor.fetchone()
            
            if resultado:
                nome, cnpj, email = resultado
                # return {"nome": nome, "cnpj": cnpj, "endereco": endereco}
                res = Empresa(nome, cnpj, email, None)
                return res 
            else:
                return "Empresa não encontrada."

            cursor.close()
            self.conn.close()

    def limpa_variaveis_emp(self):
        self.Empresa.cnpj.delete(0,tk.END)
        self.interface.nome_entry.delete(0,tk.END)
        self.interface.fone_entry.delete(0,tk.END)
        self.interface.email_entry.delete(0,tk.END)
        self.interface.rua_entry.delete(0,tk.END)
        self.interface.bairro_entry.delete(0,tk.END)
        self.interface.num_entry.delete(0,tk.END)
        self.interface.cep_entry.delete(0,tk.END)
        self.interface.cpf_entry.delete(0,tk.END)

    def limpa_variaveis_func(self):
        self.interface.cpf_entry.delete(0,tk.END)
        self.interface.nome_entry.delete(0,tk.END)
        self.interface.fone_entry.delete(0,tk.END)
        self.interface.email_entry.delete(0,tk.END)
        self.interface.rua_entry.delete(0,tk.END)
        self.interface.bairro_entry.delete(0,tk.END)
        self.interface.num_entry.delete(0,tk.END)
        self.interface.cep_entry.delete(0,tk.END)

    def variaveis_func(self):
        self.cpf = self.cpf_entry.get()
        self.nome = self.interface.nome_entry.get()
        self.fone = self.interface.fone_entry.get()
        self.email = self.interface.email_entry.get()
        self.rua = self.interface.rua_entry.get()
        self.bairro = self.interface.bairro_entry.get()
        self.num = self.interface.num_entry.get()
        self.cep = self.interface.cep_entry.get()
        self.cnpj = self.interface.cnpj_entry.get()

    def variaveis_emp(self):
        self.cnpj = self.interface.cnpj_entry.get()
        self.nome = self.interface.nome_entry.get()
        self.fone = self.interface.fone_entry.get()
        self.email = self.interface.email_entry.get()
        self.cep = self.interface.cep_entry.get()
        self.rua = self.interface.rua_entry.get()
        self.bairro = self.interface.bairro_entry.get()
        self.num = self.interface.num_entry.get()


    def cadastrar_func(self):
        self.variaveis_func()
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"WITH endereco_inserido AS (INSERT INTO endereco (cep, rua, bairro, numero)"
                                    f"VALUES ('{self.cep}', '{self.rua}', '{self.bairro}', {self.num} )"
                                    f"RETURNING id"
                                    f")"
                                    f"INSERT INTO funcionario (cpf, nome_func, telefone_func, email_func, endereco_func, emp_func)"
                                    f"SELECT '{self.cpf}', '{self.nome}', '{self.fone}', '{self.email}', id,  {self.cnpj} "
                                    f"FROM endereco_inserido;"
                            ) 
                self.conn.commit()
            
            except Exception as e:
                print('Erro ao cadastrar o funcionário:', e)
            finally:
                self.conn.close()
                self.limpa_variaveis_func()
        
    def cadastrar_emp(self):
        self.variaveis_emp()
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"WITH endereco_inserido AS (INSERT INTO endereco (cep, rua, bairro, numero)"
                                    f"VALUES ('{self.cep}', '{self.rua}', '{self.bairro}', {self.num} )"
                                    f"RETURNING id"
                                    f")"
                                    f"INSERT INTO empresa (cnpj, nome, telefone, email, endereco_emp,cpf_func)"
                                    f"SELECT '{self.cnpj}', '{self.nome}', '{self.fone}', '{self.email}', id "
                                    f"FROM endereco_inserido;"
                            ) 
                self.conn.commit()
            
            except Exception as e:
                print('Erro ao cadastrar o funcionário:', e)
            finally:
                self.conn.close()
                self.limpa_variaveis_emp()

    def login_emp(self):
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            try:
                self.usuario = self.interface.username_entry.get()
                self.senha = self.interface.password_entry.get()

                self.cursor=self.conn.cursor()
                self.cursor.execute(f"SELECT * FROM login_emp WHERE usuario = '{self.usuario}' AND senha = '{self.senha}';")
                resultado = self.cursor.fetchall()
                
                if resultado:
                    self.interface.janela_cadastro_func()
                    self.interface.username_entry.delete(0,tk.END)
                    self.interface.password_entry.delete(0,tk.END)
                    
                else:
                    self.message = messagebox.showinfo('Senha incorreta oucampos obrigatorios não preenchidos')  
                           
            except Exception as e:
                print("Erro ao criar tabela:", e)


