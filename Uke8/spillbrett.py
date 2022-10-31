from random import randint
from celle import Celle

class Spillbrett:

    def __init__(self,rader,kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = [[Celle() for kolonner in range(kolonner)] for rader in range(rader)]
        self._generasjon = 0
        self._generer()

    def tegnBrett(self):
        for i in self._rutenett:
            for j in i:
                print(j.hentStatusTegn(), end="") #henter statusen for kvar enkel plass i brettet og printer
            print() #lager ei ny linje pr rad

    def oppdatering(self):
        lever = [] #liste over kva celle som skal dø og kven som skal bli levande etter oppdaterina
        doer = []

        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):

                sjekkNabo = self.finnNabo(i,j) #finner naboene til "punktet" vi er i

                levendeNaboCelleListe = []

                for naboCelle in sjekkNabo:
                    if naboCelle.erLevende():
                        levendeNaboCelleListe.append(naboCelle) #legger til alle naboene i ei ega liste over naboer

                celle = self._rutenett[i][j] #definerer celle som den plassen vi er i rutenettet
                hovudCelleStatus = celle.erLevende() #sjekker om cella cella er levende eller dø

                if hovudCelleStatus:
                    if len(levendeNaboCelleListe) > 3 or len(levendeNaboCelleListe) < 2:
                        doer.append(celle)

                    if len(levendeNaboCelleListe) == 3 or len(levendeNaboCelleListe) == 2:
                        lever.append(celle)

                else :
                    if len(levendeNaboCelleListe) == 3:
                        lever.append(celle)

        for celler in lever:
            celler = celler.settLevende()

        for celler in doer:
            celler = celler.settDoed() #setter dei nye cellene lik dø/levende

        self._generasjon += 1
        print("Generasjon:" , self._generasjon , "Levende Celler: " , self.finnAntallLevende())



    def finnAntallLevende(self):
        levende = 0
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                if self._rutenett[i][j].erLevende():
                    levende += 1
        return levende

    def _generer(self):
        for i in self._rutenett:
            for j in i:
                seed = randint(0,2) #lager en 33% sjans for å vere levende
                if seed == 1:
                    j.settLevende()

    def finnNabo(self,rad,kolonne):
        self._sjekkRad = rad
        self._sjekkKollone = kolonne
        naboListe = [] #lager liste  for å plassere alle naboene i

        for i in range(-1, 2): # setter range slik at vi får med alle radnen
            for j in range(-1, 2):
                naboRad = self._sjekkRad + i
                naboKolonne = self._sjekkKollone + j
                gyldigTelling = True  #slik at den er True ved 'default' og eliminerer uønskaverdier


                if i == 0 and j == 0:#for å unngå at vi teller med cella vi teller fra
                    gyldigTelling = False

                if naboRad < 0 or naboRad >= self._rader:#naboRad er uten for indeksene sine
                    gyldigTelling = False


                if naboKolonne < 0 or naboKolonne >= self._kolonner:#naboSete er utenfor indeksene sine
                    gyldigTelling = False

                if gyldigTelling:
                    naboListe.append(self._rutenett[naboRad][naboKolonne]) #legger til naboene i lista
        return naboListe #returnerer lista
