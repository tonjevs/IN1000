from motorsykkel import Motorsykkel

def hovudprogram():
    Motorsykkel_1 = Motorsykkel("Yamaha","UF4520",13)
    Motorsykkel_2 = Motorsykkel("Harley Davidson" , "UT9825" , 33)
    Motorsykkel_3 = Motorsykkel("Toyota" , "HW5276" , 20)

    Motorsykkel_1.skrivUt()
    Motorsykkel_2.skrivUt()
    Motorsykkel_3.skrivUt()

    Motorsykkel_3.kjor(10)
    print("Ny kilometerstand:" , Motorsykkel_3.hentKilometerstand())

hovudprogram()
