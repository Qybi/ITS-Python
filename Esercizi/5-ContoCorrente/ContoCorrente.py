from Conto import Conto

class ContoCorrente(Conto):
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value):
        self.__saldo = value
    
    def __init__(self, nome, conto, saldo):
        super().__init__(nome, conto)
        self.__saldo = saldo

    def preleva(self, importo):
        self.saldo -= importo

    def deposita(self, importo):
        self.saldo += importo

    def descrizione(self):
        return f"Nome: {self.nome}, Conto: {self.conto}, Saldo: {self.saldo}"