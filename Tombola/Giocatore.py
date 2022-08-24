<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:48:20 2022

@author: agnes
"""

import numpy as np

'''Classe Giocatore: 
    - prende le cartelle 
    - controllo numero 
    - controllo vincita 
    - verifica cartella  '''
    
class Giocatore: 
    
    def __init__(self,username,n_cartelle, cartelle_assegnate = None):
        self.username = username 
        self.n_cartelle = n_cartelle
        self.cartelle_assegnate = []
        
    ''' Metodo Aggiungi Cartella : 
        Il giocatore prende una nuova cartella che aggiunge alle precedenti'''
    
    def aggiungi_cartella(self, nuova_cartella): 
        self.cartelle_assegnate.append(nuova_cartella)
        
    ''' Metodo Check Numero
    Dopo aver estratto il numero (intero) si controlla se le sue cartelle lo possiedono.
    0 --> al posto del numero estratto presente sulla cartella ''' 
    
    def check_num(self, num_estratto): 
        for i in range(0,len(self.cartelle_assegnate)):
            for riga in range(0,3):
                if self.cartelle_assegnate[i].cartella[riga][colonna]==num_estratto:    # Se la cartella presenta il numero
                    self.cartelle_assegnate[i].cartella[riga][colonna]=0 
        
    ''' Metodo Check Vincita: 
        Controllo delle vincite(interi, 2--> ambo, 3--> terno...) del giocatore'''
        
    def check_vincita(self,vincita): 
         for i in range(self.n_cartelle):
            if vincita==5
                                    # vedo se si è verificata la tombola: 
                                    # cioe i valori contenuti nella cartella 
                                    # sono solo 0 e -1
                occorenze = np.unique(self.cartelle_assegnate[i].cartella)
                
                if len(occorenze)==2: 
                    
                    print('Tombola!')
                    vincita = 6     
                else:                 
                    return vincita
            
            else:
                for riga in range(0,3):
                    contatore=0
                    vincita_aggiornata = vincita+1      
                    for colonna in range(0,9):
                        if self.cartelle_assegnate[i].numero_estratto(riga,colonna):
                            contatore=contatore+1
                    if contatore == vincita_aggiornata:
                        vincita = vincita_aggiornata                       
                        if vincita==2 :
                            print('Ambo')
                            return vincita                   
                        elif vincita==3 :
                            print('Terna')
                            return vincita  
                        elif vincita==4 :
                            print('Quaterna')
                            return vincita  
                            
                        elif vincita==5 :
                            print('Cinquina')
                            return vincita
          return vincita
      
      '''Metodo Visualizza Cartella Giocatore per vedere quali numeri sono stati segnati e per visualizzare
      le cartelle nel complesso'''
      def visualizza_cartelle_giocatore(self): 
          print(f"\nCartelle di {self.username} : \n")
          for i in range(1,len(self.cartelle_assegnate)): 
              print('Cartella numero' + str(i))
              for riga in range(3): 
                  print('[', end='')
                  for colonna in range(9): 
                      if self.cartelle_assegnate[i].elemento_cartella(riga,colonna) == -1: 
                          print(' ', end='')
                      elif self.cartelle_assegnate[i].elemento_cartella(riga,colonna) == 0: 
                          print('*', end='')
                      else:
                          print(int(self.cartelle_assegnate[i].elemento_cartella(riga,colonna)),end=' ')
                  print(']')
                          
                    
          
        
        
        
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:48:20 2022

@author: agnes
"""

import numpy as np

'''Classe Giocatore: 
    - prende le cartelle 
    - controllo numero 
    - controllo vincita 
    - verifica cartella  '''
    
class Giocatore: 
    
    def __init__(self,username,n_cartelle, cartelle_assegnate = None):
        self.username = username 
        self.n_cartelle = n_cartelle
        self.cartelle_assegnate = []
        
    ''' Metodo Aggiungi Cartella : 
        Il giocatore prende una nuova cartella che aggiunge alle precedenti'''
    
    def aggiungi_cartella(self, nuova_cartella): 
        self.cartelle_assegnate.append(nuova_cartella)
        
    ''' Metodo Check Numero
    Dopo aver estratto il numero (intero) si controlla se le sue cartelle lo possiedono.
    0 --> al posto del numero estratto presente sulla cartella ''' 
    
    def check_num(self, num_estratto): 
        for i in range(0,len(self.cartelle_assegnate)):
            for riga in range(0,3):
                if self.cartelle_assegnate[i].cartella[riga][colonna]==num_estratto:    # Se la cartella presenta il numero
                    self.cartelle_assegnate[i].cartella[riga][colonna]=0 
        
    ''' Metodo Check Vincita: 
        Controllo delle vincite(interi, 2--> ambo, 3--> terno...) del giocatore'''
        
    def check_vincita(self,vincita): 
         for i in range(self.n_cartelle):
            if vincita==5
                                    # vedo se si è verificata la tombola: 
                                    # cioe i valori contenuti nella cartella 
                                    # sono solo 0 e -1
                occorenze = np.unique(self.cartelle_assegnate[i].cartella)
                
                if len(occorenze)==2: 
                    
                    print('Tombola!')
                    vincita = 6     
                else:                 
                    return vincita
            
            else:
                for riga in range(0,3):
                    contatore=0
                    vincita_aggiornata = vincita+1      
                    for colonna in range(0,9):
                        if self.cartelle_assegnate[i].numero_estratto(riga,colonna):
                            contatore=contatore+1
                    if contatore == vincita_aggiornata:
                        vincita = vincita_aggiornata                       
                        if vincita==2 :
                            print('Ambo')
                            return vincita                   
                        elif vincita==3 :
                            print('Terna')
                            return vincita  
                        elif vincita==4 :
                            print('Quaterna')
                            return vincita  
                            
                        elif vincita==5 :
                            print('Cinquina')
                            return vincita
          return vincita
      
      '''Metodo Visualizza Cartella Giocatore per vedere quali numeri sono stati segnati e per visualizzare
      le cartelle nel complesso'''
      def visualizza_cartelle_giocatore(self): 
          print(f"\nCartelle di {self.username} : \n")
          for i in range(1,len(self.cartelle_assegnate)): 
              print('Cartella numero' + str(i))
              for riga in range(3): 
                  print('[', end='')
                  for colonna in range(9): 
                      if self.cartelle_assegnate[i].elemento_cartella(riga,colonna) == -1: 
                          print(' ', end='')
                      elif self.cartelle_assegnate[i].elemento_cartella(riga,colonna) == 0: 
                          print('*', end='')
                      else:
                          print(int(self.cartelle_assegnate[i].elemento_cartella(riga,colonna)),end=' ')
                  print(']')
                          
                    
          
        
        
        
>>>>>>> 10faccac2bec3af6740b8db444859f0dddd8dcbd
        