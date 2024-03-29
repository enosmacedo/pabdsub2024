import psycopg2
import tkinter as tk

def connect_database(databe_name, user_name, host_name, pass_, port_name):
    conn = psycopg2.connect(database = databe_name,
             	            user = user_name,
                             host = host_name,
                             password = pass_,
                             port = port_name)
    return conn

def limpa_variaveis_emp(self):
    self.cnpj_entry.delete(0,tk.END)
    self.nome_entry.delete(0,tk.END)
    self.fone_entry.delete(0,tk.END)
    self.email_entry.delete(0,tk.END)
    self.rua_entry.delete(0,tk.END)
    self.bairro_entry.delete(0,tk.END)
    self.num_entry.delete(0,tk.END)
    self.cep_entry.delete(0,tk.END)
    self.cpf_entry.delete(0,tk.END)

def limpa_variaveis_func(self):
    self.cpf_entry.delete(0,tk.END)
    self.nome_entry.delete(0,tk.END)
    self.fone_entry.delete(0,tk.END)
    self.email_entry.delete(0,tk.END)
    self.rua_entry.delete(0,tk.END)
    self.bairro_entry.delete(0,tk.END)
    self.num_entry.delete(0,tk.END)
    self.cep_entry.delete(0,tk.END)

def variaveis_func(self):
    self.cpf = self.cpf_entry.get()
    self.nome = self.nome_entry.get()
    self.fone = self.fone_entry.get()
    self.email = self.email_entry.get()
    self.rua = self.rua_entry.get()
    self.bairro = self.bairro_entry.get()
    self.num = self.num_entry.get()
    self.cep = self.cep_entry.get()
    self.cnpj = self.cnpj_entry.get()

def variaveis_emp(self):
    self.cnpj = self.cnpj_entry.get()
    self.nome = self.nome_entry.get()
    self.fone = self.fone_entry.get()
    self.email = self.email_entry.get()
    self.cep = self.cep_entry.get()
    self.rua = self.rua_entry.get()
    self.bairro = self.bairro_entry.get()
    self.num = self.num_entry.get()


def cadastrar_func(self):
    self.variaveis_func()
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
    self.cadastro_func()

