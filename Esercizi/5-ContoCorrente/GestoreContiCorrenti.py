from ContoCorrente import ContoCorrente

class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente: ContoCorrente, destinazione: ContoCorrente, importo: int):
        sorgente.preleva(importo)
        destinazione.deposita(importo)
        
c1 = ContoCorrente("Mario Rossi", "0001", 1000)
c2 = ContoCorrente("Luca Bianchi", "0002", 2000)

print(c1.descrizione())
print(c2.descrizione())

GestoreContiCorrenti.bonifico(c1, c2, 100)

print(c1.descrizione())
print(c2.descrizione())