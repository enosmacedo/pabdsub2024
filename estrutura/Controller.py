import psycopg2
from estrutura.Empresa import Empresa
from estrutura.Funcionario import Funcionario
from estrutura.Escala import Escala
from estrutura.Login import Login





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

    
    def cadastrar_func(self, cep, rua, bairro, num, cpf, nome, fone, email, cnpj):
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"WITH endereco_inserido AS (INSERT INTO endereco (cep, rua, bairro, numero)"
                                    f"VALUES ('{cep}', '{rua}', '{bairro}', {num} )"
                                    f"RETURNING id"
                                    f")"
                                    f"INSERT INTO funcionario (cpf, nome_func, telefone_func, email_func, endereco_func, emp_func)"
                                    f"SELECT '{cpf}', '{nome}', '{fone}', '{email}', id,  {cnpj} "
                                    f"FROM endereco_inserido;"
                            ) 
                self.conn.commit()
            
            except Exception as e:
                print('Erro ao cadastrar o funcionário:', e)
            finally:
                self.conn.close()
        
    def cadastrar_emp(self, cep, rua, bairro, num, cnpj, nome, fone, email):
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"WITH endereco_inserido AS (INSERT INTO endereco (cep, rua, bairro, numero)"
                                    f"VALUES ('{cep}', '{rua}', '{bairro}', {num} )"
                                    f"RETURNING id"
                                    f")"
                                    f"INSERT INTO empresa (cnpj, nome, telefone, email, endereco_emp,cpf_func)"
                                    f"SELECT '{cnpj}', '{nome}', '{fone}', '{email}', id "
                                    f"FROM endereco_inserido;"
                            ) 
                self.conn.commit()
            
            except Exception as e:
                print('Erro ao cadastrar o funcionário:', e)
            finally:
                self.conn.close()

    def get_password(self,usuario, senha):
        if self.conn is None:
            print("Crie a conexao primeiro")
        else:
            try:
                self.cursor=self.conn.cursor()
                self.cursor.execute(f"SELECT login,senha FROM usuario WHERE login = '{usuario}' AND senha = {senha}")
                resultado = self.cursor.fetchone()
                
                if resultado:
                    usuario, senha = resultado
                    resposta = Login(usuario, senha)
                    return resposta
                    
                else:
                    return None         
            except Exception as e:
                print('Erro: ', e)
            
            finally:
                if self.cursor:
                    self.cursor.close()
                
    def select_lista_escala(self,nome,data_entrada,data_saida,hora_entrada,hora_saida,nome_emp):
        try:
            #self.lista_escala.delete(*self.lista_escala.get_children())
            self.cursor=self.conn.cursor()
            self.cursor.execute("SELECT nome,data_entrada,data_saida,hora_entrada,hora_saida,nome_emp FROM escala ORDER BY nome ASC ; ")
            resultado= self.cursor.fetchall()
            if resultado:
                nome, data_entrada, data_saida, hora_entrada, hora_saida, nome_emp  = resultado
                resposta = Escala(nome, data_entrada, data_saida, hora_entrada, hora_saida, nome_emp)

            return resposta

        except Exception as e:
            print('Erro: ', e)

        finally:
            if self.cursor:
                self.cursor.close()



            
            for medico in var_lista_escala:
                self.lista_medico.insert('', tk.END, values=medico)

            
        except psycopg2.Error as e:
            print("ERRO")
        finally:
            if self.cursor:
                self.cursor.close()


