import database.DB_connect
from flet.core.list_view import ListView
from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''
class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:

        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        risultato=[]
        cnx = database.DB_connect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT * FROM automobile"""
        cursor.execute(query)
        for row in cursor:
            auto=Automobile(codice=row['codice'],
                            marca=row['marca'],
                            modello=row['modello'],
                            anno=row['anno'],
                            posti=row['posti'],
                            disponibile=row['disponibile'])
            risultato.append(auto)
        cursor.close()
        cnx.close()
        return risultato


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        risultato=[]
        cnx=database.DB_connect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT *
                 FROM automobile 
                 WHERE modello LIKE %s;"""
        cursor.execute(query,(f'%{modello}%',))

        for row in cursor:
            auto=Automobile(codice=row['codice'],
                            marca=row['marca'],
                            modello=row['modello'],
                            anno=row['anno'],
                            posti=row['posti'],
                            disponibile=row['disponibile'])
            risultato.append(auto)
        cursor.close()
        cnx.close()
        return risultato

