

class Empresa:
    
    
    def __init__(self, nome, cnpj, email, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def getCNPJ(self):
        return self.cnpj

    def getEmail(self):
        return self.email

    def getEndereco(self):
        return self.endereco
    
    def setNome(self, nome):
        self.nome = nome

    def setCNPJ(self, cnpj):
        self.cnpj = cnpj

    def setEmail(self, email):
        self.email = email

    def setEndereco(self, endereco):
        self.endereco = endereco
        
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

class Endereco:

    def __init__(self, numero, rua, bairro, cep):
        self.numero = numero
        self.rua = rua
        self.bairro = bairro
        self.cep = cep

    def getNumero(self):
        return self.numero

    def getRua(self):
        return self.rua

    def getBairro(self):
        return self.bairro

    def getCep(self):
        return self.cep
    
    def setNumero(self, numero):
        self.numero = numero

    def setRua(self, rua):
        self.rua = rua

    def setBairro(self, bairro):
        self.bairro = bairro

    def setCep(self, cep):
        self.cep = cep