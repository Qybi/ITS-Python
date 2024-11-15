class ContoCorrente:
    def __init__(self, nome, conto, saldo):
        self.nome = nome
        self.conto = conto
        self.saldo = saldo

    def preleva(self, importo):
        self.saldo -= importo

    def deposita(self, importo):
        self.saldo += importo

    def descrizione(self):
        return f"Nome: {self.nome}, Conto: {self.conto}, Saldo: {self.saldo}"
    
cc = ContoCorrente("Mario Rossi", "0001", 1000)
print(cc.descrizione())
cc.preleva(100)
print(cc.descrizione())
cc.deposita(200)
print(cc.descrizione())