
class Funcionario:
    def __init__(self, nome, cpf, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

    def getNome(self):
        return self.nome
    
    def getCpf(self):
        return self.cpf
    
    def getEmail(self):
        return self.email
    
    def getEndereco(self):
        return self.endereco
    
    def setNome(self, nome):
        self.nome = nome
    
    def setCpf(self, cpf):
        self.cpf = cpf
    
    def setEmail(self, email):
        self.email = email
    
    def setEndereco(self, endereco):
        self.endereco = endereco