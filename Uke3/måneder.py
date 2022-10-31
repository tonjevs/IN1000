liste_måneder = ["Januar" , "Februar" , "Mars" , "April" ,
                "Mai" , "Juni" , "Juli" , "August" , "September" ,
                 "Oktober" , "November" , "Desember"]

svar = int(input("Skriv inn ett tall for måneden. 0 tilsvarende Januar osv: "))

if svar > 13 and svar < 0 :
    print("Beklager, kunne ikke lese dette")

else:
    print(liste_måneder[svar])
    
