from student import student

class Fag:

    def __init__(self,fag):
        self._studentliste = []
        self._fag = fag

    def leggTilStudent(self,student):
        self._studentliste.append(student)

    def hentAntallStudenter(self):
        return len(self._studentliste)

    def hentFagNavn(self):
        return self._fag

    def skrivStudenterVedFag(self):
        print("Fag: " , hentFagNavn())
        for navn in self._studentliste:
            print(navn.hentStudentNavn() , end=", ")
        print()
