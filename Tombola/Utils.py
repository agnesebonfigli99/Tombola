# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:52:08 2022

@author: mcudi
"""
import argparse

def initialize_parser():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--giocatori",
                        help="Numero di giocatori",
                        required=True,
                        type=int)
    parser.add_argument("-n", "--numero_di_cartelle",
                        help="Numero di cartelle per ciascun giocatore",
                        type=int,
                        required=True,
                        nargs='+')
    return parser.parse_args()

def check_numero_giocatori(n_giocatori):
    """
    Verifica se il numero di giocatori è rispetta le regole (>1 e <=8)
    
    Input
    -------
    n_giocatori (int): numero dei giocatori
    
    Output
    ------
    n_giocatori (int): numero dei giocatori
    oppure
    un messaggio e termina il programma
    """
        
    if n_giocatori>1 and n_giocatori<9:
        return n_giocatori
    else:
        print('\n- ERRORE - Il numero di giocatori deve essere superiore ad 1 fino ad un massimo di 8\n')
        exit()

def check_lista_cartelle(n_giocatori, lista_cartelle):
    """
    Verifica se la linghezza della lista di cartelle inserita corrisponde al numero
    di giocatori 
    Input
    -------
    n_giocatori (int): numero dei giocatori
    lista_cartelle (int[]): lista delle cartelle da assegnare a ciascun giocatore
    
    Output
    ------
    lista_cartelle (int[]): lista delle cartelle da assegnare a ciascun giocatore
    oppure
    un messaggio e termina il programma
    """
    if len(lista_cartelle)!=n_giocatori:    # se la lunghezza della lista di cartelle inserita 
                                            # NON corrisponde al numero di giocatori 
        print('\n- ERRORE -  Assegnazione incoerente\n')
        
        if len(lista_cartelle)<n_giocatori:
            sc=n_giocatori-len(lista_cartelle) # valore che mi dice a quanti 
                                                # giocatori mancano cartelle
            if sc == 1:
                 print(' *** Mancano cartelle a ' +str(sc)+' giocatore! ***\n')
            else:
                 print(' *** Mancano cartelle a ' +str(sc)+' giocatori! ***\n')
        
        else:
            sc=len(lista_cartelle)-n_giocatori  # valore che mi dice quanti giocatori
                                                # mancano in base alle cartelle richieste
            if sc == 1:
                print(' *** Hai assegnato troppe cartelle, manca ' +str(sc)+' giocatore! ***\n')
            else:
                print(' *** Hai assegnato troppe cartelle, mancano ' +str(sc)+' giocatori! ***\n')
                
        exit()
    for c in lista_cartelle:
        if c<=0:
            print('\n- ERRORE -  Il numero delle cartelle per giocatore deve essere almeno 1\n')
            exit()
        elif c>5:
            print('\n- ERRORE -  Il numero delle cartelle non deve superare il limite di 5 cartelle per giocatore\n')
            exit()
    return lista_cartelle

def domanda_stampa(n_giocatori,giocatori,cartellone):
    """
    Tale metodo viene chiamato dal main ad ogni estrazione e permette di mostrare
    le cartelle dei giocatori in gioco mediante il metodo 'visualizza_cartelle_giocatore' della
    classe Giocatore()
    Vengono mostrate le cartelle dei giocatori se inserito in input 'yes' o 'y', altrimenti viene stampato un messaggio e si continua il gioco
    """
    boolean = input('Vuoi vedere le cartelle dei giocatori? y/n : ')
    
    if boolean == 'y' or boolean == 'yes': 
        for i in range(n_giocatori):
            giocatori[i].visualizza_cartelle_giocatore()
    else:
        print('Ok, prossima estrazione')
