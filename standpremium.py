from stand import Stand

# Classe figlia
class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__( codice, superficie, padiglione, prezzo)
        self.__posizione = posizione

    def __str__(self):
        return f'{super().__str__()} {self.__posizione}'

    # aggiorno il prezzo per gli stand premium
    @property
    def prezzo(self):
        return self.__prezzo * 1.30
