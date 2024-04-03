import psycopg2
import tkinter as tk
from estrutura.models import Endereco, Funcionario, Empresa,Login_emp
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
        self.cnpj_emp.delete(0,tk.END)
        self.nome_emp.delete(0,tk.END)
        self.fone_emp.delete(0,tk.END)
        self.email_emp.delete(0,tk.END)
        self.rua_emp.delete(0,tk.END)
        self.bairro_emp.delete(0,tk.END)
        self.num_emp.delete(0,tk.END)
        self.cep_emp.delete(0,tk.END)

    def limpa_variaveis_func(self):
        self.cpf_func.delete(0,tk.END)
        self.nome_func.delete(0,tk.END)
        self.fone_func.delete(0,tk.END)
        self.email_func.delete(0,tk.END)
        self.rua_func.delete(0,tk.END)
        self.bairro_func.delete(0,tk.END)
        self.num_func.delete(0,tk.END)
        self.cep_func.delete(0,tk.END)
        self.cnpj_func.delete(0,tk.END)

    def variaveis_func(self):
        self.cpf = self.cpf_func.get()
        self.nome = self.nome_func.get()
        self.fone = self.fone_func.get()
        self.email = self.email_func.get()
        self.rua = self.rua_func.get()
        self.bairro = self.bairro_func.get()
        self.num = self.num_func.get()
        self.cep = self.cep_func.get()
        self.cnpj = self.cnpj_func.get()

    def variaveis_emp(self):
        self.cnpj = self.cnpj_emp.get()
        self.nome = self.nome_emp.get()
        self.fone = self.fone_emp.get()
        self.email = self.email_emp.get()
        self.cep = self.cep_emp.get()
        self.rua = self.rua_emp.get()
        self.bairro = self.bairro_emp.get()
        self.num = self.num_emp.get()


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
                self.usuario = self.username_login.get()
                self.senha = self.password_login.get()

                self.cursor=self.conn.cursor()
                self.cursor.execute(f"SELECT * FROM login_emp WHERE usuario = '{self.usuario}' AND senha = '{self.senha}';")
                resultado = self.cursor.fetchall()
                
                if resultado:
                    self.janela_principal()
                    self.username_login.delete(0,tk.END)
                    self.password_login.delete(0,tk.END)
                    
                else:
                    self.message = messagebox.showinfo('Senha incorreta ou campos obrigatorios não preenchidos')  
                           
            except Exception as e:
                print("Erro ao criar tabela:", e)


