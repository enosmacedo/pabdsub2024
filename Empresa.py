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