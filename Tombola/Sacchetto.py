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
    Metodo estrai numero: metodo che estrae un numero dal sacchetto senza ripetizioni e lo aggiunge ad una lista. 
    In modo che il numero di estrazioni non superi il numero di elementi contenuti nel sacchetto. 
    """
    
    def estrai_numero(self): 
        l = [] #inizializzo una lista l inizialmente vuota che verrà riempita con i numeri estratti.
        for i in range(1,91): 

            random.shuffle(self.n_sacchetto) #riorganizzo l'ordine della lista n_sacchetto.

            estratto = self.n_sacchetto[0] #il numero estratto è il primo numero della lista n_sacchetto di cui abbiamo cambiato l'ordine.

            self.n_sacchetto.pop(0) #rimuovo l'elemento estratto dal sacchetto in modo che non ci siano ripetizioni nell'estrazioni

            l.append(estratto) #lista riempita

            print(f"Il numer estratto è", estratto)
            
            return estratto


