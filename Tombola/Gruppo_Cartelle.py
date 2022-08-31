# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:31:39 2022

@author: mcudi
"""

import random
import Cartella

class Gruppo_Cartelle:

    '''
    Si deve generare un gruppo di sei cartelle diverse, senza ripetizioni di numeri.
    
    E' necessario che la gli elementi sulla prima colonna di un gruppo sia pari a 9.
    La somma degli elementi dell'ultima colonna invece è 11 (80 a 90 inclusi). Sulle altre colonne la somma degli elementi deve essere pari a 10.
    Va generato un gruppo che rispetta tutte le condizioni. Se non è così si reitera il ciclo.
  
    '''

    def __init__(self):
        '''si inizializza una lista vuota che conterrà sei oggetti ovvero le cartelle'''
        self.lista_cartelle=[]
        '''si riempie la lista; la prima cartella avrà sempre la posizione 2,8 occupata per il numero 90'''
    
    def lista(self):    
        exit=False
        while exit == False:
          cartella=Cartella.genera_cartella()
          if self.cartella.casella_occupata(2,8)!=1:
             exit=True 
        self.lista_cartelle[0] = cartella     
        for i in range(1,6):
            cartella= Cartella.genera_cartella()
            self.lista_cartelle.append(cartella)
            return lista_cartelle
    
    '''dato l'indice della cartella desiderata ne permette la selezione'''
    def single_cartella(self,i):
        return self.lista_cartelle[i]
    
    '''tale metodo verifica che la somma degli elementi sulla prima colonna sia uguale a 9 (condition == True)'''
    def verifica_prima_colonna(self):
        l=[]
        for k in range(6):
            somma_el_col = 0
            somma_el_col = somma_el_col + self.single_cartella(k).self.contatore_elem_c[0]
            l.append(somma_el_col)
            c=sum(l)
            if c==9:
                condition = True
            else:
                condition=False 

        return condition

    '''tale metodo garantisce che il gruppo creato abbia 9 elementi sulla prima colonna'''
    def primo_gruppo(self):
        condiz_uscita = self.verifica_prima_colonna()
        while condiz_uscita == False:
          self.lista_cartelle()
          self.verifica_prima_colonna()
          condiz_uscita=self.verifica_prima_colonna()
        return self.lista_cartelle
    
    '''dato il gruppo di cartelle che rispetta la condizione sulla prima colonna si impone analogamente che venga rispettata la condizione sull' ultima colonna (11 elementi totali tra le sei cartelle del gruppo)'''
    def verifica_ultima_colonna(self):
        self.primo_gruppo()
        l=[]
        for k in range(6):
            somma_el_col = 0
            somma_el_col = somma_el_col + self.single_cartella(k).self.contatore_elem_c[8]
            l.append(somma_el_col)
            c=sum(l)
            if c==11:
                condition = True
            else:
                condition = False 

        return condition
    
    '''si genera il gruppo che rispetta anche la condizione sull' ultima colonna'''
    def secondo_gruppo(self):
        exitcondition = self.verifica_ultima_colonna()
        while exitcondition == False:
          self.lista_cartelle()
          self.verifica_prima_colonna()
          exitcondition=self.verifica_ultima_colonna()
        return self.lista_cartelle
      

    '''il metodo verifica che ciascuna colonna: dalla 2 alla 8 dell' intero gruppo siano formate esattamente da 10 elementi'''
    def verifica_colonne_intermedie(self):
        s1=[]
        s2=[]
        col_si=0  #numero di colonne che rispettano il vincolo
        for j in range(1,8):
            s1=[]
            for i in self.lista_cartelle:
                somma_el_col = 0
                somma_el_col = somma_el_col + i.self.contatore_elem_c[8](j)
                s1.append(somma_el_col)
            c=sum(s1)
            s2.append(c)
        for i in range(len(s2)):
            if s2[i]==10:
                col_si+=1

        if col_si==7:
            condition=True
        else:
            condition=False
        return condition

    '''si genera il gruppo che rispetta tutte le condizioni sulle colonne'''
    def terzo_gruppo(self):
        condiz = self.verifica_colonne_intermedie()
        while condiz == False:
          self.lista_cartelle()
          self.verifica_prima_colonna()
          self.verifica_ultima_colonna()
          condiz = self.verifica_colonne_intermedie()
        return self.lista_cartelle
    
    '''si inseriscono i numeri nelle posizioni diverse da  1''' 
    def generazione_numeri(self):
     numeri={0:[1,2,3,4,5,6,7,8,9],
         1:[10,11,12,13,14,15,16,17,18,19],
         2:[20,21,22,23,24,25,26,27,28,29],
         3:[30,31,32,33,34,35,36,37,38,39],
         4:[40,41,42,43,44,45,46,47,48,49],
         5:[50,51,52,53,54,55,56,57,58,59],
         6:[60,61,62,63,64,65,66,67,68,69],
         7:[70,71,72,73,74,75,76,77,78,79],
         8:[80,81,82,83,84,85,86,87,88,89,90]}
 
     for i in range (6):
      cartella_da_riempire = self.single_cartella[i]
      for j in range (3):
          for k in range (8):
            if cartella_da_riempire[j][k] != 1:
              num = random.choise(numeri[k])
              cartella_da_riempire[j][k] = num 
              numeri[k].remove(num)
              self.lista_cartelle.append(cartella_da_riempire)
      
            elif cartella_da_riempire[j][k] == 1:
             num = 0
             cartella_da_riempire [j][k]= num
      
        #è necessario generare una nuova variabile? perchè in lista cartelle ho già le sei cartelle con le posizioni e con append vado a mettere in coda un'altra (quella con i numeri)          
     
     return self.lista_cartelle

lista1=Gruppo_Cartelle()
lista1.lista()