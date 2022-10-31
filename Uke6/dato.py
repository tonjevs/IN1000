class Dato :
    def __init__(self,nyDag,nyMaaned,nyttAr):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyttAr = nyttAr

    def printAar():
        return self._nyttAr

    def datostreng(self,respons):
        self._respons = ("Dagens dato er:" , self._nydag , "." , self._nyMaaned , "." , self._nyttAr)
        return self._respons

    def datosjekk(self):
        if self._nyDag == 15:
            print("Loenningsdag!")
        elif self._nyDag == 1:
            print("ny måned, nye muligheter om dag er 1")
        else:
            print("Galt input")
