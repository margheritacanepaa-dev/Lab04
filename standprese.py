from stand import Stand

# Classe figlia
class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, prese):
        super().__init__( codice, superficie, padiglione, prezzo)
        self.__prese = prese

    def __str__ (self):
        return f'{super().__str__()} {self.__prese}'

    # aggiorno il prezzo per gli stand con prese
    @property
    def prezzo(self):
        return self.__prezzo*(1+0.07*self.__prese)

