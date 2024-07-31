import psycopg2
from estrutura.Empresa import Empresa
from estrutura.Usuario import Usuario



class BDControlador:

    def __init__(self):
        self.conn = None

    def get_empresa(self, id_empresa):
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            cursor = self.conn.cursor()
            print("id_empresa "+ id_empresa)
            
            consulta = "SELECT nome, cnpj, email FROM empresa where nome = '" + str(id_empresa) + "';" 
            print(consulta)
            cursor.execute(consulta)
            
            resultado = cursor.fetchone()
            print("resultado: " + str(resultado))
            if resultado:
                nome, cnpj, email = resultado
                # return {"nome": nome, "cnpj": cnpj, "endereco": endereco}
                res = Empresa(nome, cnpj, email, None)
                print(res)
                return res 
            else:
                return "Empresa não encontrada."

            cursor.close()
            self.conn.close()


    def get_usuario(self, nome_usuario, nome_senha):
        if self.conn == None:
            print("Crie a conexao primeiro")
        else:
            cursor = self.conn.cursor()
            
            consulta = "SELECT * FROM usuario WHERE login  = '" + str(nome_usuario) + "';" 
            print(consulta)

            cursor.execute(consulta)            
            resultado = cursor.fetchone()
            
            print(resultado)
            if resultado:
                usuario, senha, cpf  = resultado
                if str(senha) == str(nome_senha):
                    usariobj = Usuario(usuario, senha)
                    return usariobj
                return None
            else:
                return "Usuario nao encontrado."

            cursor.close()
            self.conn.close()



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


