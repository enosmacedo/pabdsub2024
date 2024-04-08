class Usuario:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def getlogin(self):
        return self.login

    def getSenha(self):
        return self.senha

    def setLogin(self, login):
        self.login = login

    def setSenha(self, senha):
        self.senha = senha