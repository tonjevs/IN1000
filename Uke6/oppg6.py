class Person:
    hobbyer = []

    def __init__(self,navn,alder):
        self._navn = navn
        self._alder = alder
        self.hobbyer.append(self)

    def leggTilHobbyer(self,nyHobby):
         self.hobbyer.append(nyHobby)

    def skrivHobby(self):
        for objekter in self.hobbyer:
            print(objekter)
            print("\n")

    def skrivUt(self):
        print("Navn:" , self._navn)
        print("Alder: " , self._alder)
        print("Hobbyer: " , p1.skrivHobby())

navn = input("Skriv inn ett navn: ")
alder = input("Skriv inn en alder: ")

p1 = Person(navn,alder)
svar = input("Vil du legge til en ny hobby(ja/nei): ")
while svar == "ja":
    p1.leggTilHobbyer(input("Skriv inn en hobby: "))
    svar = input("Vil du legge til en ny hobby(ja/nei): ")

if svar == "nei":
    p1.skrivUt()
