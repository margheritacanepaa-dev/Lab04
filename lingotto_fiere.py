import csv
from stand import Stand
from standprese import StandPrese
from standpremium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        self.__nome= nome
        self.__stand = []       # creo delle strutture dati per memorizzare stand e espositori
        self.__espositori = []

    def __str__(self):
        return f"{self.__nome} {self.__stand} {self.__espositori}"

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome= nome


    # funzione per caricare i dati del file all'interno della classe
    def carica_file_dati(self, file_path):
        try:
            with open(file_path) as file:
                reader = csv.reader(file)
                for row in reader:
                    codice= row[0]
                    if codice.startswith('ST'):
                        sup=row[1]
                        padigl = row[2]
                        prez = row[3]

                        if len(row) > 4:          # se c'è anche un altro campo, sono stand speciali
                            if row[4].isdigit():
                                prese= row[4]
                                stand_con_prese= StandPrese(codice, sup, padigl, prez, prese)
                                self.__stand.append(stand_con_prese)
                            elif row[4].isalpha():
                                posizione= row[4]
                                stand_premium = StandPremium(codice, sup, padigl, prez, posizione)
                                self.__stand.append(stand_premium)
                        else:
                            stand_standard = Stand(codice, sup, padigl, prez)
                            self.__stand.append(stand_standard)
                # aggiungo tutti gli stand alla stessa lista (sarà formata da diversi tipi di oggetti)

                    if codice.startswith('E'):
                        nome= row[1]
                        cognome= row[2]
                        espositore = Espositore(codice, nome, cognome)
                        self.__espositori.append(espositore)

        except FileNotFoundError:
            print("File non trovato")


    # Assegnazione di uno stand all'espositore, se disponibili
    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        stand_trovato= None
        for s in self.__stand:          # controllo se lo stand esiste
            if s.codice == codice_stand:
                stand_trovato = s
        if stand_trovato == None:
            raise ValueError (f"{codice_stand} non trovato")

        espositore_trovato= None
        for e in self.__espositori:         # controllo se l'espositore esiste
            if e.codice == codice_espositore:
                espositore_trovato = e
        if espositore_trovato == None:
            raise ValueError (f"{codice_espositore} non trovato")

        # Controllo delle disponibilità e associazioni
        if not stand_trovato.disponibile:
            raise ValueError(f"Lo stand {codice_stand} non è disponibile.")  # se non è disponibile

        if espositore_trovato.stand is not None:
            raise ValueError(f"L'espositore {codice_espositore} ha già uno stand.")  # se ha già uno stand

        # se non si sollevano ecceziini, faccio finalmente l'associazione
        stand_trovato.disponibile = False
        stand_trovato.espositore = espositore_trovato
        espositore_trovato.stand = stand_trovato


    # Elenco degli espositori con lo stand associato (se presente)
    def elenca_espositori(self):
        print("Elenco espositori: ")
        for e in self.__espositori:
            if e.stand is not None:    # se c'è uno stand associato, stampo entrambi
                print(f"Espositore: {e.codice}, assegnato allo stand: {e.stand.codice}") # stand è oggetto con codice
            else:
                print(f"Espositore: {e.codice}")


    # Elenco degli stand ordinati in base al prezzo.
    def stand_ordinati_per_prezzo(self):
        return sorted(self.__stand)    # li ordina in base al prezzo grazie al metodo di ordinamento della classe
