# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:26:46 2022

@author: agnes
"""

import numpy as np

"""
Classe Giocatore: 
    - prende le cartelle 
    - controllo numero 
    - controllo vincita 
    - verifica cartella
    """
    
class Giocatore: 
    
    #username: username associato al giocatore
    #n_cartelle: numero (int) di cartelle richieste dal giocatore
    #cartelle_assegnate: lista inizialmente vuota che conterrà le cartelle assegnate al giocatore
    
    def __init__(self,username,n_cartelle, cartelle_assegnate = None):
        self.username = username 
        self.n_cartelle = n_cartelle
        self.cartelle_assegnate = []
        
    """
    Metodo aggiungi_cartella : 
        Il giocatore prende una nuova cartella che aggiunge alle precedenti
        
    """
    
    def aggiungi_cartella(self, nuova_cartella): 
        self.cartelle_assegnate.append(nuova_cartella)
        
    """
    Metodo controllo_numero :
    Dopo aver estratto il numero (intero) il giocatore controlla se le sue cartelle lo possiedono.
    -1 --> al posto del numero estratto presente sulla cartella.
    Verifico che il giocatore abbia o meno il numero estratto in una delle sue cartelle
    ed in caso positivo viene posto uguale a -1 per 'segnarlo'
    numero_estratto (int) : il valore estratto dal tabellone
    
    """
    def controllo_numero(self,numero_estratto):
        
        if numero_estratto==90:
            colonna = 8
        else:
            colonna=numero_estratto//10
        stampa = True                                # Questo valore mi dice se devo stampare il fatto di avere o meno un numero
                                                    # viene inizializzato a true quindi se il giocatore ha in una delle sue cartelle il numero
                                                    # viene stampato un messaggio e reso false la variabile, cosi da non stampare il messaggio nel caso in cui
                                                    # il giocatore abbia nuovamente il numero in altre cartelle
        for i in range(0,len(self.cartelle_assegnate)):
            for riga in range(0,3):
                if self.cartelle_assegnate[i].cartella[riga][colonna]==numero_estratto:    # Se la cartella presenta il numero
                    self.cartelle_assegnate[i].cartella[riga][colonna]=-1                  # Viene sostituito un -1 
                    
                    
                    if stampa:                     # Tale if è necessario per non stampare più 
                                                        # di una volta il messaggio qualora il giocatore
                                                        # abbia lo stesso numero in piu cartelle
                        print('Ho il '+str(numero_estratto))
                        stampa = False
                                                         
            
    """ 
    Metodo check_vincita : 
        Controllo delle vincite(interi, 2--> ambo, 3--> terno...) del giocatore
        Per la verifica della Tombola si verifica che nella cartella siano presenti solo 0 e -1
    """
   
    def check_vincita(self,vincite): 
         for i in range(self.n_cartelle):
            if vincite==5:
                                    
                occorenze = np.unique(self.cartelle_assegnate[i].cartella)
                
                if len(occorenze)==2: 
                    #quindi ci sono solo 0 e -1
                    print('Tombola!')
                
                    vincite = 6     
                else:                 
                    return vincite
            
            else:
                for riga in range(0,3):
                    contatore=0
                    vincita_aggiornata = vincite+1      
                    for colonna in range(0,9):
                        if self.cartelle_assegnate[i].numero_estratto(riga,colonna):
                            contatore=contatore+1
                    if contatore == vincita_aggiornata:
                        vincite = vincita_aggiornata                       
                        if vincite==2 :
                            print('Ambo')
                            return vincite                   
                        elif vincite==3 :
                            print('Terna')
                            return vincite  
                        elif vincite==4 :
                            print('Quaterna')
                            return vincite  
                            
                        elif vincite==5 :
                            print('Cinquina')
                            return vincite
         return vincite     
                    
    """
    Metodo visualizza_cartelle_giocatore: 
    mostra le cartelle del giocatore. 
    Se un numero è stato estratto ed è presente nella cartella, viene mostrato con il simbolo '*'
    Le caselle che non contengono nulla vengono mostrate come ' ', mentre tutti gli altri numeri della cartella che non sono stati estratti vengo visualizzati normalmente.
    
    """
                    
    def visualizza_cartelle_giocatore(self):
        print(f"\nCartelle del giocatore {self.username} :\n")
        for i in range(0,len(self.cartelle_assegnate)):
            print('Cartella numero'+str(i+1))
            for riga in range(3):
                print('[ ',end='')
                for colonna in range(9):
                    if self.cartelle_assegnate[i].visualizza_elem_cartella(riga,colonna) == 0: #casella vuota --> stampo spazio vuoto
                        print(' ',end=' ')
                    elif self.cartelle_assegnate[i].visualizza_elem_cartella(riga,colonna) == -1: #numer estratto contrassegnato con *
                        print('*',end=' ')
                    else:
                        print(int(self.cartelle_assegnate[i].visualizza_elem_cartella(riga,colonna)),end=' ')
                print(']')
