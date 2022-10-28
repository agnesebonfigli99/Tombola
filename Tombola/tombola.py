# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:13:37 2022

@author: mcudi
"""

import Utils
import Tavolo
import Sacchetto
import sys

args = Utils.initialize_parser()
# Verifica che i dati inseriti siano corretti:
n_giocatori = Utils.check_numero_giocatori(args.giocatori)
cartelle_richieste = Utils.check_lista_cartelle(n_giocatori,args.numero_di_cartelle)
#n_giocatori = 3
#cartelle_richieste = [2, 4, 1]
def check_estrazione_corrente(giocatori,numero_estratto,vincite,cartellone):
    """
    Verifico che i giocatore abbiano o meno il numero estratto in una delle loro cartelle
    e che abbiano effettuato una vincita.   
         
    Input
    -----
    giocatori (Giocatore[]) : gli oggetti giocatori della tombola
    numero_estratto (int) : il valore estratto dal tabellone
    vincite (int): che mi dice a che vincita siamo arrivati 
    cartellone(Cartellone[]):  oggetto cartellone 
    
    Output 
    ------
    vincite (int): che mi dice a che vincita siamo arrivati 
             
    """       
    for i in range(0,len(giocatori)):
        print('Giocatore'+ str(i+1)+' :') 
        giocatori[i].controllo_numero(numero_estratto)
        vincite= giocatori[i].check_vincita(vincite)
    index_cartella_numero_estratto=cartellone.segna_n_estratto(numero_estratto) # In uscita ho l'indice della cartella del cartellone che contine il numero estratto
    vincite = cartellone.verifica_vincite_cartellone(vincite,index_cartella_numero_estratto)
        
    return vincite

print('\n-----------   INIZIO GIOCO   -----------')

# Inizializzazione del Banco, che assegna le cartelle ai giocatori ed inizializza il cartellone
Tavolo = Tavolo.Tavolo(n_giocatori,cartelle_richieste) 
giocatori = Tavolo.assegnazione_cartelle() 
cartellone= Tavolo.assegna_cartellone()

# La variabile 'vincite' ci indica la vincita a cui siamo arrivati ed è inizializzata a 1,
# ogni volta che si verifica una vincita tale variabile incrementa di 1. Il gioco termina
# quando 'vincite' è uguale a 6, cioè quando viene effettuata la tombola.
vincite = 1
Sacchetto=Sacchetto.Sacchetto()
for i in range(1,91):
    numero_estratto = Sacchetto.estrai_numero()
    vincite = check_estrazione_corrente(giocatori, numero_estratto, vincite, cartellone)
    Utils.domanda_stampa(n_giocatori, giocatori, cartellone)
    if vincite==6: # Se è stata fatta tombola -> termina il gioco
        print('\n------------------- FINE PARTITA ---------------------')
        sys.exit()
    i= i+1

