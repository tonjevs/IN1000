class Bud:

    def __init__(self,budgiver,budStr):
        self._budgiver = budgiver
        self._budStr = budStr
        if self._budStr <= 0 :
            self._budStr = 1

    def hentBudgiver(self):
        return self._budgiver

    def hentBudStr(self):
        return self._budStr

class Annonse:

    def __init__(self,annTekst):
        self._annTeks = annTekst

    def hentTekst(self):
        return self._annTekst

    def giBud(self,hvem,belop):
        self._nyttBud = []
        nyBud = Bud(self._hvem,self._belop)
        self._nyttBud.append(nyBud)

    def antBud(self):
        return len(self._nyttBud)

    def hoyestBud(self):
        maks = 0
        for bud in self._nyttBud:
            if bud > maks:
                bud = maks
        return maks

    def kraftBud(self,hvem,belop,max):
        nyBud = giBud(self._hvem,self._belop)
        maks = hoyestBud()
        if nyBud <= maks:
            if (maks + 1) < max:
                maks = nyBud + 1


class Kategori:

    def __init__(self,katNavn):
        self._katNavn = katNavn
        self._annonseliste = []

    def nyAnnonse(self,annTekst):
        nyannonse = Annonse(self._annTekst)
        self._annonseliste.append(nyannonse)

    def hentAnnonser(self):
        return self._annonseliste

class Bruktmarked:

    def __init__(self):
        self._kategoriOrdbok = {}

    def nyKategori(self,katNavn):
        if finnKategori(katNavn):
            nyKat = Kategori(self._katNavn)
            self._kategoriOrdbok[katNavn] = nyKat
            return nyKat


    def finnKategori(self,katNavn):
        if kat in self._kategoriOrdbok:
            if katNavn == kat:
                return self._kategorier[kat]
        return None

def hovudprogram():

    marked = Bruktmarked()
    nyKat = marked.nyKategori("sykkellykt")
    ann = nyKat.nyAnnonse("New Yorker sykkellykt")

    bud1 = ann.giBud("Peter",42)
    bud2 = ann.giBud("Ann",0)
    kraftbud3 = ann.kraftBud("Mary",40,50)

    hoyesteBudStr = ann.hoyesteBud().hentBudStr()
    budGiver = ann.hoyesteBud().hentBudgiver()

    print(hoyesteBudStr , "gitt av" , budGiver)

hovudprogram()
