class Student:

    def __init__(self,studBrukernavn):
        self._studBrukernavn = studBrukernavn
        emneListe = []

    def hentBrukernavn(self):
        return self._studBrukernavn

class Emne:

    def __init__(self,emneKode):
        self._emneKode = emneKode
        self._gruppeListe = []

    def nyAktivitet(self,aktivitet):
        return gruppeListe.append(aktivitet)

class Dato:

    def __init__(self,dag,maaned,aar):
        self._dag = dag
        self._maaned = maaned
        self._aar = aar

    def absoluttDato(self):
        if len(str(self._dag) != 2:
            self._dag = 0+self._dag
        elif if len(str(self._maaned) != 2:
            self._maaned = 0+self._maaned
        elif if len(str(self._aar) != 2:
            self._aar = 0+self._aar

        dato = int(self._aar+self._maaned+self._dag)
        return dato

    def __str__(self):

        if self._maaned == 09:
            maaned = "september"
        elif self._maaned == 10:
            maaned = "oktober"
        elif self._maaned == 11:
            maaned = "november"
        elif self._maaned == 12:
            maaned = "desember"

        s = self._dag , '.' , maaned , 20+self._aar
        return s

class Aktivitet:

    def __init__(self,emne,dato,aktivitetsnummer):
        self._emne = emne
        self._dato = dato
        self._aktivitetsnummer = aktivitetsnummer
        self._studReg = []
        self._studMott = []

    def leggTilRegistrertStudent(self,student):
        return self._studReg.append(student)

    def registrerOppmote(self,student):
        return self._studMott.append(student):

    def skrivUtOppmotteStudenter(self):
        for navn in self._studMott:
            print(navn)

    def absoluttDato(self,dag,maaned,aar):
        return Dato(dag,maaned,aar)

    def oppmote(self):
        return len(self._studMott)

    def __str__(self):
        s = ('Emne: ', self._emne , 'Aktivitetsnummer: ' ,
        self._aktivitetsnummer , 'Antall møtte: ', oppmote())
        return s

class Undervisningsadministrasjon:

    def __init__(self):
        emner[emneKode] = Emne(emneKode)
        datoer[dato] = Dato(dato)
        studenter[studBrukernavn] = Student(studBrukernavn)

    def lesInnFil(self,filnavn):
        fil = open(filnavn,"r")
        for linjer in fil:
            linjer = linjer.split()
            emneKode = linjer[0]
            aktivitet = linjer[1]
            dato = absoluttDato(linjer[2],linjer[3],linjer[4])
            aktivitetsnummer = emne.nyAktivitet(aktivitet)
            Aktivitet(emneKode,dato,aktivitetsnummer)
            Undervisningsadministrasjon()

        fil.close()

    def lesStudenFraFil(self,filnavn):
        fil = open(filnavn,"r")
        for linjer in fil:
            linje = linjer.split()
            student = Student(linje[0])
            emne = Emne(linje[1])
            emne.leggTilRegistrertStudent(student)
            
        fil.close()

    def skrivGrupperMedLavtOppmoete(self,antall):
        listeMedFaaMotte = []
        for emner in self._gruppeListe:
            for studenter in self._studMott:
                if len(studenter) < antall:
                    listeMedFaaMotte.append(emner)
        return listeMedFaaMotte
