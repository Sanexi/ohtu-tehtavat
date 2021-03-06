from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteet = []

    def tavaroita_korissa(self):
        return len(self.tuotteet)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for i in self.tuotteet:
            summa += i.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.tuotteet.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.tuotteet.pop(poistettava)

    def tyhjenna(self):
        self.tuotteet = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.tuotteet
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
