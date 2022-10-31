class Rett :
    def __init__(self,navn,pris,liste):
        self._navn = navn
        self._pris = float(pris)
        self._liste = liste

    def sjekkInnholdOK(self,substanserListe):
        for ingredient in substanserListe:
            for ingredienter in self._liste:
            if ingredient == ingredienter:
                return False
        return True

    def __str__(self):
        return 'Rett: ' , self._navn ,
        "Pris: " , self._pris ,
        "Ingredienser: " , self._liste

class Kategori:
    def __init__(self,kategori,referanseliste):
        self._kategori = kategori
        self._referanseliste = referanseliste

    def hentOkRetter(self,ingridientliste):
        self._ingrisientlise = ingridientliste
        sjekkInnholdOK(self._ingrisientlise)

class Meny:
    def __init__(self):
