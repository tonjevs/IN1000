from sang import Sang

def hovedprogram():

    sang1 = Sang("Lady Gaga and Bradley Cooper", "Shallow")

    # Metoden spill
    print("Spiller av test-objekt:")
    sang1.spill()

    print("Tester sjekkArtist med 'Lady Gaga and Bradley Cooper'")	# True
    print(sang1.sjekkArtist("Lady Gaga and Bradley Cooper"))
    print("Tester sjekkArtist med 'Lord Gaga'") 					# True, ett ord finnes i artistnavnet
    print(sang1.sjekkArtist("Lord Gaga"))
    print("Tester sjekkArtist med 'Sadley'")						# False
    print(not sang1.sjekkArtist("Sadley"))
    print("Tester sjekkArtist med 'a'")
    print(not sang1.sjekkArtist("a"))                              # False
    print()


        # Metoden sjekkTittel
    print("Tester sjekkTittel med 'Shallow'")						# True
    print(sang1.sjekkTittel("Shallow"))
    print("Tester sjekkTittel med 'shalLow'")						# True
    print(sang1.sjekkTittel("shalLow"))
    print("Tester sjekkTittel med 'Hallow'")						# False
    print(not sang1.sjekkTittel("Hallow"))
    print()

        # Metoden sjekkArtistOgTittel
    print("Tester sjekkArtistOgTittel med 'Bradley Cooper' og 'Shallow'")	# True
    print(sang1.sjekkArtistOgTittel('Bradley Cooper', 'Shallow'))
    print("Tester sjekkArtistOgTittel med 'Booper' og 'Shallow'")			# False
    print(not sang1.sjekkArtistOgTittel('Booper', 'Shallow'))

hovedprogram()
