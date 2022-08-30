# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:27:45 2022

@author: agnes
"""

import random 
"""
La Classe Sacchetto viene implementata per l'estrazione di numeri da 1 a 90 in maniera casuale. 

"""
class Sacchetto: 
    def __init__(self,n_sacchetto=None):
      #n_sacchetto : è una lista inizializzata vuota che verrà riempita con i numeri da 1 a 90
        self.n_sacchetto=[]
        for i in range(1,91): 

            self.n_sacchetto.append(i)
    """
    Metodo mostra_sacchetto: metodo che permette di visualizzare il sacchetto di numeri
    """
    def mostra_sacchetto(self): 
        print(f"il sacchetto è", self.n_sacchetto)
        
    """
    Metodo estrai numero: metodo che estrae un numero dal sacchetto e lo aggiunge ad una lista. 
    In modo che il numero di estrazioni non superi il numero di elementi contenuti nel sacchetto. 
    """
    
    def estrai_numero(self): 
        l = [] #inizializzo una lista l inizialmente vuota che verrà riempita con i numeri estratti.
        for i in range(1,91): 

            self.mischia = random.shuffle(self.n_sacchetto) #riorganizzo l'ordine della lista n_sacchetto.

            self.estratto = self.n_sacchetto[0] #il numero estratto è il primo numero della lista n_sacchetto di cui abbiamo cambiato l'ordine.

            self.n_sacchetto.pop(0) #rimuovo l'elemento dal sacchetto in modo che non ci siano ripetizioni

            l.append(self.estratto) #lista riempita

            print(f"Il numer estratto è", self.estratto, l)
        

uno = Sacchetto()
uno.mostra_sacchetto()
uno.estrai_numero()

