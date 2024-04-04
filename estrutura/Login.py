class Login:

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def getUsuario(self):
        return self.usuario

    def getSenha(self):
        return self.senha

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setSenha(self, senha):
        self.senha = senha