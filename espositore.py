# Classe Espositore

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
        self.__stand= None          # Parte associato a nessuno stand

    def __str__(self):
        return f'{self.__codice} {self.__nome} {self.__cognome}'

    # definisco per poter verificare le uguaglianze in base al codice
    def __eq__(self, other):
         if isinstance(other, Espositore):  # verifica che sia un espositore
             return self.__codice == other.__codice
         return False

    #metodi getter/setter per poter lavorare con gli attributi
    @property
    def stand(self):
        return self.__stand
    @stand.setter
    def stand(self, valore):
        self.__stand = valore
    @property
    def codice(self):
        return self.__codice