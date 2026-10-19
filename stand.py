# Classe Stand base
class Stand:
    def __init__(self,codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = int(superficie)
        self.__padiglione = padiglione
        self.__prezzo = int(prezzo)
        self.__disponibile = True      # Lo stand parte come disponibile
        self.__espositore= None        # Lo stand parte con nessun espositore associato

    # definisco per stampare
    def __str__(self):
        return f"{self.__codice} {self.__padiglione} {self.__prezzo}"

    # definisco per poter verificare le uguaglianze in base al codice
    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.__codice == other.__codice     # 2 stand sono uguali se hanno il codice uguale
        return False

    # definisco per fare confronti di ordinamento in base al prezzo
    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.__prezzo < other.__prezzo
        return False

    # metodi getter e setter per poter lavorare con attributi privati
    @property
    def prezzo(self):
        return self.__prezzo
    @property
    def codice(self):
        return self.__codice
    @property
    def disponibile(self):
        return self.__disponibile
    @disponibile.setter
    def disponibile(self, valore):
        self.__disponibile = valore
    @property
    def espositore(self):
        return self.__espositore
    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore