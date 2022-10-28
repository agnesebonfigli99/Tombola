
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:31:39 2022

@author: mcudi
"""

import numpy as np
import random
import Cartella
import math

class Gruppo_Cartelle:

    """
    Si deve generare un gruppo di sei cartelle diverse, senza ripetizioni di numeri --> l'output è una lista di 6 cartelle che rappresenta 1 gruppo.
    
    E' necessario che la somma  degli elementi sulla prima colonna di un gruppo sia pari a 9.
    La somma degli elementi dell'ultima colonna invece è 11 (80 a 90 inclusi). Sulle altre colonne la somma degli elementi deve essere pari a 10.
    Va generato un gruppo che rispetta tutte le condizioni. Se non è così si reitera il ciclo.
  
    """
    
    def _init_(self):
        self.lista_cartelle=[] #si inizializza una lista vuota che conterrà sei oggetti (ovvero le cartelle)'''
        
    """
    Metodo tramite cui si crea una lista di 6 cartelle dove la prima avrà l'ultima posizione in basso a destra 
        occupata per poi inserire il numero 90
    """
    def crea_lista(self):    
        self.lista_cartelle=[]
        prima_cartella=Cartella.Cartella()
        prima_cartella.genera_cartella() 
        posizione90=False
        while not posizione90:  #ciclo while che itera finchè non viene generata una cartella con l'ultima posizione in basso a destra occupata dove sarà inserito il 90
            if prima_cartella.casella_occupata(2,8):
                posizione90 = True 
            else:
                prima_cartella.genera_cartella()
        self.lista_cartelle.append(prima_cartella)  #quando tale cartella viene generata la salva in lista_cartelle
        for i in range(5):
            altracartella=Cartella.Cartella()
            altracartella.genera_cartella()
            self.lista_cartelle.append(altracartella)
        return self.lista_cartelle

    """ 
    Metodo che permette di selezionare una singola cartella dal gruppo di 6 cartelle
    
    """
    def single_cartella(self,i):
        return self.lista_cartelle[i]
    
    
    """
    Metodo che verifica che il gruppo di cartelle rispetti la condizione sull'ultima colonna: somma degli elementi 
    totali uguale a 11
    """
    def verifica_ultima_colonna(self):
        l=[] #lista vuota in cui viene memorizzata la somma degli elementi sull'ultima colonna delle 6 cartelle
        somma_el_col = 0  #contatore inizializzato a 0 in cui viene memorizzato il numero di elementi sull'ultima colonna per ciascuna cartella
        for k in range(6):
            singolacartella=self.single_cartella(k)
            somma_el_col = singolacartella.conta_elementi_colonne(8)  #somma gli emenenti sulla colonna di indice 8 (nona colonna) utilizzando il metodo conta_elementi_colonne
            l.append(somma_el_col)
            c=sum(l)
        if c==11:
            condition = True
        else:
            condition = False 

        return condition
    
 
    """ 
    Metodo che fa la somma degli elementi presenti su le prime 
    8 colonne del gruppo cartelle generato 
    """
    def somma_colonne_gruppo(self):
        somma_colonne=np.zeros(8)
        for c in range(0,6):
            for colonna in range(0,8):
                somma_colonne[colonna] = somma_colonne[colonna] + self.single_cartella(c).conta_elementi_colonne(colonna)
        return somma_colonne
    
    
    """
    Metodo che controlla se sono rispettati i vincoli sulle prime 8 colonne del gruppo_cartelle. 
    Restituisce True se sono rispettati; False altrimenti
    """
    def check_vincoli_colonne(self, vincoli):
        somma_colonne=self.somma_colonne_gruppo()
        if np.array_equal(somma_colonne, vincoli): #array_equal restituisce True se i due vettori che riceve in ingresso sono uguali, False altrimenti
           return True
        else:
            return False

    """
    Metodo che nel caso di mancato rispetto dei vincoli su una delle prime 8 colonne riposiziona gli 0 e gli 1 per garanntire il rispetto dei vincoli
    
    primo caso: se una colonna i-esima del gruppo ha un numero di elementi superiore al vincolo si cerca tra le colonne successive (su tutte le cartelle) una colonna j-esima
    in cui il numero di elementi sia inferiore al vincolo richiesto in modo che l'elemento in più dell'iesima colonna sarà ceduto alla j-esima colonna
    
    secondo caso: se una colonna i-esima del gruppo ha un numero di elementi inferiore al vincolo si cerca tra le colonne successive (su tutte le cartelle) una colonna j-esima
    in cui il numero di elementi sia superiore al vincolo richiesto in modo che l'elemento in meno dell'i-esima colonna le sarà ceduto dalla j-esima colonna 
    """
    def cambio_posizioni(self,vincoli):
            for i in range(0,8):  #ciclo su tutte le colonne dell'intero gruppo
                somma_colonne=self.somma_colonne_gruppo() #vettore di dimensione 8 in cui ogni elemento indica la somma del numero di elementi su una colonna dell'intero gruppo di cartelle
                while somma_colonne[i] > vincoli[i]: #ciclo while che itera finchè sull'i-iesima colonna del gruppo la somma degli elementi supera il vincolo
                  for j in range(i + 1,8): #ciclo for che va dalla colonna successiva all'i-esima fino alla colonna di indice 8
                      while somma_colonne[j] < vincoli[j]: #ciclo while che itera finchè la j-esima colonna del gruppo la somma degli elementi è inferiore al vincolo
                          for c in range(0,6):
                              cartella_singola = self.single_cartella(c)
                              for r in range(0,3): #ciclo sulle righe di ogni cartella
                                  if cartella_singola.cartella[r,i] == 1 and cartella_singola.cartella[r,j] == 0 and cartella_singola.conta_elementi_colonne(i)>1: #la seconda condizione è necessaria perchè in una singola cartella su ogni colonna deve esserci alemeno un elemento
                                      cartella_singola.rimuovi_numero(r,i)
                                      cartella_singola.aggiungi_numero(r, j, 1) 
                                      somma_colonne=self.somma_colonne_gruppo()   #con il break esce dal ciclo sulle righe
                                      break
                              if somma_colonne[j] == vincoli[j] or somma_colonne[i] == vincoli[i]:
                                    break  
                          if somma_colonne[i] == vincoli[i]:
                            break
                      if somma_colonne[i] == vincoli[i]:  
                        break
                    
                while somma_colonne[i] < vincoli[i]:
                    for j in range(i + 1,8):
                        while somma_colonne[j] > vincoli[j]:
                            for c in range(0,6):
                                cartella_singola = self.single_cartella(c)
                                for r in range(0,3):
                                    if cartella_singola.cartella[r,i] == 0 and cartella_singola.cartella[r,j] == 1 and cartella_singola.conta_elementi_colonne(j)>1:
                                        cartella_singola.rimuovi_numero(r,j)
                                        cartella_singola.aggiungi_numero(r, i, 1)
                                        somma_colonne=self.somma_colonne_gruppo()
                                        break
                                if somma_colonne[j] == vincoli[j] or somma_colonne[i] == vincoli[i]:
                                  break  
                            if somma_colonne[i] == vincoli[i]:
                              break             
                        if somma_colonne[i] == vincoli[i]:  
                          break       
                      
    """
    Metodo che genera il gruppo che rispetta tutte le condizioni sulle colonne: crea gruppi di cartelle finchè 
    non viene rispettata la condizione sull'ultima colonna e successivamente su quel gruppo effettua i cambi di posizioni
    """
    def genera_gruppo(self):
          controllo_ultima_colonna = False 
          while not controllo_ultima_colonna:
              self.crea_lista()
              controllo_ultima_colonna = self.verifica_ultima_colonna()
              
          vincoli_colonne=np.array([9,10,10,10,10,10,10,10])
          controllo_generaleOK = False
          while not controllo_generaleOK:
              self.cambio_posizioni(vincoli_colonne)
              controllo_generaleOK = self.check_vincoli_colonne(vincoli_colonne)
         
          return self.lista_cartelle
                                        
                                        
    """
    Metodo tramite cui si inseriscono i numeri nelle posizioni uguali a 1 forzando il numero 90 nella posizione in basso a destra della 
       prima cartella
    """
     
    def generazione_numeri(self):
     numeri={0:[1,2,3,4,5,6,7,8,9],
         1:[10,11,12,13,14,15,16,17,18,19],
         2:[20,21,22,23,24,25,26,27,28,29],
         3:[30,31,32,33,34,35,36,37,38,39],
         4:[40,41,42,43,44,45,46,47,48,49],
         5:[50,51,52,53,54,55,56,57,58,59],
         6:[60,61,62,63,64,65,66,67,68,69],
         7:[70,71,72,73,74,75,76,77,78,79],
         8:[80,81,82,83,84,85,86,87,88,89]}
     
     for i in range (6):
      cartella_da_riempire = self.single_cartella(i)
      for j in range (3):
          for k in range (9):
            if cartella_da_riempire.casella_occupata(j, k):
                if i==0 and j==2 and k==8: 
                      num = 90
                      cartella_da_riempire.cartella[j, k] = num
                else:
                      num = random.choice(numeri[k])
                      cartella_da_riempire.cartella[j, k] = num  
                      numeri[k].remove(num)
     #print(numeri[k])
     return self.lista_cartelle
 
    """
    metodo che genera un numero n di gruppi di 6 cartelle in base al numero di caretlle richieste dai giocatori.
    il numero totale di cartelle richieste dai giocatori viene diviso per 6 e arrotondato per eccesso in modo da sapere quanti gruppi da 6 occorrono per soddidfare la richiesta
    La funzione genera n gruppi utilizzando il metodo 'crea_gruppo' della classe Gruppo()
    in base a quante cartelle sono richieste dai giocatori
    """

    def crea_gruppi_necessari(cartelle):

          
     lista_cartelle_richieste=[]
     conteggio= math.ceil(sum(cartelle)/6) 
     # Mi dice il numero di gruppi di cartelle di cui ho bisogno
     for i in range(0,conteggio):
            g=Gruppo_Cartelle()
            g.genera_gruppo()
            g.generazione_numeri()
            lista_cartelle_richieste= lista_cartelle_richieste + g.lista_cartelle
     return lista_cartelle_richieste
