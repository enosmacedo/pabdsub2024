class Escala:
    def __init__(self, nome, data_entrada, data_saida, hora_entrada, hora_saida, nome_emp):
        self.nome = nome
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.nome_emp = nome_emp

    def getNome(self):
        return self.nome

    def getDataEntrada(self):
        return self.data_entrada

    def getDataSaida(self):
        return self.data_saida

    def getHoraEntrada(self):
        return self.hora_entrada

    def getHoraSaida(self):
        return self.hora_saida

    def getNomeEmp(self):
        return self.nome_emp
    
    def setNome(self, nome):
        self.nome = nome

    def setDataEntrada(self, data_entrada):
        self.data_entrada = data_entrada

    def setDataSaida(self, data_saida):
        self.data_saida = data_saida

    def setHoraEntrada(self, hora_entrada):
        self.hora_entrada = hora_entrada

    def setHoraSaida(self, hora_saida):
        self.hora_saida = hora_saida

    def setNomeEmp(self, nome_emp):
        self.nome_emp = nome_emp
        