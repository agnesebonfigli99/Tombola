# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:58:13 2022

@author: franc
"""

import Gruppo
import Giocatore
import random
import Cartellone

class Tavolo:
    
    """
    la classe Tavolo viene implementata per distribuire ai giocatori le cartelle da loro richieste 
    """
    
    def __init__(self,giocatori,cartelle_richieste,lista_cartelle_assegnate=None):
        #giocatori:(int)numero di giocatori che partecipano
        #cartelle_richieste: numero di cartelle richieste dal giocatore
        #lista_cartelle_assegnate: lista di numeri che rappresentano il numero di cartelle assegnate al rispettivo giocatore
        self.giocatori=giocatori
        self.cartelle_richieste=cartelle_richieste
        self.lista_cartelle_assegnate = []
        
    """
    metodo assegnazione: metodo che fornisce a ogni giocatore il numero di cartelle richieste 
    metodo che non assegna a più giocatori la stessa cartella
    cartelle_giocatore:gruppo di cartelle assegnate al giocatore
    """
    def assegnazione(self):
        ''' serve metodo che genera il gruppo di cartelle richieste dal giocatore ''' 
        #gruppo
        cartelle_giocatore = Gruppo_Cartelle.Gruppo_Cartelle()
        cartelle_giocatore.generazione_numeri()
        for i in range(self.cartelle_richieste):
            self.lista_cartelle_assegnate.append(cartelle_giocatore.single_cartella(i))
            return self.lista_cartelle_assegnate
      
    """
    metodo assegna_cartellone: il banco si occupa anche di assegnare il cartellone
    """
    def assegna_cartellone(self):
        cartellone=Cartellone.Cartellone()
        cartellone.crea_cartellone()
        return cartellone
        
