#Her lager gjer ett program som konverterer farenheit til celsius
#omgjer str() til en int verdi
fahrenheit = int(input("Skriv grad i fahrenheit for omgjering til celsius: "))
print(fahrenheit , "fahrenheit er: ")

#regner deretter ut, ved bruk av formel, for celsius
omregning = (fahrenheit - 32) * (5/9)
print(omregning , "celsius")
