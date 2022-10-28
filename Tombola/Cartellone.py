#  Developer: $ Lavinia
# -*- coding: utf-8 -*-

import numpy as np

class Cartellone:
    def __init__(self, cartellone=None):  #in questo modo il costruttore crea un solo oggetto cartellone in fase di esecuzione
        self.cartellone=[]  #martice vuota"

    """ Metodo crea_cartellone: il metodo crea il cartellone generando le cartelle che lo costituiscono (martici 3x5) """
    def crea_cartellone(self):
        #inizializzazione delle 6 cartelle come matricidi zeri 3x5
     for i in range(6):
            cartelle=np.zeros((3,5))
            self.cartellone.append(cartelle)

     """RIEMPIMENTO CARTELLE CON NUMERI DA 1 A 90 IN ORDINE CRESCENTE
     riempimento prima riga della prima caretlla della parte sx con numeri da 1 a 5,
     rimepimento prima riga della prima cartella della parte dx con numeri da 6 a 10"""
     p_sx=list((range(1,6)))
     p_dx=list((range(6,11)))

     """per completare il riempimento delle cartelle tutte le righe seguenti vengono generate moltiplicando x10 le prime due
         (a seconda della posizione destra o sinitra) """

     for i in range(6):
        #le 3 cartelle sul lato sx del cartellone sono identificate da indice pari (i=0, i=2, i=4)
        #le 3 cartelle sul latp dx di conseguenza sono identificate da indice dispari (i=1, i=3, i=5)

            if i% 2 ==0: #se indice / 2 non da resto quindi è pari
               if i==0:
                   for riga in range(3):
                       for index in range(len(p_sx)):
                           self.cartellone[i][riga][index]=p_sx[index]+(10*riga)

               elif i==2:
                   for riga in range(3):
                       for index in range (len(p_sx)):
                           self.cartellone[i][riga][index]=p_sx[index]+(riga+ i + 1)*10

               else:
                   for riga in range(3):
                       for index in range (len(p_sx)):
                            self.cartellone[i][riga][index]=p_sx[index]+(riga+i +2)*10


            else:
                if i==1:
                   for riga in range(3):
                       for index in range(len(p_dx)):
                            self.cartellone[i][riga][index] = p_dx[index] + (10 * riga)

                elif i==3:
                     for riga in range(3):
                         for index in range(len(p_dx)):
                              self.cartellone[i][riga][index] = p_dx[index] + (riga + i ) * 10

                else:
                     for riga in range(3):
                         for index in range(len(p_dx)):
                              self.cartellone[i][riga][index] = p_dx[index] + (riga + i + 1) * 10


    
    """
    Metodo segna_n_estratto: metodo che riceve in input il numero estratto e l'indice della cartella che lo contiene e sostituisce il numero 
    estratto con -1
    """
    
    def segna_n_estratto(self,num_estratto):
     for i in range(6):
      for riga in range(3):
       for index in range(5):
        if self.cartellone[i][riga][index]==num_estratto:
         self.cartellone[i][riga][index]=-1
         id_cartella = i 
         return id_cartella
  
         
    """metodo verifica_vincite_cartellone per verificare le vincite effettuate dal cartellone
        attributi:" \
         vincita: intero indicante la vincita, 2--> ambo 3--> terno, ecc..
         id_cartella: intero che identifica la cartella a cui appartiene il numero estratto, cioè la cartella per la quale si
         verifica la vincita 
        input: vincite, id_cartella
        output: vincite
        quando il numero viene estratto viene sostituito con 0
    """
    def verifica_vincite_cartellone(self,vincite,id_cartella):

        if vincite==5:
            occorrenze=np.unique(self.cartellone[id_cartella]) #per verificare la vincita

            if len(occorrenze)==1:
                print('\nTombola del Cartellone')
                vincite=6

            else:
                return vincite

        else:
             for riga in range(0,3):
                 contatore=0 #per contare gli 0 sulla riga di una certa cartella
                 vincita_aggiornata=vincite+1

                 for colonna in range (0,5):
                     if self.cartellone[id_cartella][riga,colonna]==-1:
                         contatore=contatore+1
                 if  contatore==vincita_aggiornata:
                     vincite=vincita_aggiornata

                     if vincite==2:
                         print( '\nAmbo del Cartellone')
                         return vincite
                     elif vincite==3:
                         print('\nTerno del Cartellone')
                         return vincite
                     elif vincite==4:
                         print('\nQuaterna del Cartellone')
                         return vincite
                     elif vincite==5:
                         print('\nCinquina del Cartellone')
                         return vincite

        return vincite
