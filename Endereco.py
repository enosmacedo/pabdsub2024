

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