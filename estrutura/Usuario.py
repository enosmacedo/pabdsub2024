class Usuario:

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha  = senha
    

    def validate_login(self, usuario_comparacao, senha_comparacao ):
        if (self.usuario == usuario_comparacao) and (self.senha == senha_comparacao):
            return True

        return False
