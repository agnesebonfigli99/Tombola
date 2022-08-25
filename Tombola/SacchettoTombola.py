"Sacchetto"

import random

"la classe sacchetto si occupa dell'estrazione randomica dei numeri da 1 a 90 "

class Sacchetto:
    "creazione del sacchetto"
    n_sacchetto=[]
    "n_sacchetto= lista che rappresenta il sacchetto contenente i numeri da 1 a 90"

    def __int__(self):
        self.pesca=Sacchetto.n_sacchetto
        for i in range(1,91):
            self.pesca.append(i)
        Sacchetto.n_sacchetto=self.pesca

        "estrai_numero: metodo che pesca un numero dal sacchetto e lo elimina dalla lista"

    def estrai_numero(self):
        self.numeri=Sacchetto.n_sacchetto
        self.mischia=random.shuffle(self.numeri)
        self.estratto=self.numeri[0]
        self.numeri.pop(0)
        return self.estratto