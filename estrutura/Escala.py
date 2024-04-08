class Escala:
    def __init__(self, nome_mes,data_inicial, data_final, cnpj_emp):
        self.nome_mes = nome_mes
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.cnpj_emp = cnpj_emp

    def getNome_mes(self):
        return self.nome_mes

    def getData_inicial(self):
        return self.data_inicial

    def getData_final(self):
        return self.data_final

    def getCnpj_emp(self):
        return self.cnpj_emp
    
    def setNome_mes(self, nome_mes):
        self.nome_mes = nome_mes

    def setData_inicial(self, data_inicial):
        self.data_inicial = data_inicial

    def setData_final(self, data_final):
        self.data_final = data_final

    def setCnpj_emp(self, cnpj_emp):
        self.cnpj_emp = cnpj_emp