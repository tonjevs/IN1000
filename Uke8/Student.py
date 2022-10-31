form fag import Fag

class Student:
    def __init__(self,navn):
        self._navn = navn
        self._fagliste = []

    def leggTilFag(self,fag):
        self._fagliste.append(fag)

    def hentAntallFag(self):
        return len(self._fag)

    def hentStudentNavn(self):
        return self._navn

    def skrivFagPaaStudent(self):
        print(hentStudentNavn):
        for fag in self._fag:
            print(fag.hentFagNavn(),  end=",")

    def tarFag(self, fag):
        return fag in self._fagliste
