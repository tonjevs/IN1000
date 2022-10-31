from student import Student
from fag import Fag


class Studentsystem:
    def __init__(self):
        self._FagLister = []
        self._StudListe = []

    def lesFraFil(self, fil):
        self._fil = fil
        fil = open("fil" , "r")
        for objekter in fil :
            if "*" in objekter:
                self._FagLister.append(objekter)
            else :
                self._StudListe.append(objekter)

    def finnStudent(self, studentNavn):
        for Studenter in self._StudListe:
            if studentNavn in self._StudListe:
                return hentStudentNavn(Student(studentNavn))
            else:
                return None

    def finnFag(self, fagNavn):
        for Fag in self._Faglister:
            if fagNavn in self._Faglister:
                return hentFagNavn(Fag(fagNavn))
            else :
                return None

    def skrivFagTilStudent(self):
        studentNavn = input("Skriv inn studentnavn: ")
        retultat = finnStudent(studentNavn)
        if resultat != None:
            print(skrivFagPaaStudent())

        elif resultat == None:
            print("Bruker finnes ikke i database...")

    def skrivStudenterTilFag(self):
        fagNavn = input("Skriv inn fagnavn: ")
        resultat = finnFag(fagNavn)
        if resultat != None:
            print(skrivStudenterVedFag())

        elif resultat == None:
            print("Fag finnes ikke i database...")

    def finnStudentMedFlestFag(self):
        tall = 0
        for studenter in self._StudListe:
            studtall = studenter.hentAntallFag()
            if tall < studtall:
                studtall = tall
                hentStudentNavn(studenter)

    def finnFagMedFlestStudenter(self):
        tall = 0
        for fag in self._FagLister:
            studtall = fag.hentAntallStudenter()
            if tall < studtall:
                studtall = tall
                hentFagNavn(fag)

    def leggTilStudent(self):
        navn = input("Skriv inn studentens navn: ")
        if navn not in self._StudListe:
            self._StudListe.append(navn)

    def leggTilFag(self):
        fagNavn = input("Skriv ut fagets navn: ")
        if fagNavn not in self._FagLister:
            self._FagLister.append(fagNavnh)

    def registrerStudentTilFag(self):
        fagNavn = input("Skriv inn fagnavn: ")
        studentNavn = input("Skriv inn studentens navn: ")
        if studentNavn not in self._StudListe:
            if fagNavn not in self._FagLister:


    def ordrelokke(self):
        inntast = ""
        while inntast != "q":
            self.skrivMeny()
            inntast = input("Skriv inn ditt valg: ")

            for _ in range(5):
                print()

            if inntast == "1":
                self.leggTilStudent()
            elif inntast == "2":
                self.leggTilFag()
            elif inntast == "3":
                self.skrivFagTilStudent()
            elif inntast == "4":
                self.skrivStudenterTilFag()
            elif inntast == "5":
                file_name = input("Filnavn: ")
                self.lesFraFil(file_name)
            elif inntast == "6":
                self.registrerStudentTilFag()
            elif inntast == "7":
                self.finnStudentMedFlestFag()
            elif inntast == "8":
                self.finnFagMedFlestStudenter()
            elif inntast != "q":
                print("Ugyldig input")

            for _ in range(5):
                print()

    def skrivMeny(self):
        print("Skriv '1' for aa legge til student.")
        print("Skriv '2' for aa legge til fag.")
        print("Skriv '3' for aa skrive fag til student.")
        print("Skriv '4' for aa skrive studenter til fag")
        print("Skriv '5' for aa lese fra fil.")
        print("Skriv '6' for aa registrere student til fag.")
        print("Skriv '7' for aa finne student med flest fag.")
        print("Skriv '8' for aa finne fag med flest studenter.")
        print("Skriv 'q' for aa stoppe programmet.")
