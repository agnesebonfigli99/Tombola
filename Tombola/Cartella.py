#  Developer: $ Lavinia
# -*- coding: utf-8 -*-

"""
Classe Cartella: creazione di un modello di cartella.
N.B: di seguito sarà usata la convenzione per cui se una casella della cartella è vuota (non contiene nessun numero) sarà contrassegnata con il numero 0,
se la casella contiene un numero che però è
già stato estratto al posto di tale numero conterrà -1 (casella abbassata)

Attibuti:
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

        self.contatore_elem_c = np.zeros((1,9))

        self.contatore_elem_r = np.zeros((3, 1))

    "Una volta creata la cartella come matrice di zeri, "

    """ Metodo incrementa_contatore: metodo che aggiorna (incrementando) i contatori rispettivamente degli elementi sulle righe e sulle colonne
        ogni qual volta viene aggiunto un nuovo numero """

    def incrementa_contatore(self, i_riga, i_colonna):

        # i_riga: indice della riga (int)

        # i_colonna=indice della colonna (int)

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
    nel programma una caseslla libera contiene il numero 0
    Restituisce in output un booleano: True: --> se la casella è vuota
    """

    def casella_vuota(self, i_riga, i_colonna):

        if self.visualizza_elem_cartella(i_riga, i_colonna) == 0:

            return True

        else:

            return False

    """
    Metodo casella_occuppata: metodo che controlla se la casella individuata da indice riga e indice colonna è occupata, se la
    casella è occupata conterrà un numero da 1 a 90 oppure -1 (numero estratto)
    Restituisce un boolenano: True--> se la casella è occupata
    """

    def casella_occupata(self, i_riga, i_colonna):

        if self.visualizza_elem_cartella(i_riga, i_colonna) !=0:

            return True

        else:

            return False

    """Metodo mostra_cartella: metodo che restituisce la cartella al fine di visualizzarla"""

    def mostra_cartella(self):

        return self.cartella


    """
    Metodo canc_cartella_tale metodo rende nuovamente la cartella una matrice di zeri e azzera i contatori
    """
    def canc_cartella(self):
        self.cartella = np.zeros((3,9))
        self.azzera_contatore()

    """
    metodo posizione_libera_colonna:restituisce in una lista gli indici delle posizioni libere per riga.
    """
    def posizione_libera_colonna(self,i):
        indici=[]
        for j in range(9):
            if self.cartella[i][j]==-1:
                indici.append(j)
            else:
                pass
        return indici


        """"
        Metodo genera_cartella: il metodo genera_cartella si occupa di inserire in 5 posizioni randomiche per ogni riga il numero 1 per contrassegnare che 
        quella casella conterrà un numero
        ---> riferimento usato nella classe GruppoCartelle per il riempimento
        La cartella finora è una matrice di zeri
        """


    def genera_cartella(self):
        self.cartella
        self.azzera_contatore()
        for i in range(5):
            z = self.posizione_libera_colonna(0)
            c = random.choice(z)
            self.aggiungi_numero(0, c, 1)

        for i in range(5):
            z = self.posizione_libera_colonna(1)
            c = random.choice(z)
            self.aggiungi_numero(1, c, 1)

        for i in range(5):
            z = self.posizione_libera_colonna(2)
            c = random.choice(z)
            self.aggiungi_numero(2, c, 1)

        return self.cartella

    """
    Metodo segna_numero: metodo che controlla se sulla casella è presente il numero estratto e lo segna sostituendolo con  -1
    """

    def segna_numero(self,num_estratto):
        for riga in range(0,3):
            for colonna in range(0,9):
                if self.cartella[riga][colonna]==num_estratto:
                    self.cartella[riga][colonna]=-1
                    print(self.cartella)
