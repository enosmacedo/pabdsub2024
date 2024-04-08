class Funcionario:

    def __init__(self, nome, cpf, email,cargo, endereco):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cargo = cargo
        self.endereco = endereco

    def getNome(self):
        return self.nome
    
    def getCpf(self):
        return self.cpf
    
    def getEmail(self):
        return self.email
    
    def getCargo(self):
        return self.cargo
    
    def getEndereco(self):
        return self.endereco
    
    def setNome(self, nome):
        self.nome = nome
    
    def setCpf(self, cpf):
        self.cpf = cpf
    
    def setEmail(self, email):
        self.email = email

    def setCargo(self, cargo):
        self.cargo = cargo
    
    def setEndereco(self, endereco):
        self.endereco = endereco
