# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:58:13 2022

@author: franc
"""

import Gruppo_Cartelle
import Giocatore
import random
import Cartellone

class Tavolo:
    
    """
    la classe Tavolo viene implementata per distribuire ai giocatori le cartelle da loro richieste 
    """
    
    def __init__(self,n_giocatori,cartelle_richieste):
        #giocatori:(int)numero di giocatori che partecipano
        #cartelle_richieste: numero di cartelle richieste dal giocatore
        #lista_cartelle_assegnate: lista di numeri che rappresentano il numero di cartelle assegnate al rispettivo giocatore
        self.n_giocatori=n_giocatori
        self.cartelle_richieste=cartelle_richieste
        
    """
    metodo assegnazione_cartelle: metodo che fornisce a ogni giocatore il numero di cartelle richieste 
    metodo che non assegna a più giocatori la stessa cartella
    cartelle_giocatore:gruppo di cartelle assegnate al giocatore
    """
    def assegnazione_cartelle(self):
        ''' serve metodo che genera il gruppo di cartelle richieste dal giocatore ''' 
        #gruppo
        cartelle_disponibili=[]
        cartelle_disponibili = Gruppo_Cartelle.Gruppo_Cartelle.crea_gruppi_necessari(self.cartelle_richieste)
        giocatori=[] # crea i giocatori (oggetti) e li inserisce nell'omonima lista
        
        for i in range(0,self.n_giocatori):
            giocatori.append(Giocatore.Giocatore(str(i+1),self.cartelle_richieste[i]))
            # a ciascun giocatore vengono assegnate, in maniera casuale tra quelle 
            # disponibili, il numero di cartelle richieste
            for j in range(0,self.cartelle_richieste[i]):
                
                index_cartella = random.randint(0,len(cartelle_disponibili)-1)
                giocatori[i].aggiungi_cartella(cartelle_disponibili[index_cartella])
                cartelle_disponibili.pop(index_cartella)
                
        return giocatori
            
      
    """
    metodo assegna_cartellone: il banco si occupa anche di assegnare il cartellone
    """
    def assegna_cartellone(self):
        cartellone=Cartellone.Cartellone()
        cartellone.crea_cartellone()
        return cartellone
        
