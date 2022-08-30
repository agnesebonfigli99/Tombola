#  Developer: $ Lavinia
# -*- coding: utf-8 -*-

# Implementazione classe Cartella


"""
Classe Cartella con attibuti:

-cartella: matrice di dimensioni 3x9 inizialmente contenente tutti 0; in seguito sono inseriti in 15 posizioni i numeri randomici

compresi tra 1 e 90 rispettando le specifiche

-contatore_elem_c: vettore riga di dimensione 1x9 inizlamente inizializzato a 0, incrementato di 1 per ogni numero aggiunto sulla rispettiva

colonna e decerementato di 1 se eliminato

-contatore_elem_r: vettore colonna di dimensione 3x1 inizlamente inizializzato a 0, incrementato di 1 per ogni numero aggiunto sulla rispettiva

riga e decerementato di 1 se eliminato

"""

import numpy as np


class Cartella:

    def __init__(self, cartella=None, contatore_elem_c=None, contatore_elem_r=None):

        self.cartella = np.zeros((3, 9))

        self.contatore_elem_c = np.zeros((1, 9))

        self.contatore_elem_r = np.zeros((3, 1))

    """ Metodo incrementa_contatore: metodo che aggiorna (incrementando) i contatori rispettivamente degli elementi sulle righe e sulle colonne
        ogni qual volta viene aggiunto un nuovo numero """

    def incrementa_contatore(self, i_riga, i_colonna):

        #i_riga: indice della riga (int)

        #i_colonna=indice della colonna (int)

        self.contatore_elem_r[i_riga] += 1

        self.contatore_elem_c[i_colonna] += 1

    """
    Metodo decrementa_contatore: metodo che aggiorna (decrementando) i contatori rispettivamente degli elementi sulle righe e sulle colonne

    ogni qual volta viene rimosso un numero
    """

    def decrementa_contatore(self, i_riga, i_colonna):

        self.contatore_elem_r[i_riga] -= 1

        self.contatore_elem_c[i_colonna] -= 1

    """
    Metodo aggiungi_numero: metodo che inserisce un numero nella cartella nella posizione specificata gli indici di riga e colonna,
    e per ogni elemento aggiunto utilizza il metodo incrementa_contatore
    """

    def aggiungi_numero(self, i_riga, i_colonna, num):

        "num (int): numero inserito"

        self.cartella[i_riga, i_colonna] = num

        self.incrementa_contatore(i_riga, i_colonna)

    """
    Metodo rimuovi_numero: metodo che rimuove un numero nella cartella nella posizione specificata gli indici di riga e colonna,
    e per ogni elemento aggiunto utilizza il metodo decrementa_contatore
    """

    def rimuovi_numero(self, i_riga, i_colonna):

        self.cartella[i_riga, i_colonna] = 0

        self.decrementa_contatore(i_riga, i_colonna)

    def azzera_contatore(self):

        self.contatore_elem_c = np.zeros((1, 9))

        self.contatore_elem_r = np.zeros((3, 1))

    """
    Metodo visualizza_elem_cartella: metodo che restituisce l'elemento (int) presente nella cartella che si trova nella posizione
    individuata dell'indice della riga e della colonna
    """

    def visualizza_elem_cartella(self, i_riga, i_colonna):

        elemento = self.cartella[i_riga, i_colonna]

        return elemento

    """
    Metodo inializza_contatori: metodo che rinizializza i contatori degli elementi su righe e colonne azzerandoli
    """

    def inizializza_contatori(self):

        self.contatore_elem_c = np.zeros((1, 9))

        self.contatore_elem_r = np.zeros((3, 1))

    """
    Metodo check_vincolo_col: metodo che verifica che sia rispettata la specifica sulle colonne --> da 1 a 3 elementi su ognuna
    restituisce in output un booleano (True se la condizione è verificata, False altrimenti)
    """

    def check_vincolo_col(self, i_colonna):

        if self.contatore_elem_c[i_colonna] >= 1:

            return True

        else:

            return False

    """
    Metodo check_vincolo_r:metodo che verifica che sia rispettata la specifica sulle righe --> 5 elementi su ognuna
    restituisce in output un booleano (True se la condizione è verificata, False altrimenti)
    """

    def check_vincolo_r(self, i_riga):

        if self.contatore_elem_r[i_riga] == 5:

            return True

        else:

            return False

    """
    Metodo casella_vuota: metodo che controlla se la casella individuata da indice riga e indice colonna è vuota, ricordiamo che
    nel programma una caseslla libera contiene il numero -1
    Restituisce in output un booleano: True: --> se la casella è vuota
    """

    def casella_vuota(self, i_riga, i_colonna):

        if self.visualizza_elem_cartella(i_riga, i_colonna) == -1:

            return True

        else:

            return False

    """
    Metodo casella_occuppata: metodo che controlla se la casella individuata da indice riga e indice colonna è occupata, se la
    casella è occupata conterrà un numero da 1 a 90 oppure 0 (numero estratto)
    Restituisce un boolenano: True--> se la casella è occupata
    """

    def casella_occupata(self, i_riga, i_colonna):

        if self.visualizza_elem_cartella(i_riga, i_colonna) != -1:

            return True

        else:

            return False

    
    """Metodo mostra_cartella: metodo che restituisce la cartella al fine di visualizzarla"""
    

    def mostra_cartella(self):

        return self.cartella

    """
    Metodo numero_estratto: metodo che restituisce un booleano al fine di controllare se il numero nella posizione specificata
    da indice riga e indice colonna è già stato estratto
    True--> numero estratto (=0 per convenzione del programma)
    """

    def numero_estatto(self, i_riga, i_colonna):

        if self.cartella[i_riga][i_colonna] == 0:

            return True

        else:

            return False
