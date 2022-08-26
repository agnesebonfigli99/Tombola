import numpy as np

'''Classe Giocatore: 
    - prende le cartelle 
    - controllo numero 
    - controllo vincita 
    - verifica cartella  '''
    
class Giocatore: 
    ''''username: username associato al giocatore
        n_cartelle: numero (int) di cartelle richieste dal giocatore
        cartelle_assegnate: lista inizialmente vuota che conterrà le cartelle assegnate al giocatore''''
    
    def __init__(self,username,n_cartelle, cartelle_assegnate = None):
        self.username = username 
        self.n_cartelle = n_cartelle
        self.cartelle_assegnate = []
        
    ''' Metodo Aggiungi Cartella : 
        Il giocatore prende una nuova cartella che aggiunge alle precedenti'''
    
    def aggiungi_cartella(self, nuova_cartella): 
        self.cartelle_assegnate.append(nuova_cartella)
        
    ''' Metodo Check Numero
    Dopo aver estratto il numero (intero) il giocatore controlla se le sue cartelle lo possiedono.
    0 --> al posto del numero estratto presente sulla cartella ''' 
    
    def check_num(self, num_estratto): 
        for i in range(0,len(self.cartelle_assegnate)):
            for riga in range(0,3):
                if self.cartelle_assegnate[i].cartella[riga][colonna]==num_estratto:    ''''l'iesima cartella della lista di cartelle del giocatore
                                                                                         presenta in una posizione (individuata da riga e colonna) il numero estratto''''
                    self.cartelle_assegnate[i].cartella[riga][colonna]=0 
        
    ''' Metodo Check Vincita: 
        Controllo delle vincite(interi, 2--> ambo, 3--> terno...) del giocatore'''
   ''''Per la verifica della Tombola si verifica che nella cartella siano presenti solo 0 (n estratto) e -1 (casella vuota)''''     
    def check_vincita(self,vincita): 
         for i in range(self.n_cartelle):
            if vincita==5
                                    
                occorenze = np.unique(self.cartelle_assegnate[i].cartella)
                
                if len(occorenze)==2: ''''quindi ci sono solo 0 e -1''''
                    
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
      le cartelle nel complesso
      Se nella casella è presente -1 signica che è vuota'''
      def visualizza_cartelle_giocatore(self): 
          print(f"\nCartelle di {self.username} : \n")
          for i in range(1,len(self.cartelle_assegnate)): 
              print('Cartella numero' + str(i))
              for riga in range(3): 
                  print('[', end='')
                  for colonna in range(9): 
                      if self.cartelle_assegnate[i].visualizza_elem_cartella(riga,colonna) == -1: ''''casella vuota--> stampa spazio vuoto''''
                          print(' ', end='')
                      elif self.cartelle_assegnate[i].visualizza_elem_cartella(riga,colonna) == 0: ''''numero estratto contrassegnato con *''''
                          print('*', end='')
                      else:
                          print(int(self.cartelle_assegnate[i].elemento_cartella(riga,colonna)),end=' ')
                  print(']')
                          
                    
          
        
        
       
