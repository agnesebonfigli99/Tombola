# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FZHk5pU3iKb_s5IE1_SnE7f7JNccd6IA
"""

import random

#la classe sacchetto si occupa dell'estrazione randomica dei numeri da 1 a 90 "

class Sacchetto:
    #creazione del sacchetto"
    n_sacchetto=[]
    #n_sacchetto= lista che rappresenta il sacchetto contenente i numeri da 1 a 90"

    def __int__(self,pesca=None):
        self.pesca=Sacchetto.n_sacchetto
        for i in range(1,91):
            self.pesca.append(i)
        Sacchetto.n_sacchetto=self.pesca

        #estrai_numero: metodo che pesca un numero dal sacchetto e lo elimina dalla lista"

    def estrai_numero(self):
     l = []
     if len(l) < 90:
      numero = random.randint(1,90)
      while numero in l:
        numero = random.randint(1,90)
        l.append(numero)
      print(str(numero))

       #l.append(numero)
       #print(l)
       

    def ciao(self):
      for i in range(0,90):
        return l[i+1]
       
       

    def controllo_lista(self): 
      print(l)

       
#Uno = Sacchetto(list(range(6)))
#k = l[0]

#k = list(range(1,91))

uno = Sacchetto()
uno.estrai_numero()
